Number= int(input("Enter a number: "))
Number2= int(input("Enter a number: "))
TensD1= Number//10
TensD2= Number2//10
UnitsD1= Number%10
UnitsD2= Number2%10
NewN= (TensD1 * 1000) + (TensD2 * 100) + (UnitsD1 * 10) + UnitsD2
print("Merged Number: ",NewN)