import random

print("Hello 🙏 User This Side Developer 😊 ....")
print("You Have to Guess a number , I will makw sure every attempts count . ")
print("Make Sure You win in first attempt . Good Luck ...")

number = random.randint(1, 100)
attempts = 0

while True :
    guess = int(input("Enter Your Guess Number : "))
    attempts += 1


    if (guess < number):
        print("Two Low . Try more higher You can do it ")

    elif(guess > number):
        print('Too High . Try a samller number Go for it ....')

    else:
        print("Hurray ! 👌🚀 You did it your guess is absolutely correct .")