li = []
steps = 0
while True:
    s = input()
    if s:
        li.append(int(s))
    else:
        break
print(li)
i = 0
while True:
    li[i] = li[i] + 1
    steps = steps + 1
    i = i + (li[i] - 1)
    if(i >= len(li)):
        print("Steps -->" + str(steps))
        break
