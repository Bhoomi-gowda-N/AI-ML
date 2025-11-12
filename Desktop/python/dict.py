#dictionary is a collection of key-vaule pairs.
#dictionary is mutable and unordered.
words={
    "A":"apple",
    "B":"banana",
    "C":"cherry",
    "D":"dog"
}
print(words)

#accessing values using keys
print(words["A"])                         #o/p:apple
print(words.get("B"))           #o/p:banana  get method is used to access values using key if key is not found it returns None or default value if provided.
print(words.get("E","not found"))         #o/p:not found

#adding new key-value pair
words["E"]="elephant"
print(words)             #o/p:{'A': 'apple', 'B': 'banana', 'C': 'cherry', 'D': 'dog', 'E': 'elephant'}

#updating value of existing key
words["A"]="avacado"
print(words)          #o/p:{'A': 'avacado', 'B': 'banana', 'C': 'cherry', 'D': 'dog', 'E': 'elephant'}

#removing key-value pair using del it completely removes the key-value pair from dictionary
del words["D"]
print (words)         #o/p:{'A': 'avacado', 'B': 'banana', 'C': 'cherry', 'E': 'elephant'}

#removing key-value pair using pop it removes the key-value pair and returns the value of the removed key for example:we had removed key "C" but we can still access its value example:
removed_value=words.pop("C")
print(removed_value)          #o/p:cherry
print(words)                  #o/p:{'A': 'avacado', 'B': 'banana', 'E': 'elephant'}

#removing last inserted key-value pair using popitem
last_item=words.popitem()
print(last_item)               #o/p:('E', 'elephant')
print(words)                   #o/p:{'A': 'avacado', 'B': 'banana'}


#dictionary methods
print(words.keys())                   #o/p dict_keys(['A', 'B'])
print(words.values())         #o/p:dict_values(['avacado', 'banana'])
print(words.items())          #o/p:dict_items([('A', 'avacado'), ('B', 'banana')])





