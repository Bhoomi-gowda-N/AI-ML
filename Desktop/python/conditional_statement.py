#Conditional statement means making decisions in code based on certain conditions.
age=18
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

#Nested if statement
num=int(input("enter a number:"))
if num>=0:
    if num==0:
        print("the number is zero")
    else:
        print("the number is positive")
else:
    print("the number is negative")

#elif statement it is used to check multiple conditions
marks=int(input("enter your marks:"))
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")
elif marks>=70:
    print("grade C")
elif marks>=60:
    print("grade D")
else:
    print("grade F")

#example of logical operators with conditional statements
#and operator executes when both conditons are true
#or operator executes when at least one condition is true
#not operator reverse the condition
num=int(input("enter a num:"))
if num>0 and num%2==0:
    print("the num is positive even")
elif num>0 and num%2!=0:
    print("the num is positive odd")
elif num<0 and num%2==0:
    print("the num is negative even")
else:
    print("the num is negative odd")



    