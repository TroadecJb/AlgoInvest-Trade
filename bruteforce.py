from controllers import portfoliosCreator, converters


def bruteForce(data, budget):
    # create portfolio instance from list, sort them by gain in descendig order
    dataset = converters.csvToListAlt(data)
    portefeuilles = portfoliosCreator.portfoliosCombinations(dataset, budget)
    portefeuillesSorted = sorted(portefeuilles, key=lambda pf: pf.gain, reverse=True)
    return portefeuillesSorted[0]
