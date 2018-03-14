### Exercise 3a

Write a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors n_neighbors on either side of a given member of the list to consider.
For each value in x, moving_window_average(x, n_neighbors) computes the average of that value's neighbors, where neighbors includes the value itself.
moving_window_average should return a list of averaged values that is the same length as the original list.
If there are not enough neighbors (for cases near the edge), substitute the original value as many times as there are missing neighbors.
Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors=1.
