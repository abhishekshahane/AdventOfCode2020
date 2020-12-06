#from math import floor
file1 = open("./input.txt", "r")
arr = []

for j in file1:
    arr.append(j.replace("\n", ""))
def solve(arr, a, b):
    i=0
    curr = b
    treecount=0
    length = len(arr[0])
    while i<len(arr)-1:
        location = arr[i+a][curr%length]
        if location=="#":
            treecount+=1
        i+=a
        curr+=b
    return treecount
print(solve(arr, 2, 1)*solve(arr,1,1)*solve(arr,1,3)*solve(arr,1,5)*solve(arr,1,7))
