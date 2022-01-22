import time
import sys
from fibonacci_util import fibonacci, fibonacci_index

start_time = time.time()

N = 4000000 # Four million

print(sum([fibonacci(n) for n in range(fibonacci_index(N)) if not fibonacci(n) % 2]))

print(time.time() - start_time)
