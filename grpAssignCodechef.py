# 
n=int(input())
for _ in range(n):
    count=0
    l,r=map(int,input().split())
    for i in range(l,r+1):
        res=i%10
        if res==2 or res==3 or res==9:
            count+=1
        elif i==2 or i==3 or i==3:
            count+=1
        else:
            count=count
    print(count)
            
