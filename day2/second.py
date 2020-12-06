file1 = open("./input.txt", "r")
arr = []
for j in file1:
    arr.append((j.replace("\n", "")))
#1
valid_counts = 0
v_c=0
for j in range(len(arr)):
    arr[j] = arr[j].split(" ")
    arr[j][0] = arr[j][0].split("-")
    arr[j][1] = arr[j][1].replace(":", "")
    f = int(arr[j][0][0])-1
    s = int(arr[j][0][1])-1
    letter = arr[j][1]
    count = arr[j][2].count(arr[j][1])
    if count>=int(arr[j][0][0]) and count<=int(arr[j][0][1]):
        valid_counts+=1
    if arr[j][2][f]==letter and arr[j][2][s]!=letter or arr[j][2][f]!=letter and arr[j][2][s]==letter:
        v_c+=1
print(valid_counts, v_c)
