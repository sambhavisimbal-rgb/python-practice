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
print(c.capitalize())
# capitaise() is used to only turn the first letter of the string into uppercase
# and rest other are converted to lowercase
print(c.center(40))
print(c.center(60))
# count() counts how many times a paricular charachter or sequence of character is 
# occuring in tht string
print(c.count("blah"))
print(c.count("b"))
#  endswith() checks wheter a given string ends with a given charachter or not.
#  returns true if yes false if no
print(c.endswith("blah"))
print(c.endswith("bl"))
#  we can even also check for a value in between the string by providing start and
# end index positioon
print(c.endswith("!!!",0,8))
# find() searches for the first occurence of the given value and returns the
# index where it is present. -1 if not present
print(c.find("bl"))
# isalnum() used to check if string carries any special character other
# than a-z A-Z and 0-9
# isalpha() checks only alphabets and true if only alphabets are present
#  isspace()- true if spaces available
#  isprintable()- returns if only printabe characters are present
#  swapcase() changes uppercase to lowercase and vice versa
