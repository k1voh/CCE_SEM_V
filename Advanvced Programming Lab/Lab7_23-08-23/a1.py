try:
    file = open('E:\\Language\\210953174_AP\\Lab7_23-08-23\\sample.txt','r')
    for line in file:
        print(line[::-1])
except FileNotFoundError:
    print("File does not exist") 
