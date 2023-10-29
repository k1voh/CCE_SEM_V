#make detailed tuples for each employee and store them in a list and print them


n = int(input("Enter number of employees : "))

Emp_Document = []

for i in range(n):
    Emp_Details = []
    Emp_Details.append((input("Enter ID of an Employee : ")))
    Emp_Details.append((input("Enter NAME of an Employee : ")))
    Emp_Details.append((input("Enter SALARY of an Employee : ")))
    Emp_Details.append((input("Enter DEPARTMENT of an Employee : ")))
    Emp_Document.append(tuple(Emp_Details))

srch_id = input("Enter the id to be searched for : ")
for i in Emp_Document:
    if i.index(srch_id) == 0:
        print(i)
