import sys

l1 = []
try:
    file = open(sys.argv[1],'r')
    otp = open(sys.argv[2],'w')
    l1 = file.readlines()[::-1]
    l1[0] = l1[0]+'\n'
    #print(l1)
    for lines in l1:
        otp.writelines(lines)
    file.close()
    otp.close()
except FileNotFoundError:
    print("File does not exist")
    
    
'''
python3 q3.py sample.txt output.txt
[['quiwgdiq'],['quiwgdiqwu']]
'''