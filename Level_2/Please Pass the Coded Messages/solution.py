from itertools import permutations

def Sol(l):
    res=[]
    for i in range(0,len(l)):
        p=permutations(l,len(l)-i)
        for j in p:
            s=""
            for k in j:
                s=s+str(k)
            res.append(int(s))
    res.sort(reverse=True)
    for i in res:
        flag=0
        if(i%3==0):
            return i
            flag=1
            break
    if(flag==0):
        return 0
        
l=[1,3,1,4]
print(Sol(l))
