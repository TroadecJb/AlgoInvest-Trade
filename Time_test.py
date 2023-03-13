import time
from memory_profiler import profile
from controllers import bruteforce, optimized


dataset = "DATA/dataset1.csv"

start = time.perf_counter()


# @profile
def BF():
    return bruteforce.bruteForce(dataset, 500)


@profile
def Opti():
    return optimized.optimized(dataset, 500)


end = time.perf_counter()
print(end - start)

# print(BF())
print(Opti())
