import random
user = input("enter the choose: ")

computer = random.choice([1,2,3])
youstr= {"snake":1, "water":2, "gun":3}
rev = {1:"s", 2:"w", 3:"g"}
you = rev[user]

print(f"you choose {you} and computer choose {computer}")

if you == computer:
    print("its a tie")

else:
    if you == 1 and computer == 2:
        print("you win")
    elif you == 1 and computer == 3:
        print("you lose")
    elif you == 2 and computer == 1:
        print("you lose")
    elif you == 2 and computer == 3:
        print("you win")
    elif you ==3 and computer == 1:
        print("you win")
    elif you == 3 and computer == 2:
        print("you lose")
    else:
        print("invalid input ")

