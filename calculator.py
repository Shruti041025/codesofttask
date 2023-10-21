print("Calculator For the basic aritmatic operation")
print("1:Addition")
print("2:Subtraction")
print("3:Multiplication")
print("4:Division")
print("5:Percentage")
operation = input()
if operation == "1":
    num1=input("enter the number 1\n")
    num2=input("enter the number 2\n")
    print("the addition are :"+ (str(int(num1)+int(num2))))
elif operation == "2":
     num1=input("enter the number 1\n")
     num2=input("enter the number 2\n")
     print("the subtraction are :"+ (str(int(num1)-int(num2))))
elif operation == "3":
     num1=input("enter the number 1\n")
     num2=input("enter the number 2\n")
     print("the multiplication are :"+ (str(int(num1)*int(num2))))
elif operation == "4":
    num1=input("enter the number 1\n")
    num2=input("enter the number 2\n"
    print("the division are :"+ (str(int(num1)/int(num2))))
else:
     print("invalid entry2")
    
