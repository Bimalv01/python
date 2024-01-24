r=int(input("enter: "))
def area():
    pie=3.14
    a=pie*r*r
    return a
def cercum():
    pie=3.14
    cer=2*pie*r
    print(cer)
cercum()

print(area())


l=[5,2,8,1,6,9,3]
t=[]
for i in l:
    if i%2==0:
        print(i)
        t.append(i)
print(sum(t))

s=["apple","banana","cherry","date","elder berry"]

a=[]
for i in s:
    li=len(i)
    a.append(li)
x=a.index(max(a))
print(s[x])


l=[]
for i in range(1,5):
    p=int(input(f"enter {i} "))
    l.append(p)

print(max(l))    


        
