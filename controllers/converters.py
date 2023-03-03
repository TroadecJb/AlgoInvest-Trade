import csv
from models import shares


def csvToList(pathToFile) -> list:
    # returns a list of share's class instances.

    dataset = list()
    with open(pathToFile, mode="r") as file:
        data = csv.reader(file, delimiter=",")
        next(data)
        dataset = [shares.Share(row[0], row[1], row[2]) for row in data]
    return dataset
