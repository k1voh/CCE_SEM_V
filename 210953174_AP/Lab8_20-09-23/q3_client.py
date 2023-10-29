import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345

s.connect((host,port))

print(s.recv(1024).decode().strip('b\''))

word = input()
s.send(word.encode())

print("Is it a palindrome : ",s.recv(1024).decode().strip('b\''))

print("Vowel count is : ",s.recv(1024).decode().strip('b\''))
s.recv
s.close()