a = 23
def hello():
    global a
    a = 10
    print(a)
    
hello()
print(a)
    
# enumerator
l = [ 1,2,3,4]
for index , item in enumerate(l):
     print(f" the index is {index} and the number is {item}")
     

     