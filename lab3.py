import random
from myModule import greet_user

def add_two_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

def get_random_number():
    random_num = random.randint(1, 100)
    print(f"The random number is {random_num}")

def display_menu():
    while True:
        print("\nChoose an option:")
        print("A - Run local function (add two numbers)")
        print("B - Run standard module function (get random number)")
        print("C - Run custom module function (greet user)")
        print("Q - Quit\n")

        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            add_two_numbers()
        elif choice == 'B':
            get_random_number()
        elif choice == 'C':
            name = input("What's your name? ")
            greet_user(name)
        elif choice == 'Q':
            print("Goodbye.")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    display_menu()