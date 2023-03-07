import timeit
from controllers import portfoliosCreator, converters


def optimized(data, budget):
    # create a portofolio instance from list
    dataset = converters.csvToListAlt(data)

    best_portfolio = portfoliosCreator.portfoliosOptimizedAlt(dataset, budget)

    return best_portfolio


dataset = "DATA/dataset2.csv"


optimized_pf = optimized(dataset, 500)

print(optimized_pf)


n = 100000
results = timeit.timeit(stmt="optimized_pf", globals=globals(), number=n)
print(f"{results / n} secondes")
