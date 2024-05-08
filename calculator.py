print("****SIMPLE MINI CALCULATOR*****")

#user input 
num1 =float(input("Enter the first number:"))
num2 =float(input("Enter the second number:"))

#choices for user input
print("press 1 for Addition \npress 2 for Subtraction \npress 3 for Multiplication \npress 4 for Divison")
choice =int(input("Enter your choice from 1-4: "))

# conditional statements for basic arithmetic operations
if choice ==1:
    result=num1+num2
    print(round(result,4))
elif choice==2:
    result=num1-num2
    print(round(result,4))
elif choice==3:
    result=num1*num2
    print(round(result,4))
elif choice==4:
    result=num1/num2
    print(round(result,4))
else:
    print("YOU ENTERED AN INVALID INPUT")
    