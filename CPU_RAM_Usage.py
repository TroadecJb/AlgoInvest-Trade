import time
import bruteforce, optimized

dataset = "DATA/datatest.csv"
brute_force_pf = bruteforce.bruteForce(dataset, 500)


# dataset = "DATA/datatest.csv"
optimized_pf = optimized.optimized(dataset, 500)


#### process timer and print results
results = time.process_time()
print(f"\nTimer : {results} secondes")

print(optimized_pf)
print(brute_force_pf)
