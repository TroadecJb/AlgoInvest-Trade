import random
import string
import csv

with open("DATA/datatestmoyen.csv", mode="w") as file:
    data = csv.writer(file, delimiter=",")
    for i in range(101):
        data.writerow(
            [
                "Share-" + "".join(random.choices(string.ascii_uppercase, k=4)),
                round(random.uniform(0.01, 30.04), 2),
                round(random.uniform(2, 30.04), 2),
            ]
        )
