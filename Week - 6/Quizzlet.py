def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_answers = 0
    total_questions = len(translations)

    for english, spanish in translations.items():
        prompt = "What is the Spanish translation for " + english + "?"
        user_answer = input(prompt)

        if user_answer.lower() == spanish:
            print("That is correct!")
            correct_answers += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {spanish}.")

        print()

    print(f"You got {correct_answers}/{total_questions} words correct, come study again soon!")

if __name__ == '__main__':
    main()
