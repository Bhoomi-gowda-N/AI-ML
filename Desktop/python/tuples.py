#tuple is a immutable data type in python.
my_tuple=("apple",11,True,5.6)
tuple=(1,)

#tuple methods
print(my_tuple.count("apple"))    #count is used to count the number of occurences of an elemrnt   O/p:1
print(my_tuple.index(11))         #index is used to find the index of an element   O/p:1
print(type(tuple))        #o/p:<class 'tuple'>

#tuple unpacking
a,b,c,d=my_tuple
print(a)   #o/p:apple
print(b)   #o/p:11
print(c)   #o/p:True
print(d)   #o/p:5.6

#nested tuple
nested_tuple=(1,2,(3,4),5)
print(nested_tuple[2])              #o/p:(3,4)
print(nested_tuple[2][1])           #o/p:4

#tuple concatenation
tuple1=(1,2,3)
tuple2=(4,5,6)
concatinated_tuple=tuple1+tuple2
print(concatinated_tuple)              #o/p:(1,2,3,4,5,6)

#tuple repetition
repeted_tuple=tuple1*3
print(repeted_tuple)                   #o/p:(1,2,3,1,2,3,1,2,3)

#tuple slicing
sliced_tuple=concatinated_tuple[2:5]
print(sliced_tuple)                     #o/p:(3,4,5)

#tuple length
print(len(my_tuple))                     #o/p:4

#tuple membership  membership operators means to check whether an element is present in the tuple or not (in operator and not in operator)
print(11 in my_tuple)                    #o/p:True
print("banana" not in my_tuple)          #o/p:True

#iterating through a tuple
for item in my_tuple:
    print(item)                     #o/p:apple 11 True 5.6

#tuple conversion  it is used to covert other data types to tuple and tuple to other data types
list_from_tuple=list(my_tuple)      #it converts tuple to list
print(list_from_tuple)              #o/p:['apple',11,True,5.6]
set_from_tuples=set(my_tuple)       #it converts tuple to set
print(set_from_tuples)              #o/p:{True,5.6,'apple',11}
string_from_tuples=str(my_tuple)    #it converts tuple to  string
print(string_from_tuples)           #o/p:"('apple',11,True,5.6)"
tuple_from_list=tuple(list_from_tuple)    #it converts list to tuple
print(tuple_from_list)                    #o/p:('apple',11,True,5.6)


#empty tuple
empty_tuple=()
print(empty_tuple)             #o/p:()

#single element tuple
single_element=(5,)
print(single_element)          #o/p:(5,)

