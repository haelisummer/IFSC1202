Lenght= int(input("enter how long the race is in kilometers: "))
Minutes= int(input("enter how many minutes are needed to complete race: "))
Seconds= int(input("enter how many seconds are needed to complete race: "))
Mph= (Lenght / 1.61) / ((Minutes / 60) + (Seconds / 3600))
print(Mph)

