num1 = float(input("enter the number1"))
num2 = float(input("enter the number2"))
num3 = float(input("enter the number3"))
if num1 >= num2 and num1 >= num3:
    print("num1 is largest")
elif num2 >= num1 and num2 >= num3:
    print("num2 is largest")
else:
    print("num3 is larget")