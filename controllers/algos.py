from controllers import portfoliosCreator, converters


def bruteForce_itertools(data, budget):
    # create portfolio instance from list, sort them by gain in descendig order
    dataset = converters.csvToList(data)
    portefeuilles = portfoliosCreator.portfoliosCombinations(dataset, budget)

    return portefeuilles


def bruteForce(data, budget):
    dataset = converters.csvToList_BF(data)
    portefeuilles = portfoliosCreator.portfolio_BF(dataset, budget)
    return f"\nBuy cost: {sum([s[1] for s in portefeuilles[1]])}, Value {sum([s[1] for s in portefeuilles[1]]) + sum([s[2] for s in portefeuilles[1]])}, Gain : {round(sum([s[2] for s in portefeuilles[1]]),2)}\n {[s[0] for s in portefeuilles[1]]}\n"


def optimized(data, budget):
    # create a portofolio instance from list

    dataset = converters.csvToList(data)
    best_portfolio = portfoliosCreator.portfoliosOptimized(dataset, budget)

    return best_portfolio
