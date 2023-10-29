import re

try:
    v_mail = open('D:\\210953174_AP\\Lab7_23-08-23\\valid_mail.txt','w')
    inv_mail = open('D:\\210953174_AP\\Lab7_23-08-23\\invalid_mail.txt','w')
    input = open('D:\\210953174_AP\\Lab7_23-08-23\\input.txt','r')

    for line in input:
        if re.match('/^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$',line) is not None:
            v_mail.write(line)
        else:
            inv_mail.write(line)
except FileNotFoundError:
    print("File does not exist") 