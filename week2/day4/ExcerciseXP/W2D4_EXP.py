# Exercise 1: Random Sentence Generator
import random

def get_words_from_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        return content.split()

def get_random_sentence(length):
    words = get_words_from_file(r"C:\Users\USER\Documents\Sergey\DI\DI192\week2\day4\ExcerciseXP\words.txt")
    chosen_words = [random.choice(words) for _ in range(length)]
    sentence = " ".join(chosen_words)
    return sentence.lower()

def main():
    user_input = input("Enter sentence length (2–20): ")
    try:
        length = int(user_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    if length < 2 or length > 20:
        print("Please enter a number between 2 and 20.")
        return

    sentence = get_random_sentence(length)
    print(f"Generated sentence: {sentence}")

main()

# Exercise 2: Working with JSON


import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Step 1: Load the JSON string
data = json.loads(sampleJson)

# Step 2: Access the nested “salary” key
salary = data["company"]["employee"]["payable"]["salary"]
print("Salary:", salary)

# Step 3: Add “birth_date” key
data["company"]["employee"]["birth_date"] = "1980-01-01"

# Step 4: Save modified JSON to file
with open(r"C:\Users\USER\Documents\Sergey\DI\DI192\week2\day4\ExcerciseXP\employee.json", "w") as file:
    json.dump(data, file, indent=2)
print("Modified JSON saved to employee.json")