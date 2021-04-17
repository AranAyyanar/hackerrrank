def pageCount(n, p):
    count=0
    count1=0
    if n%2==0:
        n=n+1
    for i in range(1,n,2):
        if p>i:
            count=count+1
    for i in range(n-1,0,-2):
        if p<i:
            count1=count1+1
    if count1<count:
        return count1
    else:
        return count
n = 6
p = 2
result = pageCount(n, p)
print(result)
