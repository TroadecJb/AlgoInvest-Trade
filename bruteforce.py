import timeit
import itertools
import pprint
from functions import converters, portfolios, rateCalculators

ACTIONS = [
    (20, 5),
    (30, 10),
    (50, 15),
    (40, 20),
    (60, 17),
    (80, 25),
    (22, 7),
    (26, 11),
    (48, 13),
    (34, 27),
    (42, 17),
    (110, 9),
    (38, 23),
    (14, 1),
    (18, 3),
    (8, 8),
    (4, 12),
    (10, 14),
    (24, 21),
    (114, 18),
]

# ACTIONS_sorted = sorted(ACTIONS, key=lambda e: e[0])

# dicActions = converters.listToDict(ACTIONS_sorted)

# portefeuilles = portfolios.createPFfromDict(dicActions, 500)

# firstItems = portefeuilles[:30]
# firstItemsReturn = rateCalculators.rateReturnDict(portefeuilles[:30])


def main():
    ACTIONS_sorted = sorted(ACTIONS, key=lambda e: e[0])

    dicActions = converters.listToDict(ACTIONS_sorted)

    portefeuilles = portfolios.createPFfromDict(dicActions, 500)

    portefeuilles = portfolios.createPFfromDict(dicActions, 500)
    portefeuillesSorted = rateCalculators.sortBySumReturns(portefeuilles)

    return portefeuillesSorted


# n = 10
# results = timeit.timeit(stmt="main()", globals=globals(), number=n)
# print(f"{results / n} secondes")

x = main()
print("longueur liste main :", len(x))
# print(x[:20])

pprint.pprint(x[:10])
