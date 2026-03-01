import random

# Introduction to user 

print("Welcome to SPKA Games 👏👏")
print("Let's Play the game 🚀.. Stone🗿,Paper📜 & Scisors✂️ ")

## Providing list of choices to code 

options = ["Stone","Scissors","Paper"]

## Now code for user to choose choice 

while True:
    choice_u = input("Choose your choice In between 3 (Stone,Scissors,Paper) :")

    if choice_u not in options:
        print("Invalid choice! Try again.")
        continue

    choice_c: str = random.choice(options)

## Now clashing in between computer choicce and users choice 

    if ( choice_c == choice_u):
        print("Draw 🤝 .. Try Again..")

        print("You choose : ")
        print("Bot Choice : ")

    elif ( (choice_u == "Paper" and choice_c == "Stone") or (choice_u == "Scissors" and choice_c == "Paper" ) or (choice_u == "Stone" and choice_c == "Scissors")):
        print("Congratulations ! 👏 You Won 🏆...")

    else:
        print("You Lose , Try Again .. ")

## Try again code 

play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing 👋")
        break



