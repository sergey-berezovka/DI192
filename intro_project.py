import random
secret_number = random.randint(1, 100)
attempts = 7

print("Guess the number between 1 and 100!")
print(f"You have {attempts} attempts.\n")

while attempts > 0:
    try:
        guess = int(input("Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.\n")
            continue

        if guess == secret_number:
            print("Congratulations! You guessed it!")
            break
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1
        print(f"Attempts left: {attempts}\n")

    except ValueError:
        print("Please enter a valid number.\n")

if attempts == 0 and guess != secret_number:
    print(f"Game over! The number was {secret_number}.")
