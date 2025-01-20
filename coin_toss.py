import random

def coin_toss():
    print("Welcome to the Coin Toss Game!")
    user_call = input("Call heads or tails: ").lower()
    toss_result = random.choice(["heads", "tails"])

    if user_call == toss_result:
        print(f"You called {user_call}, and the coin shows {toss_result}. You win!")
    else:
        print(f"You called {user_call}, but the coin shows {toss_result}. You lose!")

if __name__ == "__main__":
    coin_toss()