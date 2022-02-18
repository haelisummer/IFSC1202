Number=int(input("enter a number: "))
OnesD= Number%10
Number= Number//10
TensD= Number%10
Hundigit= Number // 10
print("Sum of Digits: ",OnesD+TensD+Hundigit)