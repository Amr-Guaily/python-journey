import random
import string

print("Welcome to the password Generator!")

password_length = int(input("Enter the total number of characters in the password: "))

letters_length = int(input("Enter the number of letters in the password: "))
numbers_length = int(input("Enter the number of numbers in the password: "))
symbols_length = int(input("Enter the number of symbols in the password: "))

if (letters_length + numbers_length + symbols_length) > password_length:
    print("The total number of characters in the password should be equal to the sum of letters, numbers, and symbols")
    exit()

letters = random.choices(string.ascii_letters, k=letters_length)
numbers = random.choices(string.digits, k=numbers_length)
symbols = random.choices(string.punctuation, k=symbols_length)

password = letters + numbers + symbols

# for i in range(letters_length):
#     password.append(random.choice(letters))

# for i in range(numbers_length):
#     password.append(random.choice(numbers))

# for i in range(symbols_length):
#     password.append(random.choice(symbols))

random.shuffle(password)

password = "".join(password)

print(f"Your password is: {password}")