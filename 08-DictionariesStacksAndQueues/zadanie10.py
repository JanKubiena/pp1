arr = [
    {
        "population" : "38M",
        "country" : "poland"
    },
    {
        "population" : "80M",
        "country" : "germany"
    },
    {
        "population" : "500M",
        "country" : "usa"
    },
    {
        "population" : "1,2mld",
        "country" : "china"
    },
    {
        "population" : "50k",
        "country" : "monaco"
    }
]

i = 0
while(i < len(arr)):
    for k,v in arr[i].items():
        print(v," ",end="")
    print()
    i+=1  
 
 