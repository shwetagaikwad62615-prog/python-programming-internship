import random 
secrect_number= random.randint(1,10)
attempts =5
print("Guess the Number Between 1-10: ")
print("You have only",attempts,"Attempts")
for i in range(attempts):
    guess=int(input("Enter Your guess: "))
    if guess ==secrect_number:
        print("Congratulations 🎉👏!!!\nYou Guessed the correct Number.")
        break
    elif guess<secrect_number:
        print("To Low")
    else:
        print("To High")
else: 
    print("Game Over !!!")
    print("The correct Number was:",secrect_number)    