import numpy as np
from time import time
ti = time()

n = 1000

result = np.sum(np.arange(0,n,3)) \
	   + np.sum(np.arange(0,n,5)) \
	   - np.sum(np.arange(0,n,15))\

print(f'{result = }\nin {time()-ti :.3f} seconds')