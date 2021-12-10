from pytube import YouTube

def download_video(url: str, quality='high', directory='.'):
    yt = YouTube(url)
    video = None
    if quality == 'high':
        video = yt.streams.get_highest_resolution()
    else:
        video = yt.streams.first()

    video.download(directory)
    return "Video downloaded successfully"


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=9em32dDnTck'
    download_video(url)

