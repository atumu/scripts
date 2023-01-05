## This converter has been made by mGz1337 ##
## This is an open source and a free tool ##
## This is used to convert a mp4 file to mp3 ##
## Never use this app for illegal, unethical, damaging purposes. I'm not responsible for your actions! ##

from moviepy.editor import *
try :
    video = input("What is the name of your file? (include mp4) >> ")
    mp4_file = video
    mp3_file = "{}.mp3".format(mp4_file)
    videoClip = VideoFileClip(mp4_file)
    audioclip = videoClip.audio
    audioclip.write_audiofile(mp3_file)
except NameError:
    print("")
    exit("You either didn't install the moviepy library, or you didn't put the correct name! Be sure to include mp4")
except OSError:
    print("")
    exit("You either didn't install the moviepy library, or you didn't put the correct name! Be sure to include .mp4 after the song name!")
audioclip.close()
videoClip.close()
print("")
exit("The mp4 file has been successfully converted to mp3. Enjoy! :)")
