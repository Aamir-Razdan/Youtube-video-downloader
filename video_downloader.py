# from pytube import YouTube
# link=str(input("Enter your link:"))
# yt=YouTube(link)
# stream=yt.stream.get_highest_resolution()
# stream.download()
# print("Download sucessfully")


from pytube import YouTube
from http.client import IncompleteRead
#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)
# var_regex = re.compile(r"^\$*\w+\W")
#Showing details

print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")



