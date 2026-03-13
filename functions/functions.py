# def greet(name):
#     print (f"good day "+ name,sep = "&")
#     return "G"

# a = greet("kartik")
# print (a)


# #recursion 

# def factorial(n):
#     if (n ==1 or n ==0):
#         return 1
#     return n*factorial(n-1)

# n = int (input ("enter a number "))

# print(f"factorial of the number is {factorial(n)}")


# # practice set/
# a = 1
# b = 2
# c = 3 
# def greatest(a,b,c):
#     if( a>b and a<b ):
#         return ("a is greatest ") 
        
#     elif( c>b and c>a ):
#         return ("c is greatest ") 
#     elif( b>c and b>a ):
#         return ("b is greatest ") 
# print(greatest(a,b,c))



#  temp
# temp = int(input(" enter the temp in farhniet"))

# def convert(x):
#     c = 5 *(x-32)/9
#     return c

# print(convert(100))

#recursion problem

# def sum(n):
#     if n == 0:        # Base case
#         return 0
#     return sum(n-1) + n  # Recursive case

# n = int(input("Enter a number: "))
# print(sum(n))


# pattern 


# 7
# word = input("enter the word to be removed ")
# def remove(l , word):
#     n  =[]
#     for item in l :
#         if not (item ==  word):
#             n.append(item.strip(word))
#     return n

# l = [ "kartik", "hardik", "artik"]

# print(remove(l,"k"))

# 8


def multiply(n):
    for i in range (1,11):
        print (f"{n}X{i} = {n*i}")
    
multiply(5)