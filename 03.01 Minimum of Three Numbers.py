Num1=int(input("Enter a number: "))
Num2=int(input("Enter a number: "))
Num3=int(input("Enter a number: "))

if Num1 <= Num2 and Num1 <= Num3:
    print(Num1)
elif Num2 <= Num3 and Num2 <= Num1:
    print(Num2)
else:
    print(Num3)
