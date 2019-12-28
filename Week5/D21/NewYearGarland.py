'''
This is the answer for contest problem on 'https://codeforces.com/contest/1279/problem/A'
'''
test=eval(input())
for i in range(test):
    lst=input()
    nums=lst.split(" ")
    r=int(nums[0])
    g=int(nums[1])
    b=int(nums[2])
    if(r<=g+b+1 and g<=r+b+1 and b<=g+r+1):
        print("Yes")
    else:
        print("No")
