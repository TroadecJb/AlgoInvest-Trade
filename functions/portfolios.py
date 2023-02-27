import itertools


def createPFfromList(listActions: list, budget: int) -> list:
    # returns all combinations of a list which sum are under the budget
    masterList = list()

    for i in range(1, len(listActions) + 1):
        combo = list(itertools.combinations(listActions, i))

        masterList += [
            portefeuille
            for portefeuille in combo
            if sum([action[0] for action in portefeuille]) <= budget
        ]

    return masterList


def createPFfromDict(dictActions: dict, budget: int) -> list:
    # returns all combinations of a list which sum are under the budget
    masterList = list()

    for i in range(1, len(dictActions) + 1):
        combo = list(map(dict, itertools.combinations(dictActions.items(), i)))
        masterList += [
            portefeuille
            for portefeuille in combo
            if sum([valeur[0] for valeur in portefeuille.values()]) <= budget
        ]
    return masterList
