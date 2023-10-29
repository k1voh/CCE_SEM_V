
data={}
l1 = []
try:
    file = open('210953174_AP\Lab7_23-08-23\sample.txt','r')
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
    
'''
append = [1,2,[1,2]]
extend = [1,2,1,2]
'''