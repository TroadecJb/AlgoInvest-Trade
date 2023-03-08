import itertools
from models import portfolios


def portfoliosCombinations(liste: list, budget) -> list:
    portfolios_list = list()
    for i in range(1, len(liste)):
        combo = itertools.combinations(liste, i)

        for idx, c in enumerate(combo):
            new_portfolio = portfolios.Portfolio(c)
            new_portfolio.getPrice()
            if new_portfolio.price <= budget:
                new_portfolio.getGain()
                new_portfolio.getValue()
                portfolios_list.append(new_portfolio)
    portfolios_list.sort(key=lambda pf: pf.gain, reverse=True)
    return portfolios_list[0]


def createPFfromDict(dictActions: dict, budget: int) -> list:
    # returns all combinations of a list which sum are under the budget

    combos = [
        pf
        for i in range(1, len(dictActions) + 1)
        for pf in map(dict, itertools.combinations(dictActions.items(), i))
    ]

    return combos


def portfoliosOptimized(liste: list, budget) -> portfolios:
    ### return a portfolio instance with a list of share instance where the total purchase cost is within the limit of a budget
    ###

    # create two lists, sorted either by gain or rate
    list_by_gain = sorted(liste, key=lambda s: s.gain)
    list_by_rate = sorted(liste, key=lambda s: s.rate)

    mother_of_list = [list_by_gain, list_by_rate]

    min_share_price = liste[0].price
    print(min_share_price)

    portfolios_list = []

    for i in range(len(mother_of_list)):
        remaining_budget = budget
        potential_portfolio = portfolios.Portfolio([])

        while remaining_budget >= min_share_price:
            available_shares = list(
                filter(lambda share: share.price <= remaining_budget, mother_of_list[i])
            )
            # make the only available shares have a price lower than the remaining budget thus purchasable
            try:
                elem = available_shares.pop(-1)
            except IndexError:
                break
            remaining_budget -= elem.price
            potential_portfolio.listShares.append(elem)
            mother_of_list[i].remove(elem)

        # update portfolio's attribute thanks to the methods
        potential_portfolio.getGain()
        potential_portfolio.getPrice()
        potential_portfolio.getValue()
        portfolios_list.append(potential_portfolio)

    portfolios_list.sort(key=lambda pf: pf.gain, reverse=True)
    return portfolios_list[0]
