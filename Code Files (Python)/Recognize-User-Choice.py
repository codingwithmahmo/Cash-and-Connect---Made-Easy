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