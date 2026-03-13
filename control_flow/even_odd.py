num = int(input("enter the number"))
# method1
if num%2 == 0:
    print("even number")
else :
    print("odd")
# method 2
ld = num%10
even = [0,2,4,6,8]
if ld in even:
    print("even")
else :
    print ("odd")

# method 3
if((num//2)*2 == num ):
    print("even")
else:
    print("odd")

# method4
if (num&1 == 0):
    print("even")
else:
    print("odd")
    
    