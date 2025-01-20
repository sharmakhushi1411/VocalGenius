import random
import time

def memory_test():
    numbers = [random.randint(1, 99) for _ in range(5)]
    print("Welcome to the Memory Test!")
    print("Remember these numbers:")
    print(numbers)
    time.sleep(5)  # Give the player time to memorize
    print("\n" * 50)  # Clear the screen
    
    user_input = input("Enter the numbers you remember, separated by spaces: ").split()
    user_numbers = [int(x) for x in user_input]
    
    if user_numbers == numbers:
        print("Well done! You remembered all the numbers!")
    else:
        print(f"Oops! The correct numbers were {numbers}.")

if __name__ == "__main__":
    memory_test()