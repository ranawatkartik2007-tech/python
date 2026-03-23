class employee :
    language = "pyhton" # this is the class attribute
    salary= 1000

    
    
    def getinfo(self):
         print(f"Language: {self.language}, Salary: {self.salary} ")

    @staticmethod
    def greet():
            print("hello world")


harry = employee()
harry.name = "harry" #this the instance attribute
harry.getinfo()

rohan = employee()
rohan.getinfo()


