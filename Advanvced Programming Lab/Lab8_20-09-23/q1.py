import re

names = []

for name in dir(re):
    if 'find' in name:
        names.append(name)
        
names.sort()
print(names)