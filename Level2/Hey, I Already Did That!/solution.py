#Method to convert a number in base 10 to any base
def decimal_to_base(n, b):         
    if n == 0:
        return 0
    d = []
    while n:
        d.append(int(n % b))
        n /= b
    return ''.join(map(str,d[::-1]))

#Method to subtract 2 numbers which are in base 10 or in any other base.
def subtraction(x,y,b):
    if(b==10):
        z_int=int(x)-int(y)
        return int(z_int)
    else:
        x_dec = int(x, b)
        y_dec = int(y, b)
        z_int = decimal_to_base(x_dec - y_dec, b)
        return int(z_int)

#The Algorithm which generates the minion ID.
def algo(s,b):
    num=[]
    k=len(s)
    for i in s:
        num.append(i)
    asc_num=[]
    for i in num:
        asc_num.append(i)
    asc_num.sort()
    dsc_num=[]
    for i in num:
        dsc_num.append(i)
    dsc_num.sort(reverse=True)
    s_asc=""
    s_dsc=""
    for i in asc_num:
        s_asc+=str(i)
    for i in dsc_num:
        s_dsc+=str(i)
    z_int=subtraction(s_dsc,s_asc,b)
    if(len(str(z_int))<k):
        v=""
        for j in range(k-len(str(z_int))):
            v=v+"0"
        z=v+str(z_int)
    else:
        z=str(z_int)
    return z

#Detection of the Cycle and calculation of its length.

def solution(s,b):
    lr=[s]
    e=set([])
    check=""
    while True:
        if(s!=algo(s,b)):
            s=algo(s,b)
            if s in lr:
                if s not in e:
                    e.add(s)
                elif s in e:
                    return len(e)
            elif s not in lr:
                lr.append(s)
        else:
            return 1
    

s=input()
b=int(input())
print(solution(s,b))
