sheet = []
diffs = []
while True:
    row = [int(n) for n in input().split()]
    if row:
        sheet.append(row)
    else:
        break
for row in sheet:
    diffs.append(max(row) - min(row))
print(sum(diffs))
