from itertools import cycle
record = []
steps = 0
li = [int(x) for x in input().split()]
while li not in record:
    n = max(li)
    i = li.index(n)
    print(li)
    record.append(li[:])
    li[i] = 0
    for counter, x in enumerate(cycle(li)):
        if(counter >= i + 1):
            n -= 1
            li[counter % len(li)] += 1
        if (n == 0):
            break
    print(li)
    print(record)
    print(len(record))
print("Cycles for repitition --> " + str(len(record) - record.index(li)))
