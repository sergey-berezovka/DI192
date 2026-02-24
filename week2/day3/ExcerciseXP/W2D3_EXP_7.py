#Exercise 7: Faker Module
from faker import Faker

fake = Faker()

users = []

def add_users(number_of_users):
    for _ in range(number_of_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

add_users(5)

print(users)