import itertools
from models import portfolios


def portfoliosCombinations(liste: list, budget) -> list:
    portfoliosList = list()
    for i in range(1, len(liste)):
        combo = itertools.combinations(liste, i)
        for idx, c in enumerate(combo):
            new_portfolio = portfolios.Portfolio(f"pf-{idx}", c)
            if new_portfolio.price <= budget:
                portfoliosList.append(new_portfolio)

    return portfoliosList


# def createPFfromDict(dictActions: dict, budget: int) -> list:
#     # returns all combinations of a list which sum are under the budget
#     masterList = list()

#     for i in range(1, len(dictActions) + 1):
#         combo = list(map(dict, itertools.combinations(dictActions.items(), i)))
#         masterList += [
#             portefeuille
#             for portefeuille in combo
#             if sum([valeur[0] for valeur in portefeuille.values()]) <= budget
#         ]
#     return masterList
