import timeit
from controllers import portfoliosCreator, converters


# dataset = converters.csvToListAlt("DATA/dataset1.csv")


def optimized(budget):
    # create a portofolio instance from list
    dataset = converters.csvToListAlt("DATA/dataset2.csv")

    portfolio = portfoliosCreator.portfoliosOptimized(dataset, 500)

    portfolio.getGain()
    portfolio.getValue()
    portfolio.getPrice()

    return portfolio


optimized_pf = optimized(500)

print("\n", optimized_pf)
# print(len(optimized_pf.listShares))


n = 30
results = timeit.timeit(stmt="optimized(500)", globals=globals(), number=n)
print(f"{results / n} secondes")
