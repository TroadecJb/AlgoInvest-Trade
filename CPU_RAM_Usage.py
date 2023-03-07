import timeit
import psutil
import optimized, bruteforce


dataset = "DATA/dataset2.csv"
data_brute_force = "DATA/datatest.csv"

# optimized_pf = optimized.optimized(dataset, 500)
# brute_force_pf = bruteforce.bruteForce(data_brute_force, 500)


print(psutil.cpu_percent(interval=1))

# n = 100
# results = timeit.timeit(stmt="optimized_pf", globals=globals(), number=n)
# print(f"{results / n} secondes")

# n = 10
# results = timeit.timeit(stmt="brute_force_pf", globals=globals(), number=n)
# print(f"{results / n} secondes")
