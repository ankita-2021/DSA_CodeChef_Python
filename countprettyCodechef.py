# Vasya likes the number 239. Therefore, 
# he considers a number pretty if its last digit is 2, 3 or 9.

# Vasya wants to watch the numbers between L and R (both inclusive), 
# so he asked you to determine how many pretty numbers are in this range. Can you help him?

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains two space-separated integers L and R.
# Output
# For each test case, print a single line containing one integer — the number of pretty numbers between L and R.

# Constraints
# 1≤T≤100
# 1≤L≤R≤105


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

            
