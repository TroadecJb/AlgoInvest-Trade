import itertools
from models import portfolios


def portfoliosCombinations(liste: list, budget) -> list:
    portfolios_list = list()
    for i in range(1, len(liste)):
        combo = itertools.combinations(liste, i)

        for c in combo:
            new_portfolio = portfolios.Portfolio(c)
            new_portfolio.getPrice()
            if new_portfolio.price <= budget:
                new_portfolio.getGain()
                new_portfolio.getValue()
                portfolios_list.append(new_portfolio)
    portfolios_list.sort(key=lambda pf: pf.gain, reverse=True)
    return portfolios_list[0]


def portfolio_BF(liste: list, budget, portfolio=[]):
    if liste:
        list_one = portfolio_BF(liste[1:], budget, portfolio)

        first_share = liste[0]

        if first_share[1] <= budget:
            list_two = portfolio_BF(
                liste[1:], budget - first_share[1], portfolio + [first_share]
            )

            if list_one < list_two:
                return list_two

        return list_one
    else:
        return round(sum([share[2] for share in portfolio]), 2), portfolio


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

    list_by_gain = sorted(liste, key=lambda s: s.rate)

    min_share_price = liste[0].price

    potential_portfolio = portfolios.Portfolio([])

    while budget >= min_share_price:
        available_shares = list(
            filter(lambda share: share.price <= budget, list_by_gain)
        )
        # make the only available shares have a price lower than the remaining budget thus purchasable
        try:
            elem = available_shares.pop(-1)
        except IndexError:
            break
        budget -= elem.price
        potential_portfolio.listShares.append(elem)
        list_by_gain.remove(elem)

    # update portfolio's attribute thanks to the methods
    potential_portfolio.getGain()
    potential_portfolio.getPrice()
    potential_portfolio.getValue()

    return potential_portfolio
