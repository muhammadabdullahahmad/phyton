import random

lower_bound = 1
upper_bound = 10
max_attempts = 12
secret_number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print(f"Invalid input. Please enter a number between {lower_bound} and {upper_bound}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"
    
def play_game():
    attempts = 0
    won = False
    
    while attempts < max_attempts and not won:
        attempts += 1
        guess = get_guess()  
        result = check_guess(guess, secret_number)
        print(result)
        
        if result == "Correct":
              print(f"Congratulations! You guessed the number in {attempts} attempts.")
              won = True
              break
        else:
         print(f"{result}.try again")
        
    if not won:
            print(f"sorry you are out of attempts the secret number is {secret_number}")
    
if __name__ == "__main__" :
        print("welcome to the number guessing game")
        play_game()