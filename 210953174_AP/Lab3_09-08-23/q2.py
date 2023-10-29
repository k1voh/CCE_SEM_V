

def main(parList):
        return list(set(parList))
    

N = int(input("enter the number of elements : "))
parList = []
for i in range(N):
    parList.append(int(input("enter a number for list :")))
print(main(parList))