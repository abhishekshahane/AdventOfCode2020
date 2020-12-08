import re
def check(arr):
    valids = 0
    for i in range(len(arr)):
        a = []
        se = []
        for k in range(len(arr[i])):
            se.append(arr[i][k])
            a.append(arr[i][k][0])
        if "byr" in a and "iyr" in a and "hgt" in a and "eyr" in a and "hcl" in a and "ecl" in a and "pid" in a:
            an = True
            for field in se:
                if field[0]=="iyr":
                    if len(str(field[1]))==4 and int(field[1])>=2010 and int(field[1])<=2020:
                        an = True
                    else: 
                        an=False
                        continue

                elif field[0]=="byr":
                    if len(str(field[1]))==4 and int(field[1])>=1920 and int(field[1])<=2002:
                        an=True
                    else:
                        an=False
                        continue

                        
                elif field[0]=="eyr":
                    if len(str(field[1]))==4 and int(field[1])>=2020 and int(field[1])<=2030:
                        an=True
                    else:
                        an=False
                        continue

                elif field[0] == "hgt":
                    if field[1][-2:]=='cm' and int(field[1][:-2]) >=150 and int(field[1][:-2]) <= 193:
                        an=True
                    elif field[1][-2:]=='in' and int(field[1][:-2]) >= 59 and int(field[1][:-2]) <= 76:
                        an=True
                    else:
                        an = False
                        continue
                elif field[0]=="hcl":
                    if field[1][0]=="#" and field[1][:0].isalnum()==True:
                        an=True
                    else:
                        an=False
                        continue
                
                elif field[0]=="ecl":
                    lst = ["amb", "blu" ,"brn", "gry", "grn", "hzl", "oth"]
                    if field[1] in lst:
                        an=True
                    else:
                        an=False
                        continue
                elif field[0]=="pid":
                    if len(str(field[1]))==9:
                        an=True
                    else:
                        an=False
                        continue

            if an==True:
                print(se)
                valids+=1

        else:
            continue
    print(valids)
        
file1 = open("./input.txt", "r")
stra = ""
for x in file1:
    stra+=x
arr = stra.split("\n\n")
new_arr =[]
for each in arr:
    new_arr.append(each.replace("\n", " "))
final_arr = []
for each in new_arr:
    final_arr.append(each.split(" "))

for i in range(len(final_arr)):
    for j in range(len(final_arr[i])):
        final_arr[i][j] = final_arr[i][j].split(":")
check(final_arr)
