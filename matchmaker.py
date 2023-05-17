# t=int(input())
# for _ in range(t):
#     n=int(input())
#     arr1=list(map(int,input().split()))
#     arr2=list(map(int,input().split()))
#     arr1.sort()
#     arr2.sort(reverse=True)
#     count=0
#     for i in range(n):
#         if arr1[i]%arr2[i]==0 or arr2[i]%arr1[i]==0:
#             count+=1
#     print(count)


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid-1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums)-1 and nums[mid+1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(nums)-1, condition)

def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)
# def locate_card(cards, query):
    
#     def condition(mid):
#         if cards[mid] == query:
#             if mid > 0 and cards[mid-1] == query:
#                 return 'left'
#             else:
#                 return 'found'
#         elif cards[mid] < query:
#             return 'left'
#         else:
#             return 'right'
    
#     return binary_search(0, len(cards) - 1, condition)
nums=list(map(int,input().split()))
target=int(input())
print(first_and_last_position(nums, target))