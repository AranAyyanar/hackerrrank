def sockMerchant(n, ar):
    list2=[i for i in ar]
    count=0
    for i in list2:
        list1=[list2[j] for j in range(list2.index(i)+1,len(list2))]
        for j in list1:
            if i!="":
                if i==j:
                    count=count+1
                    list2[list2.index(i,(list2.index(i))+1)]=""
                    list2[list2.index(i)]=""
                    break
    return count
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = sockMerchant(n, ar)
print(result)
