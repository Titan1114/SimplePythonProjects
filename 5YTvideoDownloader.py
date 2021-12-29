# put the url link and that yt video will be automatically downloaded on your desktop.
from pytube import YouTube

url=input("Enter your url link:  ")

my_video = YouTube(url)

print(my_video.thumbnail_url)
print(my_video.title)

my_video=my_video.streams.get_lowest_resolution()

my_video.download()

