import streamlit as st
from pytube import YouTube

# Set page title and favicon
st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon="📹"
)

# Set app background color
st.markdown(
    """
    <style>
        body {
            background-color: #f2f2f2;
        }
        .stTextInput {
            background-color: #d9d9d9;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("YouTube Video Downloader")

# Input field for the user to enter the URL
url = st.text_input("Enter the URL of the YouTube video", key="url")

# Checkbox for auto-selecting best resolution
auto_resolution = st.checkbox("Automatically select best resolution")

# Dropdown menu for selecting video resolution
resolution_options = ["144p", "240p", "360p", "480p", "720p", "1080p"]
if not auto_resolution:
    resolution = st.selectbox("Select Video Resolution", resolution_options)

# Button to trigger the download
if st.button("Download"):
    if url:
        try:
            yt = YouTube(url)
            if auto_resolution:
                stream = yt.streams.get_highest_resolution()
            else:
                if resolution == "144p":
                    stream = yt.streams.filter(res="144p", file_extension="mp4").first()
                elif resolution == "240p":
                    stream = yt.streams.filter(res="240p", file_extension="mp4").first()
                elif resolution == "360p":
                    stream = yt.streams.filter(res="360p", file_extension="mp4").first()
                elif resolution == "480p":
                    stream = yt.streams.filter(res="480p", file_extension="mp4").first()
                elif resolution == "720p":
                    stream = yt.streams.filter(res="720p", file_extension="mp4").first()
                elif resolution == "1080p":
                    stream = yt.streams.filter(res="1080p", file_extension="mp4").first()

            stream.download()
            st.success("Download successful!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube URL")
