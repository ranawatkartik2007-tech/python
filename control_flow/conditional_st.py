age = int (input("enter the age "))
if(age>18):
    print("your arev above consent ")
elif(age < 0):
    print("negative age is not valid ")
else:
    print("below the consent ")
# greatest of four number
num1 = int(input(" enter the frist number"))
num2 = int(input(" enter the second number"))
num3 = int(input(" enter the third number"))
num4 = int(input(" enter the fourth number"))
if (num1>num2 and num1>num3 and num1>num4):
    print("first is grestsest")
elif (num2>num1 and num2>num3 and num2>num4):
    print("second is grestsest")
elif (num3>num2 and num3>num1 and num3>num4):
    print("third is grestsest")
elif (num4>num2 and num4>num3 and num4>num1):
    print("fourth is grestsest")

# marks problem
marks1 = int(input("enter the marks 1 : "))
marks2 = int(input("enter the marks 2 : "))
marks3 = int(input("enter the marks 3 : "))

total_pec = ((marks1+marks2+marks3)/300)*100
if( total_pec<= 40 and marks1<33 and marks2<33 and marks3<33 ):
    print(" your are fail , try next year")
else:
    print("congratulations, you are pass")

if ( marks1 == 0 or marks2 == 1):
    print ("omly checking ")

#practice set
p1 = " buy now"
p2 = " follow me"
p3 = " subscribe now"
p4 = " like the video"
p5 = " share the video"
mess = input(" enter the message ")
if ((p1 in mess) or (p2 in mess) ):
    print ("spam ")
else:
    print("not spam ")

# student grde
marks = int(input(" enter the marks "))
if (100 > marks > 90 ):
    print(" EX")
elif (90 > marks > 80):
    print(" A ")
elif(80 > marks > 70):
    print(" B ")  


    