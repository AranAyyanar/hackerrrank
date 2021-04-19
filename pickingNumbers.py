def pickingNumbers(a):
    list1=[]
    for i in range(0, len(a)):
        list2=[]
        list2.append(a[i])
        for j in range(i+1,len(a)):
            if abs(a[i]-a[j]==0) or abs(a[i]-a[j])==1:
                list2.append(a[j])
        if len(list2)>1:
            list1.append(list2)
    list2=[]
    for i in range(0,len(list1)):
        list2.append(len(list1[i]))
    main_1=list2.index(max(list2))
    list4=list1[main_1]
    k=""
    for i in range(0, len(list4)-1):
        if abs(list4[i]-list4[i+1])>1:
            k=list4[i]
            break
    list6=[]
    for i in list4:
        if i!=k:
            list6.append(i)
    return len(list6)
    
k=list(map(int,input().split(" ")))
a=[]
for j in k:
    a.append(int(j))

result = pickingNumbers(a)
print(result)
