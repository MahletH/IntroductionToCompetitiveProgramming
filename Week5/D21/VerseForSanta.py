'''
This is an answer for contest problem on 'https://codeforces.com/contest/1279/problem/B'
'''
test=eval(input())
numLst=[]
vers=[]
for i in range(test):
    ver=input()
    lst=input()
    nums=lst.split(" ")
    vLst=ver.split(" ")
    skpd,ski=0,0
    v=int(vLst[1])
    j,ctr=0,0
    while(v>=0 and j<len(nums)):
        if(int(nums[j])>skpd):
            if(v-skpd>=0):
                v-=skpd
                ctr=1
                skpd,ski=int(nums[j]),j+1
        else:
            if(v-int(nums[j])<0):
                break;
            v-=int(nums[j])
        j+=1
    if(j==len(nums) and v>=0 ):
        if(v-skpd>=0):
            ski=0;
    print(ski)
          
