Number=int(input("Enter a 4-digit number: "))
OnesD= Number%10
Number= Number//10
TensD= Number%10
Number = Number // 10
Hundigit= Number % 10
ThousD= Number // 10


if Hundigit == TensD and OnesD == ThousD:
    print("YES")
else:
    print("NO")
