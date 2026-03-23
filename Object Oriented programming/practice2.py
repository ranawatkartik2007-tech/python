class employeee:
    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
    def print_info(self):
        print(f" name : {self.name} ,salary {self.salary} and language {self.language}")


harry = employeee("harry","c++",12345)
harry.print_info()