import socket

def search(nums, key):
    for i in nums:
        if i == key:
            return True
    return False


def sort(nums):
    return sorted(nums)

def split(nums):
    odd = []
    even = []
    
    for i in nums:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
            
    return odd,even


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    s.bind((host,port))

    s.listen(5)

    while True:
        c, addr = s.accept()
        print("Got connection from : ", addr)
        c.send("Send an Integer array : ".encode())
        arr = c.recv(1024).decode().strip('b\'[]').split(",")
        arr = [int(x) for x in arr]
        while True:
            buff = c.recv(1024).decode().strip('b\'[]').split(",")
            buff = [int(x) for x in buff]
            option = buff[0]
            if option == 1:
                key = buff[1]
                c.send(str(search(arr,key)).encode())
            elif option == 2:
                c.send(str(sort(arr)).encode())
            elif option == 3:
                odd,even = split(arr)
                c.send(str(odd).encode())
                c.send(str(even).encode())
            elif option == 4:
                c.close()
                s.close()
                exit()
if __name__ == '__main__':
    main()

