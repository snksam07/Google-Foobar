def adder(lu):
    su=0
    for i in lu:
        su+=i
    return su

def solution(l,k):
    flag=0
    for i in range(0,len(l)+1):
        for j in range(i+1,len(l)+i):
            if(adder(l[i:j])==k):
                flag=1
                return [i,j-1]
    if(flag==0):
        return [-1,-1]
    
               
               

l=list(map(int,input().split(',')))
k=int(input())
print(solution(l,k))
