import random
def game(): 

    player_guess_correct =0
    player_guess_wrong = 0
    while True:
        x = (input("guess the number from 1 to 9:  "))
        y=list(range(1,10))
        z= random.choice(y)
    
        
        if  x  == "exit":
            print (f"player guess correct: {player_guess_correct}  ,  player guess wrong: {player_guess_wrong}")
            break
        try:
            x = int(x)  # Convert input to an integer
        except ValueError:
            print("Please enter a valid number or 'exit' to quit.")
            continue  # Go to the next iteration if input is invalid

        if x > z:
            print("too high")
            player_guess_wrong +=1
        elif x < z:
            print("too low")
            player_guess_wrong +=1
        else:
            print("Correct")
            player_guess_correct +=1
game()