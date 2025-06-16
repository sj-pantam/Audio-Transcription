import streamlit as st
import requests

st.title("🎙 Meeting Notes Generator")

audio_file = st.file_uploader("Upload audio file (mp3)")

if audio_file:
    st.audio(audio_file)

    if st.button("Generate Notes"):
        response = requests.post("http://localhost:8000/transcribe", files={"file": audio_file})

        try:
            output = response.json()
            st.subheader("📝 Summary:")
            st.write(output["summary"])
            st.subheader("✅ Action Items:")
            st.write(output["actions"])

            with st.expander("📄 Full Transcript"):
                st.text_area("Transcript", value=output["transcript"], height=300)

        except Exception as e:
            st.error("Backend returned invalid JSON or crashed:")
            st.code(response.text)
