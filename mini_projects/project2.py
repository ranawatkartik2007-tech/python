import random
n = random.randint(1,100)
guesses = 0
a = -1
while(a!= n):
    a = int(input("enter the number "))
    guesses +=1
    if a<n:
        print(" higher number plz")
    elif a>n:
        print(" lower number plz")
        
print(f"you the guess the number {n} in {guesses} attempts")    
    

