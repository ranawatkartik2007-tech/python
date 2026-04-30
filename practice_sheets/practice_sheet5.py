
try:
    n = open("txt1.txt", "a")
    n.write("hello")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    n = open("txt2.txt", "a")
    n.write("hello")
except Exception as e:
    print(f"An error occurred: {e}")

try:
    n = open("txt3.txt", "a")
    n.write("hello")
except Exception as e:
    print(f"An error occurred: {e}")

print(" end of the code execution")


# 3

l = [1,2,3,4,5,6,7,]

for i , item in enumerate(l):
    if (i == 2 or i == 4 or i == 6):
        print(f"{item}")
        
        
        
        # 4
        
try:
     a = int(input(" enter the number "))
     b = int(input(" enter the second number "))
     print(f" the sum is {a+b}")
except ValueError as v:
     print(f"error is {v}")
     print(" value error occurred")
        
except ZeroDivisionError as e:
     print("infinite")
     
     
# 5

     
     
     
