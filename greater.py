num = input("enter the number")
num_int = int(num)
print(type(num_int))
try:
    if num_int > 100:
        print("it is error")
    else:
        print("it is not error")
except Exception as e:
    print(e)