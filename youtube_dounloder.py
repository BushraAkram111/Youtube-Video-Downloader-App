import streamlit as st
import yt_dlp

# Set page title and favicon
st.set_page_config(
    page_title="YouTube Video Downloader",
    page_icon="📹",
    layout="centered"
)

# Custom CSS for both dark and light modes
st.markdown(
    """
    <style>
        body {
            background-color: var(--background-color);
        }
        .stTextInput div, .stCheckbox div, .stSelectbox div {
            background-color: var(--element-background-color);
        }
        .stButton button {
            background-color: var(--button-background-color);
            color: var(--button-text-color);
            border: none;
            padding: 10px 24px;
            text-align: center;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .stButton button:hover {
            background-color: var(--button-hover-background-color);
        }
    </style>
    <script>
        const root = document.documentElement;
        const observer = new MutationObserver(() => {
            const darkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
            if (darkMode) {
                root.style.setProperty('--background-color', '#2e2e2e');
                root.style.setProperty('--element-background-color', '#454545');
                root.style.setProperty('--button-background-color', '#4CAF50');
                root.style.setProperty('--button-text-color', '#ffffff');
                root.style.setProperty('--button-hover-background-color', '#45a049');
            } else {
                root.style.setProperty('--background-color', '#f7f7f7');
                root.style.setProperty('--element-background-color', '#e8e8e8');
                root.style.setProperty('--button-background-color', '#4CAF50');
                root.style.setProperty('--button-text-color', '#ffffff');
                root.style.setProperty('--button-hover-background-color', '#45a049');
            }
        });
        observer.observe(root, { attributes: true, attributeFilter: ['class'] });
    </script>
    """,
    unsafe_allow_html=True
)

st.title("📹 YouTube Video Downloader 📹")

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
        ydl_opts = {
            'format': 'best' if auto_resolution else f'bestvideo[height<={resolution[:-1]}]+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                st.success("Download successful!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid YouTube URL")
