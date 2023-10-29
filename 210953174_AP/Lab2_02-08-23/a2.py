lst1 = []
lst2 = []

for i in range(int(input("Enter size of lst1: "))):
    lst1.append(int(input("Enter Number: ")))
    
for i in range(int(input("Enter size of lst2: "))):
    lst2.append(int(input("Enter Number: ")))
    
print("Union: ", list(set(lst1+lst2)))

########################################
lst3 = []

for i in lst1:
    if (i in lst2) and (i not in lst3):
        lst3.append(i)

print("Intersection: ", lst3)
########################################
lst4 = []

for i in lst1:
    if i not in lst2:
        lst4.append(i)

print("Difference: ", lst4)


