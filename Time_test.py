import time
import psutil
import os
from memory_profiler import profile
from controllers import bruteforce, optimized


dataset = "DATA/datatest.csv"

start = time.perf_counter()

# @profile
# def BF():
#     return bruteforce.bruteForce(dataset, 100)


@profile
def Opti():
    return optimized.optimized(dataset, 500)


# print(BF())
print(Opti())

end = time.perf_counter()
print(end - start)
