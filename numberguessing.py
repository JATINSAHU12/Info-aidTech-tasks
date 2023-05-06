import random


def game():
    random_number = random.randint(1, 100)
    trials = 1
    guess = 0

    def trials_reminder():
        i = 10 - trials
        print("You have " + str(i) + " trials left!")
    while guess != random_number and trials <= 10:
        guess = int(input("\nEnter a number: "))
        if guess < random_number-10:
            print("\nYour guess is way too far, try a higher one.")
            trials_reminder()
        elif guess > random_number+10:
            print("\nYour guess is way too far, try a lower one.")
            trials_reminder()
        if random_number - 10 < guess < random_number:
            print("\nYour guess is so close, try a higher one.")
            trials_reminder()
        elif random_number + 10 > guess > random_number:
            print("\nYour guess is so close, try a lower one.")
            trials_reminder()
        elif guess > 100 or guess < 1:
            print("\nCould you please make sure you picked an integer between 1 and 100!")
        trials += 1
    if guess == random_number:
        print("\nNice job pal, you guessed the right number which is: " + str(random_number))
        decision()
    elif guess != random_number:
        print("\nSorry mate, you're out of trials.\n \n The right number is " + str(random_number))
        decision2()


def decision():
    carry_on = input("\n\nDo you want to play again?\n type 'p' for play or 'q' for quit: ")
    if carry_on == "p":
        game()
    elif carry_on == "q":
        print("\nI hope you have a wonderful day. Bye, " + name + ".")
    else:
        print("\nPlease, Enter a valid letter")
        decision()


def decision2():
    carry_on = input("\n\nI know you can do it pal.\nDo you wanna try your luck again ?\n type 'p' for play or 'q' for quit: ")
    if carry_on == "p":
        game()
    elif carry_on == "q":
        print("\nI hope you have a wonderful day. Bye, " + name + ".")
    else:
        print("\nPlease, Enter a valid letter")
        decision2()


print("Please enter your name ")
name = input()
print("\nBonjour " + name + ", Let's play a little quick game called 'Guess my number'.\nYou have to guess a number between 1 and 100.")
print("If you wanna win, you have to get the right number within 10 trials,\nand if you fail to get it, you lose.")
print("Good luck with the guessing buddy.\n")
game()