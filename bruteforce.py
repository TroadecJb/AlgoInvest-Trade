import timeit
from controllers import converters, portfoliosCreator


dataset = converters.csvToList("DATA/datatest.csv")


def bruteForce(data, budget):
    # create portfolio instances form list, sort them by gain in descendig order
    portefeuilles = portfoliosCreator.portfoliosCombinations(dataset, budget)
    portefeuillesSorted = sorted(portefeuilles, key=lambda pf: pf.gain, reverse=True)
    return portefeuillesSorted


# n = 10
# results = timeit.timeit(stmt="bruteForce(dataset, 500)", globals=globals(), number=n)
# print(f"{results / n} secondes")

test_Datatest = bruteForce(dataset, 500)
print("longueur liste main :", len(test_Datatest))
# for pf in test_Datatest[:30]:
#     print(pf)
