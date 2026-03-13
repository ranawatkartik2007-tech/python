marks = { 
    "Name ": " Kartik",

    "Age ": "21",



}
print(marks.get("Name11 "))
marks.pop("Age ") # delete any mention key and value
print(marks)
marks.update({"college": "JIET"}) #adding new key and value and update exixting 
print(marks)
marks.popitem()  #delete the recent added key and value
print(marks)
#sets
s = set() #empty set 
e = {1,3,2,"kartik"} #set
f = {1,43,54}
#set union and intersection 
print( e.union(f) )
#practice set
words = {
    "madad": "help",
    "hello" : "namaste"
    
    }
word = input (" enter the word you want to translate ")
print(words[word])
# problem2 /
n = input("enter the number")
f.add(int(n))
n = input("nter the number")
f.add(int(n))
n = input("enter the number")
f.add(int(n))
n = input("enter the number")
f.add(int(n))
print(f)
s.add(int(18))
s.add("18")
print(s)
# problem6
d = {}
name = input (" emnter the name :")
lang = input ("enter your fav lang: ")
d.update({name:lang})

name = input (" emnter the name :")
lang = input ("enter your fav lang: ")
d.update({name:lang})

name = input (" emnter the name :")
lang = input ("enter your fav lang: ")
d.update({name:lang})
print(d)




      