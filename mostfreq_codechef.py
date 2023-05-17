# mostfreq codechef
tc=int(input())
for _ in range(tc):
    n=int(input())
    arr=list(map(int,input().split()))
    res={}
    for item in arr:
        if item not in res:
            res[item]=1
        else:
            res[item]+=1
            
    d1={}
    for v in d1.values():
        if v not in d1:
            d1[i]=1 
        else:
            d1[i]+=1
    key=None
    val=0
    for k,v in d1.items():
        if key==None:
            key=k
            val=v 
        elif v>val:
            val=v 
            key=k 
        elif v==val:
            key=min(key,k)
    print(key)