import math

def distance(x, y):
    total = 0
    if len(x) == len(y):
        square_differences = [(x[i]-y[i])**2 for i in range(len(x))]
        return math.sqrt(sum(square_differences))

print(distance((0,0),(1,1)))
