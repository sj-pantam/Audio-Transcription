# Deployment Guide

This guide will help you deploy the Meeting Notes Generator application to make it accessible on the internet.

## Frontend Deployment (Streamlit Cloud)

1. **Create a GitHub Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign up/Login with your GitHub account
   - Click "New app"
   - Select your repository
   - Set the main file path to `frontend/app.py`
   - Add environment variable:
     - Key: `BACKEND_URL`
     - Value: Your backend URL (we'll get this after backend deployment)

## Backend Deployment (Railway)

1. **Create a Railway Account**
   - Go to [Railway](https://railway.app/)
   - Sign up with your GitHub account

2. **Deploy the Backend**
   - Create a new project
   - Choose "Deploy from GitHub repo"
   - Select your repository
   - Set the root directory to `backend`
   - Add environment variables:
     ```
     PYTHON_VERSION=3.9
     ```

3. **Get the Backend URL**
   - After deployment, Railway will provide a URL
   - Copy this URL and update the `BACKEND_URL` in Streamlit Cloud

## Alternative Backend Deployment (Render)

If you prefer Render:

1. **Create a Render Account**
   - Go to [Render](https://render.com/)
   - Sign up with your GitHub account

2. **Deploy the Backend**
   - Create a new Web Service
   - Connect your GitHub repository
   - Set the root directory to `backend`
   - Set the build command: `pip install -r requirements.txt`
   - Set the start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Add environment variables:
     ```
     PYTHON_VERSION=3.9
     ```

## Testing the Deployment

1. **Test the Backend**
   - Visit your backend URL
   - You should see the FastAPI documentation

2. **Test the Frontend**
   - Visit your Streamlit Cloud URL
   - Try uploading a small audio file
   - Check if the transcription works

## Troubleshooting

1. **Backend Issues**
   - Check the logs in Railway/Render
   - Verify environment variables
   - Check if the port is correctly set

2. **Frontend Issues**
   - Check Streamlit Cloud logs
   - Verify the `BACKEND_URL` environment variable
   - Check browser console for errors

3. **Common Problems**
   - CORS issues: Add CORS middleware to backend
   - Timeout issues: Increase timeout in frontend
   - Memory issues: Check server resources

## Security Considerations

1. **Rate Limiting**
   - Consider adding rate limiting to prevent abuse
   - Add API key authentication if needed

2. **File Size Limits**
   - Current limit is 50MB
   - Adjust based on your server capacity

3. **Error Handling**
   - All errors are properly caught and displayed
   - Sensitive information is not exposed 