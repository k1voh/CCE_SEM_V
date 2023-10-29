

def main(parList):
        mult = set()
        for i in range(len(parList)):
            mult.add(parList[i])

        return mult
    

print(main.__code__.co_nlocals)