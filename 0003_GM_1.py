from time import time, sleep

start_time = time()

N = 600851475143

for i in range(2, N):
    while not N % i:
        N /= i
    if N == 1:
        break

print(f'Result = {i}, in {time() - start_time} seconds')
