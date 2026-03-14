f = open("file.txt")
# line = f.readlines()
# print(line)

'''This will make the list of all the lines present in the file and print it '''

#using Loop
line = f.readlines()
while(line  !=""):
    print(line)
    line = f.readline()
