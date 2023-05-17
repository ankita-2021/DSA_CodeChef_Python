'''Chef has bought a new robot, which will be used for delivering dishes to his customers. 
He started testing the robot by letting it move on a line.

Initially, the robot is placed at the coordinate x=X. 
Then, it should execute a sequence of N commands, described by a string S with length N. 
Each character of this string is either 'L' or 'R', denoting that the robot should walk one step to the left (decreasing x by 1) or to the right (increasing x by 1), respectively.

How many distinct points are visited by the robot when it has executed all the commands? 
A point p is visited by the robot if p is an integer and the robot's position before or after executing some command is x=p.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and X.'''
# input
# 2
# 6 10
# RRLLLL
# 2 0
# LL
# # output
# 5
# 3



for i in range(int(input())):
    n,x=map(int, input().split())
    s=input()
    res=[]
    res.append(x)
    for i in s:
        if i=="R":
            x+=1
            res.append(x)
        elif i=="L":
            x-=1
            res.append(x)
    count=0
    l1=[]
    for item in res:
        if item not in l1:
            count+=1
            l1.append(item)
    print(count)
    