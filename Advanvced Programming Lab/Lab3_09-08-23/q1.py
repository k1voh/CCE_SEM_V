
def main(parList):
        mult = 1
        for i in range(len(parList)):
            mult = mult * parList[i]

        return mult
    

N = int(input("enter the number of elements : "))
parList = []
for i in range(N):
    parList.append(int(input("enter a number for list :")))
print(main(parList))