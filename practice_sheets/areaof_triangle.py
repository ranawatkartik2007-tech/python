b = eval(input(" enter the breath of the triangle "))
h = eval(input(" enter the height of the triangle ") )
Area = 0.5 * b * h
print (" The Area of the triangle is ", Area) 


a = eval(input(" enter the first side of the triangle"))
b = eval(input(" enter the second side of the triangle"))
c = eval(input(" enter the third side of the triangle"))
s = (a + b + c) / 2
Area = (s*(s-a)*(s-b)*(s-c))**0.5
print ("area of the triangle ", Area)



A1 = eval ( input(" Enter the coefficient of square x"))
B1 = eval ( input (" Enter the coefficient of x"))
C1 = eval (input (" entre the constant "))
D = B1**2 - 4 * A1 * C1
if D > 0:
    x1 = (-B1 + D**0.5) / (2*A1)
    x2 = (-B1 - D**0.5) / (2*A1)
    print (" the roots of then quadratic equation are ", x1, "and ", x2) 





