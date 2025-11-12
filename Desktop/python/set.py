#set is a collection of unique items.
#sets are mutable and unordered.
#sets do not allow duplicate values.
fruits={"apple","banana","cherry","apple"}
print(fruits)          #o/p:{'apple', 'cherry', 'banana'} duplicate 'apple' is removed

s=set()    #creating empty set
s.add("apple")
s.add("banana")
print(s)         #o/p:{'banana', 'apple'}

#adding duplicate value
s.add("apple")
print(s)       #o/p:{'banana', 'apple'} duplicate 'apple' is not added

#removing value using remove() it raises error if value not found
s.remove("banana")
print(s)          #o/p:{'apple'}

#s.remove("grape")    
#print(s)          #raises keyerror as 'grape' not found

#removing value using discard() it does not raise error if value not found
s.discard("apple")
print(s)             #o/p:set() as 'apple' is removed

s.discard("grape")
print(s)             #o/p:set() no error raised as'grape' not found

#set operations
A={1,2,3,4}
B={3,4,5,6}

#UNION  which combines all unique elements from both sets
print(A.union(B))        #o/p:{1, 2, 3, 4, 5, 6}
print(A|B)               #o/p:{1, 2, 3, 4, 5, 6}  | is union operator

#INTERSECTION which gives common elements in both sets
print(A.intersection(B))       #o/p:{3,4}
print(A&B)                     #o/p:{3,4}  & is intersection operator

#DIFFERENCE which gives elements present in first set but not in second set
print(A.difference(B))         #o/p:{1,2}
print(A-B)                     #O/P:{1,2}   - is difference operator

#SYMMETRIC DIFFERENCE which gives elements present in either of the sets but not in both
print(A.symmetric_difference(B))    #o/p:{1,2,5,6}
print(A^B)                          #o/p:{1,2,5,6}  ^ is symmetric difference operator

#set methods
print(A.isdisjoint(B))             #o/p:False as A and B have common elements 
print(A.issubset(B))               #o/p:False as all elements of A are not in B
print(A.issuperset(B))             #o/p:False as all elements of B are not in A
A.clear()                          #removes all elements from set A
print(A)                           #o/p:set()
print(len(B))                      #o/p:4   as B has 4 elements








