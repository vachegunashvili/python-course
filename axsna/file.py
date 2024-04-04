number1=int(input("please eneter first number:"))

number2=int(input("please eneter second number:"))

if number1>number2 or number2<number1:
    print("first number is bigger then second number")
elif number1<number2 or number2>number1:
    print("number2 is bigger then number1")
elif number1==number2:
    print("first1 equals second2")