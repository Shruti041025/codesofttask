import random

user_choice = int(input("enter the choice of user : Type 0 is for rock,Type 1 is paper,Type 2 is for scissors\n"))

if user_choice >= 3 or user_choice < 0  :
   print("invalid and you loose")
else :
computer_choice = random.randint(0,2)
print("computer choose")
print(computer_choice)
if computer_choice == user_choice:
    print("the game is draw")
elif user_choice == 2  and computer_choice == 0:
    print("user loose the game")
elif user_choice == 0 and computer_choice == 2:
    print("you won the game")
elif computer_choice > user_choice:
        print(" user loose the game")
elif user_choice > computer_choice:
    print("user won the game")
