"""create a text file with minimum 10 lines
read the lines
store the data in a dictionary with string as a key and occurence of the key as the value"""

data={}
l1 = []
try:
    file = open('D:\\210953174_AP\\program_check\\sample.txt','r')
    for line in file:
        l1.extend(line.strip("\n").split(" "))
    file.close()
    for i in l1:
        if i in data:
            data[i] = data[i]+1
        else:
            data[i] = 1
except FileNotFoundError:
    print("File does not exist") 
finally:
    print(data)