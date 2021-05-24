s="ashley"
t="ash"
k=6
count=0
list1=[]
list2=[]
for i in s:
   list1.append(i)
for j in t:
   list2.append(j)
list3=list2.copy()
if len(list1)>len(list2):
    list2.append("")
else:
    list2.append("")
f=len(list1)
l=0
for i in range(0,len(list2)):
   if list1[i]!=list2[i]:
       l=i
       break
for i in range(l,f):
    list1.pop()
    count=count+1
for j in range(l,len(list3)):
    list1.append(list2[j])
    count=count+1
print(count)
