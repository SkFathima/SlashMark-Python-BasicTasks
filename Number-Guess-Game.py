import random
def number_guess_game():
    name = input("May I ask you for your name?\n")
    print(f"{name}, We are going to play a game. I am thinking of a number between 1 and 200.\nGo head. Guess!")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 6
    
    while attempts < max_attempts:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess == secret_number:
            attempts += 1
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("The guess of the number that you have entered is too high.")
        else:
            print("The guess of the number that you have entered is too low.")
        
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print("Try Again!")
        else:
            print(f"Nope. The number I was thinking of was {secret_number}.")
            break
    
if __name__ == "__main__":
    number_guess_game()
