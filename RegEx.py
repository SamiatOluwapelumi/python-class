import re
from xml.dom.pulldom import CHARACTERS
# Search the string to see if it starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#       print("YES! We have a match!")
# else:
#   print("No match")

# y=re.search('in',txt)
# if y:
#     print('yes')

# META CHARACTERS

#1.Find all lower case characters alphabetically between "a" and "m":
txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)


#2.Find all digit characters:
txt = "That will be 59 dollars"
x = re.findall("\d", txt)
print(x)


#3.Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
txt = "hello planet"
x = re.findall("p....t", txt)
print(x)


#4.Check if the string starts with 'hello':
txt = "hello planet"
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


#5.Check if the string ends with 'planet':
txt = "hello planet"
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")


#6.Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
txt = "hello planet"
x = re.findall("he.*o", txt)

print(x)



#7.Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
txt = "hello planet"
x = re.findall("he.+o", txt)

print(x)


#8.Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
txt = "hello planet"
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

#9.Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
txt = "hello planet"
x = re.findall("he.{2}o", txt)

print(x)

#10.Check if the string contains either "falls" or "stays":
txt = "The rain in Spain falls mainly in the plain!"
x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
