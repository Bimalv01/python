arr=[11,17,19,23,18,16,21,2,11]
max1=[]
for i in range(3):
    m=max(arr)
    max1.append(m)
    arr.remove(m)
print(max1)
    
