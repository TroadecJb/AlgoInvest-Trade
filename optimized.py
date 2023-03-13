import timeit
from controllers import algos

dataset = "DATA/dataset1.csv"
budget = 500

algo_opti = algos.optimized(dataset, budget)

loop = 1_000_000
result = timeit.timeit("algo_opti", globals=globals(), number=loop)
print(f"Timer : {result / loop} seconds")

print(algo_opti)
