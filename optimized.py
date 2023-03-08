from controllers import portfoliosCreator, converters


def optimized(data, budget):
    # create a portofolio instance from list
    dataset = converters.csvToList(data)

    best_portfolio = portfoliosCreator.portfoliosOptimized(dataset, budget)

    return best_portfolio
