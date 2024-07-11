import streamlit as st
import youtube_dl
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")

# Set page title and favicon
st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon="📹",
    layout="centered"
)

st.title("📹 YouTube Video Downloader 📹")

# Input field for the user to enter the URL
url = st.text_input("Enter the URL of the YouTube video", key="url")

# Function to handle the download
def download_video(url):
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            st.write("Downloading...")
            ydl.download([url])
            st.success("Download successful!")
    except youtube_dl.DownloadError as e:
        st.error(f"An error occurred during download: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        logging.error("An unexpected error occurred: %s", e)

# Button to trigger the download
if st.button("Download"):
    if url:
        download_video(url)
    else:
        st.warning("Please enter a valid YouTube URL")
