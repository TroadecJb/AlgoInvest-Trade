from controllers import portfoliosCreator, converters, rateCalculators


def bruteForce(data, budget):
    # create portfolio instance from list, sort them by gain in descendig order
    dataset = converters.csvToList(data)
    portefeuilles = portfoliosCreator.portfoliosCombinations(dataset, budget)

    return portefeuilles
