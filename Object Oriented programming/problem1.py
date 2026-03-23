class calculator:
    def __init__(self,num1):
        self.num1 = num1
    
    def square(self):
        print(f"The square of {self.num1} is {self.num1**2}")

    def cube(self):
        print(f"The cube of {self.num1} is {self.num1**3}")
    def seqr(self):
        print(f"The square root of {self.num1} is {self.num1**0.5}")


a = calculator(4)
a.square()
a.cube()
a.seqr()
