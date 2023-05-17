def keepmult(original,nums):
    while(True):
        if original in nums:
            original*=2
        else:
            return original
nums=list(map(int,input().split()))
original=int(input())
print(keepmult(original, nums))