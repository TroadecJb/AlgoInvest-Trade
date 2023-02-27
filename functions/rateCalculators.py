def rateReturn(action):
    # calcul combien une action rapporte
    return action[0] * action[1] / 100


def rateReturnList(portFolio: list) -> list:
    # calcul combien toutes les actions dans la liste rapportent
    return [action[0] * action[1] / 100 for action in portFolio]


def rateReturnDict(portfolio: list) -> list:
    # calcul combien toutes les actions d'une liste de dictionnaire rapportent
    portfolioReturn = list()
    for pf in portfolio:
        total = 0
        for data in pf.values():
            gain = rateReturn(data)
            total += gain

        portfolioReturn.append(total)
    return portfolioReturn


def sortBySumReturns(listPortfolios: list, key_list=1, desc=True) -> list:
    portfolios = listPortfolios
    returnValues = rateReturnDict(listPortfolios)

    return sorted(
        zip(portfolios, returnValues), reverse=desc, key=lambda x: x[key_list]
    )
