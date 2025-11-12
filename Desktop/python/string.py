#string is a data type in python.
a="harry"
#string is immutable i.e we cannnot change the values of string.
#srting slicing is used to get a part of the string.
print(a[0:3]) #output:har
print(a[1:4]) #output:arr
print(a[:4])  #output:harr
print(a[2:])  #output:rry
print(a[:])  #output:harry
print(a[-4:-1])  #output:arr
print(a[-4:]) #output:arry
print(a[:-2]) #output:har
print(a[-3:]) #o/p:rry
print(a[-1:]) #o/p:y
print(a[:-1]) #o/p:harr
print(a[-5:-2]) #o/p:har

#slicing with step
b="abcdefghhij"
print(b[0:10:2]) #o/p:acegi
print(b[1:10:3]) #o/p:bdfhj
print(b[::2]) #o/p:aceghj


