import json
import requests
from gtts import gTTS 
import os
from moviepy.editor import AudioFileClip, ImageClip


def add_image(image, audio):
    audio = AudioFileClip(audio)
    image = ImageClip(image)
    video = image.set_audio(audio)
    video.duration = audio.duration
    video.fps = 1
    video.write_videofile("joke.mp4")


def get_joke_mp3():
    file = requests.get("https://icanhazdadjoke.com/", headers= {"Accept": "application/json"})
    joke = file.json()["joke"]
    speech = gTTS(text = joke, lang = "en", slow = False)
    speech.save("readed_joke.mp3")


get_joke_mp3()
add_image("emoji.jpg", "treaded_joke.mp3")
os.system("xdg-open joke.mp4")

