# n1 = int(input("enter the first number "))
# n2 = int(input("enter the second number "))
# if n1 < n2:
#     for num in range (n1,n2+1):
#         if num < 2:
#             continue
#         is_true = True
#         for i in range (2,num):
#             if num % i == 0:
#                 is_true = False
#                 break
#         if is_true:
#           print(num) 
         


# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))

# # Optional: Ensure n1 < n2
# if n1 > n2:
#     print("Error: n1 should be less than n2")
# else:
#     print(f"Prime numbers between {n1} and {n2}:")
    
#     for num in range(n1, n2 + 1):
#         if num < 2:
#             continue
        
#         is_prime = True
        
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:  # ✅ Now inside the main loop
#             print(num)



            # 2
# num = int(input("Enter the  number: "))
# temp = num 
# while( num>0):
#     num  = num  // 10
#     count  = count + 1

# sum =0 
# while (temp>0):
#     digit = temp % 10
#     sum = sum + digit ** count
#     temp = temp // 10


# if sum == num:
#     print("the number is armstrong")
# else:   
#     print("the number is not armstrong")


# num = int(input("Enter the  number: "))
# temp = num 
# count = 0
# while( num>0):
#     num  = num  // 10
#     count  = count + 1

# sum =0 
# while (temp>0):
#     digit = temp % 10
#     sum = sum + digit ** count
#     temp = temp // 10


# if sum == num:
#     print("the number is armstrong")
# else:   
#     print("the number is not armstrong")



# 3/
# num1 = int(input("Enter the  number: "))

# for i in range (1, num1+1):
#     for j in range (i):
#         print(chr(65+j),end = " ")
#     print()      
# # 4
# num = int(input("Enter the  number: "))
# for i in range (1,num+1):
#     print(" "*(i-1)+ "*"*1)

    

    # 5
# num = int(input("Enter the  number: "))
# for i in range (1,num+1):
#     print(" "*(num-i)+"*"*1)


#6
password = input(" Enter the password: ")
if not 8<= len(password)<=14:
    print("password must be between 8 and 14 characters")
is_upper = False
is_lower = False
is_symbol = False
is_digit = False

l = ["@","#","$","%","&"]
for i in range (len(password)):
    if password[i].isupper():
            is_upper = True

    elif password[i].islower():
            is_lower = True

    if password[i] in l:
            is_symbol = True

    if password[i].isdigit():

         is_digit = True

if (is_upper and is_lower and is_symbol and is_digit):
    print("the password is valid")
else:
    print("the password is not valid") 

# 7


