sheet = []
divs = []
while True:
    row = [int(n) for n in input().split()]
    if row:
        sheet.append(row)
    else:
        break
for row in sheet:
    for i in row:
        for j in row:
            if (i % j == 0):
                divs.append(i//j)
while(1 in  divs):
    divs.remove(1)
print(sum(divs))
