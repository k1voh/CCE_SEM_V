data={"Character":0,
      "Word": 0,
      "Lines": 0}
l1 = []
l2 = []
try:
    file = open('210953174_AP\Lab7_23-08-23\sample.txt','r')
    for line in file:
        l1.extend(line.strip("\n").split(" "))
        data["Lines"] += 1
        for i in line:
            if i != " ":
                data["Character"] += 1    
    file.close()
    data["Word"] = len(l1)
except FileNotFoundError:
    print("File does not exist") 
finally:
    print(data)