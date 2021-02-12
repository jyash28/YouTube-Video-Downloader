from pytube import YouTube

url = 'paste your video url '
my_video = YouTube(url)


#get Video Title
print(my_video.title)


#get Thumbnail Image
print(my_video.thumbnail_url)



#set stream resolution
my_video = my_video.streams.get_highest_resolution()


#Download video
my_video.download()
