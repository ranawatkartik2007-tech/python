myList = [1,2,3,4]

SquareList = [ i*i for i in myList]
print(SquareList)


# with condition
SquareList = [ i*i for i in myList if i % 2 == 0]
print(SquareList)

