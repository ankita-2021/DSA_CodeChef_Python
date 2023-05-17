'''n=int(input())
for _ in range(n):
    temp=int(input())
    frwd_count=0
    bckwrd_count=0
    for i in range(1,temp+1):
        if i%2!=0:
            frwd_count+=3
        else:
            bckwrd_count+=1
    print(frwd_count-bckwrd_count)'''

# n=int(input())
# for _ in range(n):
#     x1,x2,x3,v1,v2=map(int,input().split())
#     chef_dist=abs(x3-x1)
#     kefa_dist=abs(x3-x2)
#     chef_time=chef_dist/v1
#     kefa_time=kefa_dist/v2
#     if kefa_time<chef_time:
#         print("Kefa")
#     elif chef_time<kefa_time:
#         print("Chef")
#     else:
#         print("Draw")

'''n=int(input())
for _ in range(n):
    x,y,z=map(int,input().split())
    if (x+y)<z:
        print("Yes")
    else:
        print("No")'''
# n=int(input())
# for _ in range(n):
#     arr=map(int,input().split())
#     pos=0
#     neg=0
#     zero=0
#     for i in arr:
#         if i>0:
#             pos+=1
#         elif i<0:
#             neg+=1
#         elif i==0:
#             zero+=1
#     pos_count=pos/n 
#     neg_count=neg/n 
#     zero_count=zero/n
#     print(pos_count,)
#     print(neg_count,)
#     print(zero_count,)


'''tc=int(input())
for _ in range(tc):
    n=[int(x) for x in input().split()]
    arr=n=[int(x) for x in input().split()]
    l=len(arr)
    get_sum=sum(arr)
    mean=get_sum//n
    nw_arr=arr.sort()
    if l%2==0:
        med1=nw_arr[l//2]
        med2=nw_arr[l//2-1]
        median=(med1+med2)/2
    else:
        median=nw_arr[l//2]
    print(mean, meadian)'''
'''n=int(input())
d=n//7
rem=n%7
print(rem)'''
