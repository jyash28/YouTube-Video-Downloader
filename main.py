from pytube import YouTube

url = ' paste your url here'
my_video = YouTube(url)


#get Video Title
print(my_video.title)


#get Thumbnail Image
print(my_video.thumbnail_url)

#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

#set stream resolution
my_video = my_video.streams.get_highest_resolution()


#Download video
my_video.download()
