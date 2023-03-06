import itertools
from models import portfolios


def portfoliosCombinations(liste: list, budget) -> list:
    portfolios_list = list()
    for i in range(1, len(liste)):
        combo = itertools.combinations(liste, i)
        for idx, c in enumerate(combo):
            new_portfolio = portfolios.Portfolio(f"pf-{idx}", c)
            if new_portfolio.price <= budget:
                portfolios_list.append(new_portfolio)

    return portfolios_list


def portfoliosOptimized(liste: list, budget) -> portfolios:
    list_shares = liste[:]
    remaining_budget = budget
    min_share_price = list_shares[0].price
    potential_portfolio = portfolios.PortfolioAlt([])

    while remaining_budget > min_share_price:
        available_shares = list(
            filter(lambda share: share.price <= remaining_budget, list_shares)
        )
        # make the only available shares have a price lower than the remaining budget thus purchasable
        try:
            elem = available_shares[-1]
        except IndexError:
            break
        remaining_budget -= elem.price
        potential_portfolio.listShares.append(elem)
        list_shares.remove(elem)

    return potential_portfolio
