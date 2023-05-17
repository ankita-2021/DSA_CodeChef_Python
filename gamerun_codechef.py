# t= int(input())
# for _ in range(t):
#     n,k=map(int,input().split())
#     arr=list(map(int,input().split()))
#     i=0
#     maxx=-float('INF')
#     while i<n-k:
#         j=i
#         summ=0
#         while j<=i+k-1:
#             summ+=arr[j]
#             j+=1
#         if summ>maxx:
#             maxx=max(maxx,summ)
#         i+=1
#     print(maxx)
'''
t= int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    i=0
    mx=-float('INF')
    sm=0
    while i<k:
        sm+=arr[i]
        i+=1 
    mx=sm
    
    while i<n:
        sm+=arr[i]
        sm-=arr[i-k]
        if sm>mx:
            mx=sm
        i+=1 
    print(mx)'''

# t= int(input())
# for _ in range(t):
#     n=int(input())
'''for i in range(int(input())):
    n=int(input())
    s=input()
    r=input()
    nw_s=sorted(s)
    nw_r=sorted(r)
    S=''.join(nw_s)
    R=''.join(nw_r)
    if S==R:
        print("YES")
    else:
        print("NO")'''

l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
nw_l1=[]
nw_l2=[]
res=[]
for i in l1:
    if i not in l2:
        nw_l1.append(i)
for j in l2:
    if j not in l1:
        nw_l2.append(j)
res.append(nw_l1)
res.append(nw_l2)

# for item1 in nw_l1:
#     if item1 not in res:
#         res.append(item1)
# for item2 in nw_l2:
#     if item2 not in res:
#         res.append(item2)
print(res)





