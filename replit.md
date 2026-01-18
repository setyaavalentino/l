# YouTube Live Streaming App

## Overview
A Streamlit-based application for YouTube live streaming with Google OAuth authentication. The app allows users to authenticate with their YouTube/Google account and manage live streaming sessions.

## Project Structure
- `app.py` - Main application file containing all functionality
- `.streamlit/config.toml` - Streamlit configuration for server settings
- `requirements.txt` - Python dependencies
- `packages.txt` - System dependencies (ffmpeg)

## Tech Stack
- **Framework**: Streamlit (Python)
- **APIs**: Google OAuth 2.0, YouTube Data API v3
- **Database**: SQLite (local file: streaming_logs.db)
- **Video Processing**: FFmpeg, OpenCV

## Running the App
The app runs on port 5000 with:
```
python -m streamlit run app.py
```

## Configuration
Streamlit is configured in `.streamlit/config.toml`:
- Runs on `0.0.0.0:5000` 
- Headless mode enabled
- CORS and XSRF protection disabled for Replit proxy compatibility

## Dependencies
Key Python packages:
- streamlit
- google-auth, google-auth-oauthlib, google-api-python-client
- ffmpeg-python, opencv-python-headless
- pandas, numpy, pillow

System dependencies:
- ffmpeg
