num = float(input("enter the number"))
print("it is a number")
try:
    if num > 0:
        print("it is a positive number")
    else:
        print("it is a negative number")
    if num == 0:
        print("it is a zero")
except Exception as e:
    print(e)