#list is a container to store a set of values of any data types.
friends=["alice",12.5,True,23,"bob"]
#list is mutable i.e we can change the values of list.

#list indexing and slicing.
print(friends[0])     #o/p:alice
print(friends[1])     #o/p:12.5
print(friends[-1])    #o/p:bob
print(friends[0:3])   #o/p:['alice',12.5,True]
print(friends[1:])    #o/p:[12.5,True,23,'bob']


#list methods
friends.append("charlie")     #append is used to add an element at the end of the list.
print(friends)                #o/p:['alice',12.5,True,23,'bob','charlie']

friends.insert(1,"david")     #insert is used to add an element at a specific index.
print(friends)                #o/p:['alice','david',12.5,True,23,'bob','charlie']

friends.remove(23)            #remove is used to remove an element from the list.
print(friends)                #o/p:['alice',12.5,True,'bob','charlie']

friends.pop()                 #pop is used to remove the last element from the list.
print(friends)                #o/p:['alice',12.5,True,'bob']

friends.sort()                #sort is used to sort the elements of the list in ascending order.
print(friends)                #o/p:[12.5,'alice','bob',True]

friends.reverse()             #reverse is used to reverse the order of the elements in the list.
print(friends)                #o/p:[True,'bob','alice',12.5]

print(friends.index("bob"))   #index is used to find the index of an element in the list. o/p:1

print(friends.count("alice"))    #count is used to count the number of occurrences of an element in the list. o/p:1

#for a single list like list=[1,] it is considered as a integer data type not a list.
list1=[1,]
print(type(list1))
