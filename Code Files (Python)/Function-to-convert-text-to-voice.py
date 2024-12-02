from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
import pygame
import io

# Dummy data for bank accounts
accounts = {
    1001: {"name": "John Doe", "balance": 1500},
    1002: {"name": "Jane Smith", "balance": 2500},
    1003: {"name": "Ali Khan", "balance": 5000},
}

# Function to play text-to-speech
def speak_text(text, language_code):
    tts = gTTS(text=text, lang=language_code)
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_data, "mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue