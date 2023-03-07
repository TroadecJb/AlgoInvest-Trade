from controllers import portfoliosCreator, converters


def optimized(data, budget):
    # create a portofolio instance from list
    dataset = converters.csvToListAlt(data)

    best_portfolio = portfoliosCreator.portfoliosOptimizedAlt(dataset, budget)

    return best_portfolio
