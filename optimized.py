import timeit
from controllers import portfoliosCreator, converters
from models import portfolios


dataset = converters.csvToListAlt("DATA/dataset2.csv")


def optimized(data, budget):
    # create a portofolio instance from list
    portfolio = portfoliosCreator.portfoliosOptimized(data, 500)

    portfolio.getGain()
    portfolio.getValue()
    portfolio.getPrice()

    return portfolio


optimized_pf = optimized(dataset, 500)

print("\n", optimized_pf)
# print(len(optimized_pf.listShares))


n = 30
results = timeit.timeit(stmt="optimized(dataset, 500)", globals=globals(), number=n)
print(f"{results / n} secondes")
