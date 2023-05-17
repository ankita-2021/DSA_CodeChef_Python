# # n=int(input())
# # for _ in range(n):
# #     a,b=map(int,input().split())
# #     c=21-(a+b)
# #     if c>=1 and c<=10:
# #         print(c)
# #     else:
# #         print(-1)

# # n=int(input())
# # for _ in range(n):
# #     x1,y1,x2,y2=map(int,input().split())
# #     dist= max(abs(x1-x2),abs(y1-y2))
# #     print(di
# '''tc=int(input())
# for _ in range(tc):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     count=0
#     for i in arr:
#         if i>=10 and i<=60:
#             count+=1
#     print(count)'''

# # tc=int(input())
# # for _ in range(tc):
# #     a,b,c,d=map(int,input().split())
# #     if a+c==180 or b+d==180:
# #         print("Yes")
# #     else:
# #         print("No")
# '''tc=int(input())
# for _ in range(tc):
#     temp=int(input())
#     if temp%10==0:
#         bag=int(temp/10)
#         print(bag)
#     else:
#         print((temp//10)+1)'''

# # t=int(input())
# # if t%2==0:
# #     cell=t//2
# #     black_cell=t*cell
# #     print(black_cell)
# # n=int(input())
# # for _ in range(n):
# # 	s,t=map(str,input().split())
# # 	nw_s=sorted(s)
# # 	nw_t=sorted(t)
# # 	if nw_s==nw_t:
# # 		print(True)
# # 	else:
# # 		print(False)



# ''''def insertIn(n,x,arr):
#     if x<=arr[0]:
#         return [x]+arr
#     elif x>=arr[-1]:
#         return arr+[x]
#     for i in range(1,n):
#         if x<=arr[i]:
#             left=arr[:i]
#             right=arr[i:]
#             return left+[x]+right

# tc=int(input())
# for _ in range(tc):
#     n,x=[int(x) for x in input().split()]
#     arr=[int(x) for x in input().split()]
#     print(insertIn(n, x, arr)) '''


# # let Input = document.querySelector('input');
# # let btn = document.querySelector('button');
# # let content = document.querySelector('.todos');
# # let count =-1
# # btn.addEventListener('click',function(){
# #     count +=1;
# #     let inputcontent =document.createElement('p');
# #     inputcontent.innerHTML= Input.value
# #     inputcontent.setAttribute("key",count);
# #     content.appendChild(inputcontent);

# #     inputcontent.addEventListener('click',function(){
# #         content.removeChild(inputcontent);
# #     })
# # })
# # 
# '''n=int(input())
# for i in range(n):
#     x=int(input())
#     count=0
#     for j in range(x):
#         if x%10==4:
#             count+=1
#         x=x//10
#     print(count)'''
# # n=int(input())
# # for _ in range(n):
# #     x,y,z=map(int,input().split())
# #     if (x+(z*2))>=y:
# #         print("Yes")
# #     else:
# #         print("No")
# '''n=int(input())
# for _ in range(n):
#     x,m,d=map(int,input().split())
#     time_take=x*m
#     delay=x+d
#     minn_delay=min(time_take,delay)
#     print(minn_delay)'''

# # n=int(input())
# # for _ in range(n):
# #     Sa,Sb,Sc=map(int,input().split())
# #     if Sa<Sb and Sa<Sc:
# #         hardest=Sa
# #         print("Draw")
# #     elif Sb<Sa and Sb<Sc:
# #         hardest=Sb
# #         print("Bob")
# #     else:
# #         hardest=Sc
# #         print("Alice")

#     # print(summ)
# '''n=int(input())
# for _ in range(n):
#     s=input()
#     t=input()
#     for i in range(len(s)):
#         if s[i]==t[i]:
#             print("G",end="")
#         else:
#             print("B",end="")
#     print()'''
# # string palindrom
# str_name=input()
# # for iterate hoga 0 se len/2 yani ki half tk
# for i in range(0,int(len(str_name)/2)):
#     # if my str_name[i] first half wala agr last index udhr equal nhi hua to false...
#     if str_name[i]!=str_name[len(str_name)-i-1]: 
#         print(False)
#         break
# else:
#     print(True)

# str_name=input()
# s=str_name.split()
# if 'R' in s:
#     print("R")
# elif 'B' in s:
#     print("B")
# else:
#     print("G")
# s,p= input().split()
# if s=="R" or p=="R":
#     print("R")
# elif s==p:
#     print(s)
# elif s=="B" or p=="B":
#     print("B")
'''n=int(input())
for _ in range(n):
    arr=map(int,input().split())
    summ=0
    for i in arr:
        summ=summ+i
    print(summ)'''
# n=int(input())
# for _ in range(n):
#     arr=list(map(int,input().split()))
#     count_1=0
#     count_0=0
#     for i in range(len(arr)):
#         # arr k har k index mein ye check krna ki hr ek index m kitne 1's hain isliye arr[i]
#         if arr[i]==1: 
#             count_1+=1
#         else:
#             count_0+=1
#     if count_1>count_0:
#         print("Yes")
#     else:
#         print("No")
'''n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    if a==0:
        print("Liquid")
    elif b==0:
        print("Solid")
    else:
        print("Solution")'''
# n=int(input())
# for _ in range(n):
#     a,b,c,d = list(map(int,input().split()))
#     A=c//a
#     B=d//b
#     coco=A+B
#     print(coco)

    