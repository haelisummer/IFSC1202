PointA=int(input("Enter Point A: "))
PointB=int(input("Enter Point B: "))
PointC=int(input("Enter Point C: "))

AB= PointA - PointB
AC= PointA - PointC
if AB > AC:
    print(AB * -1)
elif AC > AB:
    print(AC * -1)