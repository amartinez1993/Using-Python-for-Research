import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
# write your code here!
R = 1000
x = []
Y = []

for i in range(R):
    x.append(random.uniform(0,1))
Y.append(x)
    
for i in range(1,10):
    Y.append(moving_window_average(x, n_neighbors = i))
    


