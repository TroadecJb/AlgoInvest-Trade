import time
import resource
from controllers import algos

dataset = "DATA/datatest.csv"
budget = 500

start = time.time()
before_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

algo_opti = algos.bruteForce(dataset, budget)

after_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
end = time.time()
ram_usage = after_ram - before_ram
memory = ram_usage / 1024

print(f"Memory usage of algo_bf: {memory} KB")

print(f"Timer : {end - start} seconds")

print(algo_opti)
