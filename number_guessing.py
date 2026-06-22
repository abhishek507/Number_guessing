
# use random.randint to generate a random number
# start a wile loop to iterate until the condition satisfies 
# user input to guess the number
# if user guess is correct return you got it right .if guess is 2 high return too high and if guess is too low return too low.
# if input is other than 1 to 100 than return invalid 

import random

random_number = random.randint(1,100)
counter = 0

while True:
   
    try:
        guess = int(input("Guess the number between 1 to 100 : "))
        

        if random_number == guess:
            print("congratulations you guessed the correct number")
            counter+=1
            print(f"no of time you have guessed : {counter} times  and finally you  won!")
            break
        
        elif random_number > guess:
            print(" you guessed too low")
            counter+=1
            print(f"no of time you have guessed : {counter}")

        elif (guess > 100 or guess < 1):
            print("enter between 1 to 100")

        
        else:
            print("you guessed to high")
            counter+=1
            print(f"no of time you have guessed : {counter}")
        


    except ValueError:
        print("enterd a invalid input")
        
        
