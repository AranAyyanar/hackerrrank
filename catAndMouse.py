def catAndMouse(x, y, z):
    if abs(x - z) == abs(y - z):
        return "Mouse C"
    elif abs(x - z) > abs(y - z):
        return "Cat B"
    else:
        return "Cat A"


n = int(input())
for i in range(0, n):
        list1 = list(map(int, input().split(" ")))
        x = list1[0]
        y = list1[1]
        z = list1[2]
        result = catAndMouse(x, y, z)
        print(result)
