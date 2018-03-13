import time

start = time.time()
for i in range(1000):
    play_strategic_game()
stop = time.time()
print ("Time: "+str(stop-start))
plt.hist(i)
plt.show()
