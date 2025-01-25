import random

def bat_first ():
    print("You are batting first")
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
    return total

def bowl_second (target):
    print("You are bowling now")
    print("Enter the number between 1 to 6")
    total = 0
    while True:
        user = int(input())
        computer = random.randint(1,6)
        print("Computer's number is ",computer)
        if user == computer:
            print("Computer is out")
            print("Computer's total score is ",total)
            break
        else:
            total += computer
            print("Computer's total score is ",total)
            if total > target:
                break
    return total
