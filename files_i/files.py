str = "kartik is a good boy "

f = open ("file.txt","r")
data= f.read()
print(data)


# write

f = open ("file2.txt","w")
f.write("happy")
f.close()
print("file.txt")

# using with
with open ("file.txt","w") as f2:
    f2.write(str)



