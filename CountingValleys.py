def countingValleys(steps, path):
    count=0
    out=0
    for i in path:
        if i == "U":
            count=count+1
        elif i == "D":
            count=count-1
        if count==0 and i=="U":
            out=out+1
    return out




path = "UDDDUDUU"
steps=8

count=countingValleys(steps, path)
print(count)
