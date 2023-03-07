import timeit
from controllers import portfoliosCreator, converters


def optimized(data, budget, filter="rate"):
    # create a portofolio instance from list
    dataset = converters.csvToListAlt(data, filter)

    portfolio = portfoliosCreator.portfoliosOptimized(dataset, budget)

    portfolio.getGain()
    portfolio.getValue()
    portfolio.getPrice()

    return portfolio


dataset = "DATA/dataset1.csv"

optimized_pf = optimized(dataset, 500, "gain")

print("\n", optimized_pf)
# print(len(optimized_pf.listShares))


n = 100000
results = timeit.timeit(stmt="optimized_pf", globals=globals(), number=n)
print(f"{results / n} secondes")
