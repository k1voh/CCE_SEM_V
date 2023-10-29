
word = input("Enter a sentence : ")

count_Upper = 0
count_Lower = 0

for i in word:
    if i.isupper():
        count_Upper = count_Upper + 1
    else:
        count_Lower = count_Lower + 1
        
print(count_Upper, count_Lower)