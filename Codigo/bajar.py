from pytube import YouTube
import os

yt = YouTube('https://youtu.be/MTn9lGKBteA')

yt.streams.filter(only_audio=True).first().download()

print("PC1_extraordinaria\Videos")
destination = str(input(">> ")) or '.'

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded.")
