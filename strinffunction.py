fruit= "Mango"
length = len(fruit)
print(length)
print(fruit[0:3])
print(fruit[0:len(fruit)-2])
print(fruit[0:-1])
print(fruit[1:3])
for i in fruit:
 print(i)
#  strings are immutable
a="harry" 
# i cannot change this a not so if i need to perform some changes
# i need to perform string operations 
print(a.upper())
print(a.lower())

# string functins returns a new string instead of changing the original
#  rstrip function
b="!!!harry!!!!!!"
print(b.rstrip("!"))
# removes only traiing ! mark and not leading
# replace function is used to replace anything from the strip
print(b.replace("harry","sambhavi"))
# split() fuction converts a string into a list from and splits a string into 
# parts 
c="harry!!!! blah blah blah"
print(c.split(" "))

