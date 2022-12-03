f = open("countries.txt",'r',encoding="utf-8" )
myline = f.readline()
while myline:
     print(myline)
     myline = f.readline()
f.close()
