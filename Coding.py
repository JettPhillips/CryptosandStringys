#Stirngs

#Concatination
#   2 strings or more and put them together

firstName = "Jesus"
lastName = "Christ"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName
print("  ")

#Repetition

print("Hip "*2 + "Hooray!")
def knockKnock():
    print("Knock "*2)
    print("Who's There")

knockKnock()

#Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])

print(name[-1])

for i in range(0, len(name)):
    print(name[i])

#Slicing and dicing

print(name[4:-3])

for i in range(0, len(name)+1):
    print(name[0:i])

# Searching

print("biv" in name)

if "y" not in name:
    print("y is not in name")
else:
    print("y is in name")

# String Methods to investigate:
# Method        Use Example         Explanation
# center        aStr.center(w)
# ljust         aStr.ljust(w)
# rjust         aStr.rjust(w)
# upper         aStr.upper()
# lower         aStr.lower()
# index         aStr.index(item)
# rindex        aStr.rindex(item)
# find          aStr.find(item)
# rfind         aStr.rfind(item)
# replace       aStr.replace(old, new)

# Be sure to include multiple examples of all of them in use

print(ord("a"))
print(chr(75))

from mapper import *
print(letterToIndex('M'))

print(indexToLetter(44))