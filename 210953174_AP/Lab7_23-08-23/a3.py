import sys

try:
    file = open(sys.argv[1],'r')
    otp = open("otp.txt",'w')
    wrap = int(sys.argv[2])
    
    sentences = file.readlines()
    
    sentences = [word for x in sentences for word in [x[:wrap:]+"\n",x[wrap::]]]
    
    otp.writelines(sentences)

except FileNotFoundError:
    pass

'''
INPUT
-----
hello i am shouvik
shome from south delhi
-----

OUTPUT
------
hello i am
shouvik
shome fro
m south 
delhi
-------
'''