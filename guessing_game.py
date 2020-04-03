import random


def start_game():
    
    print("""----------------------------
         WELCOME TO 
    'GUESS THAT NUMBER'
----------------------------""")

def high_score(score):
    
    rec.append(score)
    print("The high score is {}.\n".format(min(rec)))
    
    

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
    player_name =  input("What is your name? ")
    rec = []
    
       
#Found random generator code here: https://docs.python.org/3/library/random.html
number = random.randint(1,10)
score = 0

while True:
    
    try:    
        guess = input("Pick a number between 1 and 10:  ")
        guess = int(guess)
        
        if guess < 1 or guess > 10:
            raise ValueError("Please use a number 1-10")
            
    except ValueError as err:
            print("That wont work! {}.\n".format(err))
            
    else:
            
        if guess > number:
            print("It is lower!")
            score += 1

        elif guess < number:
            print("It is higher!")
            score += 1

        elif guess == number:
            score += 1
            print("\nYOU GOT IT {}!!! It took you {} tries".format(player_name.upper(),score))
            replay = input("Would you like to play again? [y]es/[n]o: ")
            replay = replay.lower()
                   
            if replay == "y":
                number = random.randint(1,10)
                high_score(score)
                score = 0
                continue
        
            elif replay == "n":
                score = 0
                game_running = False
                break
            
print("Great job, the game is over.")

