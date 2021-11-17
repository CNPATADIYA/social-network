s='1'
def fun(n):
    if n%2==0:
        print(s*int(n/2))
    else :
        print('7'+s*int((n-3)/2))

n=int(input())
for i in range(0,n):
        m=int(input())
        fun(m)