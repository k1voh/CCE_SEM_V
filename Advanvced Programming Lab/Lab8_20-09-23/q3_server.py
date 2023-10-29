import socket

def palindrome(word):
    return(word[0::] == word[::-1])


def count_vowel(word):
    d = {'a' : 0, 'e': 0, 'i': 0, 'o': 0, 'u':0}
    for i in word:
        if i in d:
            d[i] += 1
            
    return d



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 12345
    s.bind((host,port))

    s.listen(5)

    while True:
        c, addr = s.accept()
        print("Got connection from : ", addr)
        c.send("Send a word(in Lowercase) : ".encode())
        word = c.recv(1024).decode().strip('b\'')
        c.send(str(palindrome(word)).encode())
        c.send(str(count_vowel(word)).encode())
        c.close()

if __name__ == '__main__':
    main()

