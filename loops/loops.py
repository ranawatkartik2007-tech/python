# num = int (input ("enter the number"))
# for i in range (1,11):
#     print(f" {i} X {num} = {i*num}")

#     # 2
# l = [ " haeey", "Sohan", "sakshi"]
# for i in range (0, len(l)):
#     if l[i].startswith("s"):
#         print("hello",l[i])
#     #  5/


# 4
# i = 1
# sum= 0 
# while (i<=n):
#     if n>0:
#      sum +=i
#      i +=1

# print(f"sum of {n} natual numbers are {sum}")

    
# # 6
# fact = 1
# for i in range (1,n+1):
#    fact *= i 
#    i+=1


# print(f"factorail of {n} numbers is ", fact) 

# 7

# for i in range (1,n+1):
#     print(" " * (n-i)+ "*" *( 2*i-1))
# # Method 2: Using nested for loop
# n = int(input("Enter the value of n: "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for k in range(2 * i - 1):
#         print("*", end="")
#     print()
    
# 8
# n = int( input("enter a number "))
# for i in range (1,n+1):
#     for j in range(i):
#         print("*",end ="")
#     print()
   

# 9
n = int( input("enter a number "))
for i in range(1,n+1):
    if ( i == 1 or i == n):
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")


      # 10
      # 
for i in range(10,0,-1):
    print(f"{n}X{i}=  ", n*i)
    
    
