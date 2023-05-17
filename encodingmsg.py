# Chef recently graduated Computer Science in university, so he was looking for a job. He applied for several job offers, but he eventually settled for a software engineering job at ShareChat. Chef was very enthusiastic about his new job and the first mission assigned to him was to implement a message encoding feature to ensure the chat is private and secure.

# Chef has a message, which is a string S with length N containing only lowercase English letters. It should be encoded in two steps as follows:

# Swap the first and second character of the string S, then swap the 3rd and 4th character, then the 5th and 6th character and so on. If the length of S is odd, the last character should not be swapped with any other.
# Replace each occurrence of the letter 'a' in the message obtained after the first step by the letter 'z', each occurrence of 'b' by 'y', each occurrence of 'c' by 'x', etc, and each occurrence of 'z' in the message obtained after the first step by 'a'.
# The string produced in the second step is the encoded message. Help Chef and find this message.

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains a single integer N.
# The second line contains the message string S.
# Output
# For each test case, print a single line containing one string — the encoded message.

'''input
2
9
sharechat
4
chef

output
shizxvzsg
sxuv'''

for i in range(int(input())):
    n=int(input())
    x=list(input())
    b=''
    if(n%2!=0):
        n-=1
    for i in range(0,n,2):
            x[i],x[i+1]=x[i+1],x[i]
    x=''.join(x)
    for i in range(0,len(x)):
        a=ord(x[i])
        b=b+chr(219-a)
    print(b) 