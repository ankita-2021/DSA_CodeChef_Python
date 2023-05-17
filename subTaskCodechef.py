

# t = int(input())
# for _ in range(t):
#   #take input
#   n, m, k = map(int, input().split())
#   arr = list(map(int, input().split()))
#   #check condition 1, are all correct?
#   c1 = False
#   ans = 0
#   for i in range(n):
#     if arr[i] == 1:
#       ans += 1
#   if ans == n:
#     c1 = True
#   #check condition 2, are first m correct?
#   c2 = False
#   ans = 0
#   for i in range(m):
#     if arr[i] == 1:
#       ans += 1
#   if ans == m:
#     c2 = True
  
#   if c1:
#     print(100)
#   elif c2:
#     print(k)
#   #if neither condition met, score is 0
#   else:
#     print(0)
        

# arr = list(map(int, input().split()))
# key=int(input())
# for i in arr:
#     if i==key:
#         print(arr.index(i))
#     else:
#         print("absent")
