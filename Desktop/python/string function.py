#string functions
c=" hello world "
print(c.upper()) #o/p: HELLO WORLD --upper case is used to convert lower case to upper case.
print(c.lower()) #o/p:hello world  --lower case is used to convert upper case to lower case.
print(c.strip()) #o/p:hello world  --strip is used to remove spaces from both sides.
print(c.replace("world","python")) #o/p:hello python --replace is used to replace a word with another word.
print(c.split()) #o/p:['hello','world'] --split is used to split a string into a list.

d="hello"
print(d.capitalize()) #o/p:Hello --capitalize is used to conver first letter to upper case.
print(d.count("l")) #o/p:2 --count is used to count the number of occurrences of a substring in a string.
print(d.find("e")) #o/p:1 --find is used to find the index of a substring in a string.
print(d.islower()) #o/p:True --islower is used to check if all characters in a string are lower case.
print(d.isupper()) #o/p:False --isupper is used to check if all characters in a string are upper case.
print(d.startswith("he")) #o/p:True --startswith is used to check if a string starts with a substring.
print(d.endswith("lo")) #o/p:True  --endswith is used to check if a string ends with a substring.
print(d.index("l")) #o/p:2 --index is used to find the index of a substring in a string.
print(d.swapcase()) #o/p:HELLO --swapcase is used to convert upper case to lower case and vice versa.
print(d.title()) #o/p:Hello --title is used to convert the first letter of each word to upper case.

