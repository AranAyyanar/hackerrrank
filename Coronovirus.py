def main():

    V=input()
    N=int(input())
    list1=[]
    list2=[]
    for i in range(0,N):
        B=input()
        list1.append(B)
    for i in V:
        list2.append(i)
    list3=[]
    for i in range(0,len(list1)):
        list4=[]
        for j in list1[i]:
            list4.append(j)
        if len(list2)>len(list4):
            list5 = [list2[k] for k in range(list2.index(list4[0]),len(list2))]
            T=""
            for j in list4:
                if j in list5:
                    T="POSITIVE"
                    list5 = list5[list5.index(j)+1:]
                else:
                    T="NEGATIVE"
                    break
            list3.append(T)
        else:
            list3.append("NEGATIVE")
    for i in list3:
        print(i)
        
                  
main()
