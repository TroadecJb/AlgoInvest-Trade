import csv
from models import shares


def listToDict(liste: list) -> dict:
    # returns a dictionnary from a list where every elements is a tuple/list of two subelements
    dico = dict()
    for idx, e in enumerate(liste):
        dico[f"action-{idx+1}"] = [e[0], e[1]]

    return dico


def csvToDict(pathToFile) -> dict:
    # returns a dictionnary from a csv
    dico = dict()
    with open(pathToFile, mode="r") as file:
        data = csv.reader(file, delimiter=",")
        next(data)
        for idx, l in enumerate(data):
            dico[f"action-{idx+1}"] = [float(l[1]), float(l[2])]

    return dico


def csvToList(pathToFile) -> list:
    # returns a list of share's class instances sorted by rate/gain/value

    dataset = list()
    with open(pathToFile, mode="r") as file:
        data = csv.reader(file, delimiter=",")
        next(data)

        dataset = sorted(
            [
                shares.Share(row[0], float(row[1]), float(row[2]))
                for row in data
                if float(row[1]) > 0 and float(row[2]) > 0
            ],
            key=lambda s: s.price,
        )

    return dataset
