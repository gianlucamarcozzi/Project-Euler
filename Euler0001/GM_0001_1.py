import time
start_time = time.time()
N = 1000 * 100

print(sum([x for x in range(N) if (not (x % 3) or not (x % 5))]))

print(time.time() - start_time)
