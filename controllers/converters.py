import csv
from models import shares


def csvToList_BF(pathToFile) -> list:
    data = list()
    with open(pathToFile, mode="r") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)
        data = [tuple(x) for x in reader]

    dataset = list()
    for i in range(len(data)):
        share = list()
        share.append(data[i][0])
        share.append(float(data[i][1]))
        share.append(round((float(data[i][1]) * float(data[i][2]) / 100), 2))
        dataset.append(tuple(share))

    return dataset


def csvToList(pathToFile) -> list:
    # returns a list of share's class instances sorted by rate/gain/value

    with open(pathToFile, mode="r") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)

        dataset = sorted(
            [
                shares.Share(row[0], float(row[1]), float(row[2]))
                for row in reader
                if float(row[1]) > 0 and float(row[2]) > 0
            ],
            key=lambda s: s.price,
        )

    return dataset
