import sys
from itertools import *
import time


start_time = time.time()
N = int(sys.argv[1])
num = "0"*N


for x in range(1, N+1):
    num += str(x)

s = set()
for n in permutations(num):
    if n in s:
        continue
    else:
        print(*n)
        s.add(n)

print(f"--- {time.time() - start_time} seconds ---")
