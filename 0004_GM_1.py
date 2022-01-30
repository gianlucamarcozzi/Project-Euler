from time import time, sleep
from GM_utils import GM_is_palindrome as is_palindrome
start_time = time()

def func(N, m):
    for i in range(m//2, 0, -1):
        j = m - i
        if is_palindrome( (N-i)*(N-j) ):
            return (N-i)*(N-j)
    return 0

N = 999
M = N

res = 0

for m in range(N):
    if func(N, m):
        res = func(N, m)
        break

print(f'{res = }, in {time() - start_time} seconds')
