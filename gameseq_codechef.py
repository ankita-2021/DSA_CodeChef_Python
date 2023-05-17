# t=int(input())
# for _ in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     count=0
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if (arr[i]+arr[j])%2==0:
#                 count
#     print(count)

# equalcardgame....
'''tc=int(input())
for _ in range(tc):
    n=int(input())
    rem=52%n
    print(rem)
'''
'''zoo problem'''
# s=str(input())
# count_z=0
# count_o=0
# for i in s:
#     if i=="z":
#         count_z+=1
#     elif i=="o":
#         count_o+=1
# if count_o==2*(count_z):
#     print("Yes")
# else:
#     print("No")


arr=list(map(int,input().split()))
res=[]
first=arr[:len(arr)//2]
for i in first:
    res.append(arr[i][0])
print(res)
second=arr[len(arr)//2:]
for j in second:
    rem2=j%10
    res.append(rem2)
nw= ''
for element in res:
    nw+=str(element)
    nw_num=int(nw)
if nw_num%11==0:
    print("OUT")
else:
    print("NON")

    
