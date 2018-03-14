import random, math

random.seed(1)

def in_circle(x, origin = [0]*2):
   # Define your function here!
    if distance(x,origin) < 1:
        return True
    else:
        return False
        
print (in_circle((1,1),(0,0)))
