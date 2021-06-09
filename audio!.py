import moviepy.editor  #install moviepy

video=moviepy.editor.VideoFileClip('zeevideo.mp4')  #video must be in the same folder or you can change path
audio=video.audio #conversion

audio.write_audiofile('AudioNews.mp3') #sample output audio is saved in the folder
print("Task Done!")