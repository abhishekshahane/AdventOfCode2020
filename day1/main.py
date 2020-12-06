file1 = open("./input.txt", "r")
arr = []
for x in file1:
    arr.append(int(x.replace("\n", "")))
#day 1 complete
#1
for x in range(len(arr)):
    for j in range(x+1, len(arr)):
        if arr[x]+arr[j]==2020:
            print(arr[x]*arr[j])
#2
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for x in range(j+1, len(arr)):
            if arr[i]+arr[j]+arr[x]==2020:
                print(arr[x]*arr[i]*arr[j])
