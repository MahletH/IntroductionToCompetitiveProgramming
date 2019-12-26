import random as r
random_list=[]
for i in range(10000+1):
    random_list.append(i)
for j in range(10000-1):
    k=r.randint(j+1,10000)
    random_list[j],random_list[k]=random_list[k],random_list[j]

print(random_list)

    
