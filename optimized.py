import time
import resource
from controllers import algos

dataset = "DATA/dataset2.csv"
budget = 500

before_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

start = time.time()

algo_opti = algos.optimized(dataset, budget)

after_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
ram_usage = after_ram - before_ram
memory = ram_usage / 1024

print(f"Memory usage of algo_opti: {memory} KB")
end = time.time()

print(f"Timer : {end - start} seconds")

print(algo_opti)
