C1=int(input("How many students are in this classroom 1: "));
C2=int(input("How many students are in this classroom 2: "));
C3=int(input("How many students are in this classroom 3: "));
fulldesks1 = C1 // 2
partialdesk1 = C1 % 2   
fulldesks2 = C2 // 2
partialdesk2 = C2 % 2
fulldesks3 = C3 // 2
partialdesk3 = C3 % 2
total= fulldesks1+fulldesks2+fulldesks3+partialdesk1+partialdesk2+partialdesk3
print(total)