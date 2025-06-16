import streamlit as st
import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get backend URL from environment variable or use default
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

def process_audio(audio_file):
    # Show file size
    file_size = audio_file.size / (1024 * 1024)  # Convert to MB
    st.write(f"File size: {file_size:.2f}MB")
    
    # Audio player
    st.audio(audio_file)

    # Process button
    if st.button("Generate Notes", type="primary"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Upload phase
            status_text.text("Uploading file...")
            progress_bar.progress(20)
            
            # Make request to backend
            response = requests.post(
                f"{BACKEND_URL}/transcribe",
                files={"file": audio_file},
                stream=True,
                timeout=300  # 5-minute timeout
            )
            
            progress_bar.progress(40)
            status_text.text("Transcribing audio...")
            
            # Handle errors
            if response.status_code == 413:
                st.error("File too large! Please upload a file smaller than 50MB.")
                return
            elif response.status_code != 200:
                st.error(f"Error: {response.status_code} - {response.text}")
                return
                
            output = response.json()
            
            progress_bar.progress(80)
            status_text.text("Generating summary and action items...")
            
            # Display results in columns
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📝 Summary")
                st.write(output["summary"])
            
            with col2:
                st.subheader("✅ Action Items")
                st.write(output["actions"])

            # Full transcript in expander
            with st.expander("📄 Full Transcript", expanded=False):
                st.text_area("Transcript", value=output["transcript"], height=300)
                
            progress_bar.progress(100)
            status_text.text("Done!")
            time.sleep(1)
            progress_bar.empty()
            status_text.empty()

        except requests.exceptions.Timeout:
            st.error("Request timed out. The file might be too large or the server is busy.")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to the server. Please check your internet connection.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
        finally:
            progress_bar.empty()
            status_text.empty()

# Page config
st.set_page_config(
    page_title="Meeting Notes Generator",
    page_icon="🎙",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
    }
    .main {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎙 Meeting Notes Generator")
st.markdown("""
    Upload your meeting audio file and get an AI-generated summary, action items, and full transcript.
    Supports MP3 files up to 50MB.
""")

# File uploader
audio_file = st.file_uploader("Upload audio file (mp3)", type=['mp3'])

if audio_file:
    process_audio(audio_file)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit, FastAPI, and Whisper")
