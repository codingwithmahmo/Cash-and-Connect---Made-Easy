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