arr=list(map(int,input().split()))
count=set()  
for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            count.add(i)
            count.add(i-1)
print(len(count))