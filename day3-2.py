from itertools import count

def sum_spiral():
    a, i, j = {(0,0): 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0), (0,0,-1), (1,-1,0), (1,0,1)]:
            for _ in range(s+ds):
                i += di
                j += dj
                a[i,j] = sum(a.get((k, l), 0) for k in range(i-1,i+2) for l in range(j-1, j+2))
                yield a[i,j]
for x in sum_spiral():
    if x > 368078:
        print(x)
        break
