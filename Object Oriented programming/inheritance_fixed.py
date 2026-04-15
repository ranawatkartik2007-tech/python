class employee:
    programming_language = "python"
    com = "MNC"
    def show(self):
        print(f"lang is {self.programming_language} and company is {self.com}")

class prog:
    def lang(self):
        print("language is hello")

class inher(employee, prog):
    def hello(self):
        super().lang()
        print(f"hello {self}")

# Fixed version: Renamed 'lang' class attribute to 'programming_language' to avoid shadowing
# the 'lang()' method from prog class during super().lang() call.

a = inher()
a.hello()
a.show()
