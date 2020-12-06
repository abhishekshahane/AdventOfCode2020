file1 = open("./input.txt", "r")
stra = ""
for x in file1:
    stra+=x
arr = stra.split("\n\n")
new_arr =[]
for each in arr:
    new_arr.append(each.replace("\n", " ").replace(":", ","))
valids = 0
for i in range(len(new_arr)):
    if "byr" in new_arr[i] and "iyr" in new_arr[i] and "hgt" in new_arr[i] and "eyr" in new_arr[i] and "hcl" in new_arr[i] and "ecl" in new_arr[i] and "pid" in new_arr[i]:
        valids+=1
print(valids)
