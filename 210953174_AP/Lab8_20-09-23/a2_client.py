import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.connect((host,port))

arr = []
nums = int(input("Enter the number of elements : "))
print(s.recv(1024).decode().strip('b\''))
for i in range(nums):
    arr.append(int(input("Enter number : ")))
s.send(str(arr).encode())
while True:
    print("What would you like to do?(1:search|2:sort|3:split|4:exit) : ")
    opt = int(input())
    if opt == 1:
        key = int(input("What would you like to search for : "))
        buff = [opt,key]
        s.send(str(buff).encode())
        print(s.recv(1024).decode().strip('b\''))
    elif opt == 2:
        buff = [opt]
        s.send(str(buff).encode())
        print(s.recv(1024).decode().strip('b\''))
    elif opt == 3:
        buff = [opt]
        s.send(str(buff).encode())
        print(s.recv(1024).decode().strip('b\''))
        print(s.recv(1024).decode().strip('b\''))
    elif opt == 4:
        buff = [opt]
        s.send(str(buff).encode())
        s.close()
        exit()
