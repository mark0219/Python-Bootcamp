import math

def addone(x):
    return(x+1)
    
def series(x,y):
    series_sum=1.0
    count = 0
    print x,y, 1.0/(float(x)**float(count+1))
    while 1.0/(float(x)**float(count+1)) >float(y):
        count += 1
        series_sum += 1.0/(float(x)**float(count))
    return(series_sum,count)

for i in range(3):
    print i, math.sqrt(i), addone(i)

print
ans, count=series(2.0,0.000000000001)
print ans,count