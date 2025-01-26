import random

def bat_first ():
    print("You are batting first")
    print("You Have to set the target")
    print("Enter the number between 1 to 6")
    total = 0
    while True:
        user = int(input())
        computer = random.randint(1,6)
        print("Computer's number is ",computer)
        if user == computer:
            print("You are out")
            print("Your total score is ",total)
            break
        else:
            total += user
            print("Your total score is ",total)
    target = total + 1
    print("Computer has to score ",target)
    print("Computer is batting now")
    print("You have take the wicket of computer before it reaches the target")
    comp_total = 0
    while True:
        user = int(input())
        computer = random.randint(1,6)
        print("Computer's number is ",computer)
        if user == computer:
            print("Computer is out")
            print("Computer's total score is ",comp_total)
            if comp_total < target:
                print("You have won the match")
                print("Congratulations")
                break
            else:
                print("Computer has won the match")
                print("Better luck next time")
                break            
        else:
            comp_total += computer
            print("Computer's total score is ",comp_total)
            if comp_total >= target:
                print("Computer has won the match")
                print("Better luck next time")
                break

def bowl_first ():
    print("You are bowling first")
    print("Computer will set the target")
    print("Enter the number between 1 to 6")
    comp_total = 0
    while True:
        user = int(input())
        computer = random.randint(1,6)
        print("Computer's number is ",computer)
        if user == computer:
            print("Computer is out")
            print("Computer's total score is ",comp_total)

            break
        else:
            comp_total += computer
            print("Your total score is ",comp_total)
    target = comp_total + 1
    print("You have to score ",target)
    print("You are batting now")
    print("You have reach the target before computer takes your wicket")
    total = 0
    while True:
        user = int(input())
        computer = random.randint(1,6)
        print("Computer's number is ",computer)
        if user == computer:
            print("You are out")
            print("Your total score is ",total)
            if total < target:
                print("Computer has won the match")
                print("Better luck next time")
                break
            else:
                print("You have won the match")
                print("Congratulations")                
                break            
        else:
            total += user
            print("Your total score is ",total)
            if total >= target:
                print("You have won the match")
                print("congratulations")
                break
def toss(choice):
    print("Tossing the coin")
    toss = random.randint(1,2)
    if toss == choice:
        print("You have won the toss")
        print("What do you want to do?")
        print("1. Bat")
        print("2. Bowl")
        choice_1 = int(input("Enter 1 or 2 to chose between bat or bowl respectively: "))
        if choice_1 == 1:
            bat_first()
        elif choice_1 == 2:
            bowl_first()
        else:
            print("Invalid choice")
    else:
        print("Computer has won the toss")
        choice_2 = random.randint(1,2)
        if choice_2 == 1:
            print("Computer has chosen to bat")
            bowl_first()
        else:
            print("Computer has chosen to bowl")
            bat_first()

print("Welcome to Hand Cricket Game")
print("Let's start the game")
print("Toss time")
print("Enter 1 for Heads")
print("Enter 2 for Tails")
ch = int(input("Enter your choice: "))
toss(ch)
