

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
        

def findPair(nums, target):
 
    # consider each element except the last
    for i in range(len(nums) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):
 
            # if the desired sum is found, print it
            if nums[i] + nums[j] == target:
                print('Pair found', (nums[i], nums[j]))
                return
 
    # No pair with the given sum exists in the list
    print('Pair not found')

nums=list(map(int,input().split()))
target=int(input())
print(findPair(nums, target))
    