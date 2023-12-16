# Import the necessary libraries
from pytube import YouTube


def download_video(video_url, download_path="/downloads"):
    # Create a YouTube object and get the video stream
    yt = YouTube(video_url)
    video = yt.streams.get_highest_resolution()
    # Download the video
    video.download(download_path)


if __name__ == "__main__":
    video_url = r""
    # Define the video URL and download path
    download_path = "/"
    download_video(video_url, download_path)
    print("Video downloaded successfully!")
