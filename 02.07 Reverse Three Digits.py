Number=int(input("enter a number: "))
OnesD= Number%10
Number= Number//10
TensD= Number%10
Hundigit= Number // 10
NewN= (OnesD * 100) + (TensD * 10) + Hundigit 
print("Reverse of Digits: ",NewN)