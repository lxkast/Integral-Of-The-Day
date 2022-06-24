import scrapetube
import pafy

channel = "UCNLRwiQSPlAn_hiEM2yWIwg"
  
file = open("Integrals.txt", "w")
videos = scrapetube.get_channel(channel)
for video in videos:
    vidLink = video["videoId"]
    video = pafy.new(vidLink)
    img = video.thumb
    print(img)
    file.write(img + "\n")