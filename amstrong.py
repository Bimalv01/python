for i in range(1,1001):
    string=str(i)
    digit=len(string)
    sum1=0
    for j in string:
        sum1+=int(j)**digit
        if i==sum1:
            print(i)

n=5
f=1
for i in range(n):
    f*=n
    n-=1
print(f)

for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)

a=0
b=1
for i in range(10):
    c=a+b
    a=b
    b=c
    print(c)
    
def loan(a,m,r):
    r=r*a
    s1=1-(1+r)**-m
    s3=r/s1
    return s3
def tot():
    a=int(input("enter amount: "))
    m=int(input("enter month: "))
    r=float(input("enter amount: "))
    total=loan(a,m,r)
    print(f"{total:.2f}")
tot()

n=5
for i in range(1,n):
    print(" "*(n-i),"*"*(2*i-1))

for j in range(1,10):
    for k in range(1,j):
        print(j,end="")
    print()
    

a=int(input("enter"))
b=float(input("enter"))
c=int(input("enter"))

eq=b**2-4*a*c
root1=(-b+(eq**0.5))/2*a
root2=(-b-(eq**0.5))/(2*a)
print(root1)
print(root2)





    
