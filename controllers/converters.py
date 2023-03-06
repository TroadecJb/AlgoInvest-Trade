import csv
from models import shares


def csvToList(pathToFile) -> list:
    # returns a list of share's class instances.

    dataset = list()
    with open(pathToFile, mode="r") as file:
        data = csv.reader(file, delimiter=",")
        next(data)
        dataset = [
            shares.Share(row[0], float(row[1]), float(row[2]))
            for row in data
            if float(row[1]) > 0
        ]
    return dataset


def csvToListAlt(pathToFile) -> list:
    # returns a list of share's class instances.

    dataset = list()
    with open(pathToFile, mode="r") as file:
        data = csv.reader(file, delimiter=",")
        next(data)
        dataset = sorted(
            [
                shares.ShareAlt(row[0], float(row[1]), float(row[2]))
                for row in data
                if float(row[1]) > 0 and float(row[2]) > 0
            ],
            key=lambda i: i.gain,
        )
    return dataset
