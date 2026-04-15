class employee:
    lange = "python"
    com = " MNC"
    def __init__(self):
        print("vonstructor1")

    def show(self):
        print(f"lang is {self.lange}and company is {self.com}")

class prog:
    def lang(self):
        print("language is hello")

class inher(employee,prog):
    def hello(self):
        # super().__init__()
        print (f"hello{self}")


a = inher()
a.hello()
a.show()


