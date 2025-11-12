#tables
'''
for i in range(1,20):
  for j in range(1,10):
   print(f"{i}x{j}={i*j}")
'''
       

#to access name starting with s in list
'''
l=["harry","srinivas","bhoomika","sahil"]
for name in l:
     if name.startswith("s"):
        print(f"hello {name}")
'''


#to find sum of natural numbers
'''
n=int(input("numbers"))
i=0
sum=0
while(i<=n):
     sum+=i
    i+=1
print(sum)
'''


#factorial
'''
n=int(input("number"))
product=1
for i in range(1,n+1):
    product*=i
print (f"fact of {n} is {product}")
'''

#pattern programs
'''
  *
 ***
*****
'''
'''

n=int(input("number"))
for i in range(1,n+1):
    print(" "*(n-i),end="")    #end gives by default new line after print it is an argument. its is used for spaces
    
    print("*" * (2*i-1),end="") # its for printing *
    print("")
    '''

'''
*
**
***
'''
'''
n=int(input("number"))
for i in range(1,n+1):
    print("*" *i,end="")
    print("")
'''

'''
* * *
*   *
* * *
'''
'''
n=int(input("number"))
for i in range(1,n+1):
    if (i==1 or i==n):
        print("*"* n)  
    else:  
      print("*",end="")
      print(" "*(n-2),end="")
      print("*")
'''


