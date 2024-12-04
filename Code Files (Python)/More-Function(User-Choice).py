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