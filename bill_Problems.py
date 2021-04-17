def bonAppetit(bill, k, b):
    T="Bon Appetit"
    sum1=0
    for i in bill:
        if i!=bill[k]:
            sum1=sum1+i
    q=sum1//2
    l=b-q
    if l!=0:
        print(l)
    else:
        print(T)


nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
bonAppetit(bill, k ,b)
