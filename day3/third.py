file1 = open("./input.txt", "r")
arr = []
for j in file1:
    arr.append((j.replace("\n", "")))
i=0
curr = 3
treecount=0
length = len(arr[0])
while i<len(arr)-1:
    location = arr[i+1][curr%length]
    if location=="#":
       treecount+=1
    i+=1
    curr+=3
print(treecount)
