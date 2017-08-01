import math

def addone(x):
    return(x+1)
    
def series(x,iters):
    series_sum=1.0
    count = 0
    for i in range(iters-1):
        series_sum += 1.0/(float(x)**float(i))
    return(series_sum)

for i in range(3):
    print i, math.sqrt(i), addone(i)

print
ans = series(2.0,10)
print ans