def sorted1(arr):
    d=arr.copy()
    d.sort()
    return d

def gridChallenge(grid):
    # Write your code here
    result = "YES"
    list2 = []
    list4 = []
    for i in grid:
        list3 = []
        for j in i:
            list3.append(j)
        list3.sort()
        list2.append(list3)
    for i in range(0,len(list2[0])):
        list5=[]
        for j in range(0, len(list2)):
            list5.append(list2[j][i])
        list4.append(list5)
    for i in range(0,len(list2[0])):
        if list4[i]!=sorted1(list4[i]):
            result = "NO"
            break
        
    return result
