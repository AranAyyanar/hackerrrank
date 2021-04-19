def getMoneySpent(keyboards, drives, b):
    list1=[]
    for i in range(len(keyboards)-1,-1,-1):
        if keyboards[i]<b:
            for j in range(len(drives)-1,-1,-1):
                if keyboards[i]+drives[j]<=b:
                    result=keyboards[i]+drives[j]
                    list1.append(result)
    if len(list1)==0:
        return -1
    else:
        return max(list1)
 keyboards=[40,50,60]
 drives=[5,8,12]
 b=60
        
 result = getMoneySpent(keyboards, drives, b)
 print(result)
