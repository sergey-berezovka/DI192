from anagram_checker import AnagramChecker
import os

def main():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "sowpods.txt")

    checker = AnagramChecker(file_path)

    while True:
        print("\n1. Enter a word")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "2":
            print("Goodbye!")
            break

        elif choice == "1":
            user_input = input("Enter a word: ").strip()

            if len(user_input.split()) != 1:
                print("Error: Only one word allowed.")
                continue

            if not user_input.isalpha():
                print("Error: Only alphabetic characters allowed.")
                continue

            word = user_input.lower()

            print(f"\nYOUR WORD: \"{word.upper()}\"")

            if checker.is_valid_word(word):
                print("This is a valid English word.")
            else:
                print("This is NOT a valid English word.")

            anagrams = checker.get_anagrams(word)

            if anagrams:
                print("Anagrams:", ", ".join(anagrams))
            else:
                print("No anagrams found.")

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()