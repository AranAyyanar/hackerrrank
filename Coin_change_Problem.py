def getWays(n, c):
    # Write your code here
    count = 0
    a = [[ 0 for i in range(0,n+1)] for x in range(0, len(c))]
    for i in range(0,len(c)):
        a[i][0]=1
    for i in range(0, len(c)):
        for j in range(0,n+1):
            if c[i]>j:
                a[i][j]=a[i-1][j]
            else:
                if i == 0 and j!=0:
                   if j%c[i] == 0:
                        a[i][j]=1
                else:
                    a[i][j]=a[i-1][j]+a[i][j-c[i]]
    return a[-1][-1]
  
  n=3
  c=[1,2,3]
  d = getways(n, c)
    
