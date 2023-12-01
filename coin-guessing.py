import random

choice = int(input("""
Welcome to the coin guessing game!
Choose a method to toss the coin:
1. using randowm.random()
2. using random.randint()
Enter your choice (1 or 2):
""")) 

if choice == 1:
    random_num = random.random()
    if random_num >= 0.5:
        computer_result = "Heads"
    else:
        computer_result = "Tails"

elif choice == 2:    
    if  random.random() == 0:
        computer_result = "Heads"
    else:
        computer_result = "Tails"
else:
    print("Invalid choice. Please select either 1 or 2.")
    exit()

user_choice = input("Enter your Guess (Heads or Tails): ")

if user_choice.lower() == computer_result.lower():
    print("Congratulations! You won.")
else:
    print("Sorry, you lost.")

print(f"The computer's coin toss result was {computer_result}.")    


