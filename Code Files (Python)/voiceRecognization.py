#sample text file in which we are doing the voice recognization feature by using the urdu language as well.

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

# Function to recognize speech
def recognize_speech(language_code):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            recognized_text = recognizer.recognize_google(audio, language=language_code)
            return recognized_text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError as e:
            return f"Error with the speech recognition service: {e}"

# Main Bank Management System function
def bank_management_system():
    translator = Translator()
    pygame.init()

    # Language selection
    print("Available languages: English (en), Urdu (ur), French (fr), Spanish (es), Arabic (ar)")
    language_code = input("Enter the language code you want to interact in: ").strip().lower()

    # Welcome message
    welcome_text = "Welcome to the Bank Management System. How can I assist you today?"
    translated_welcome = translator.translate(welcome_text, dest=language_code).text
    print(f"Prompt: {translated_welcome}")
    speak_text(translated_welcome, language_code)

    # User speaks an option (e.g., "Check balance", "Withdraw money")
    options_text = "Say 'Check balance' or 'Withdraw money'."
    translated_options = translator.translate(options_text, dest=language_code).text
    print(f"Options: {translated_options}")
    speak_text(translated_options, language_code)

    # Recognize the user's choice
    user_choice = recognize_speech(language_code)
    print(f"User Choice: {user_choice}")

    # Handle user choice
    if "balance" in user_choice.lower():
        # Ask for account number
        acc_prompt = "Please say your account number."
        translated_acc_prompt = translator.translate(acc_prompt, dest=language_code).text
        print(f"Prompt: {translated_acc_prompt}")
        speak_text(translated_acc_prompt, language_code)

        # Recognize the account number
        try:
            account_number = int(recognize_speech('en-US'))  # Assuming account numbers are spoken in digits
            if account_number in accounts:
                balance_text = f"Your account balance is {accounts[account_number]['balance']} dollars."
                translated_balance = translator.translate(balance_text, dest=language_code).text
                print(f"Balance: {translated_balance}")
                speak_text(translated_balance, language_code)
            else:
                error_text = "Account not found. Please try again."
                translated_error = translator.translate(error_text, dest=language_code).text
                print(f"Error: {translated_error}")
                speak_text(translated_error, language_code)
        except ValueError:
            error_text = "Invalid input. Please try again."
            translated_error = translator.translate(error_text, dest=language_code).text
            print(f"Error: {translated_error}")
            speak_text(translated_error, language_code)

    elif "withdraw" in user_choice.lower():
        withdraw_text = "Withdrawal functionality is under development."
        translated_withdraw = translator.translate(withdraw_text, dest=language_code).text
        print(f"Reply: {translated_withdraw}")
        speak_text(translated_withdraw, language_code)

    else:
        error_text = "I didn't understand your choice. Please try again."
        translated_error = translator.translate(error_text, dest=language_code).text
        print(f"Error: {translated_error}")
        speak_text(translated_error, language_code)

# Run the Bank Management System
bank_management_system()
