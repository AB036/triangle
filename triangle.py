import random


def line(x0,y0, x1, y1):
    dx = abs(x0-x1) 
    dy = -abs(y0-y1) 
    sx = 1 if x0 < x1 else -1 
    sy = 1 if y0 < y1 else -1 
    err = dx + dy 
    while 1: 
        yield x0, y0
        e2 = 2*err;
        if (x0 == x1) and (y0 == y1): 
            break 
        if e2 >= dy: 
            err += dy 
            x0 += sx 
        if e2 <= dx: 
            err += dx 
            y0 += sy 


l = [] 
for k in range(6): 
    l.append(random.randint(0,100))
s = set()
for t1,t2 in ((0,2),(0,4),(2,4)): 
    x1,y1 = l[t1], l[t1+1] 
    x2,y2 = l[t2], l[t2+1] 
    for x,y in line(x1,y1,x2,y2):
        s.add((x,y))

xmin = min([c[0] for c in s])
xmax = max([c[0] for c in s])
ymin = min([c[1] for c in s])
ymax = max([c[1] for c in s])

        
for y in range(ymin, ymax+1): 
    for x in range(xmin, xmax+1): 
        if (x,y) in s: 
            print("*", end="") 
        else: 
            print(" ",end="")
    print()
