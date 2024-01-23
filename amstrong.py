for i in range(1,1001):
    string=str(i)
    digit=len(string)
    sum1=0
    for j in string:
        sum1+=int(j)**digit
        if i==sum1:
            print(i)






    
