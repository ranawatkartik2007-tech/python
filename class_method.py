class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f" the class atribute is {cls.a}")


class twod:
    def __init__(self, i,j):
        self.i = i
        self.j = j 

    def show(self):
        print(f"the 2d vector is {self.i}i + {self.j}j ")

class threed(twod):
    def __init__(self,i,j,k):
       super().__init__(i,j)
       self.k = k 


    def show(self):
        print(f"the 3d vector is {self.i}i + {self.j}j+ {self.k}k ")


a = twod(2,3)
a.show()
b = threed(3,4,5)
b.show()

class employee:
    salary= 230
    increment = 20

    @property
    def salaryafterinc(self):
        return (self.salary + self.salary*(self.increment/100) )
    
e = employee()
print(e.salaryafterinc)


    