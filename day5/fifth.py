inp = open("input.txt", "r")
arr =[]

for each in inp:
    arr.append(each)
#lambda to remove \n from each
remove = list(map(lambda a: a.strip("\n"), arr))
seat_ids = []
for each in remove:
    d = each[:7]
    e = each[7:]
    ans1 = d.replace('F', '0').replace('B', '1')
    ans2 = e.replace('L','0').replace('R', '1')
    seat_ids.append(int(ans1,2)*8+int(ans2,2))
print(max(seat_ids))
for i in range(100, max(seat_ids)-100):
    if i not in seat_ids:
        print(i)
    
