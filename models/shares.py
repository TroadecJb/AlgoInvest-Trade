# class Share:
#     # class for a share: Name, Price, Rate and Gain

#     def __init__(self, name, price, rate) -> None:
#         self.name = name
#         self.price = price
#         self.rate = rate
#         self.value = self.price * (1 + self.rate / 100)
#         self.gain = (self.price / 100) * self.rate


class Share:
    # class for a share: Name, Price, Value, Gain

    def __init__(self, name, price, rate) -> None:
        self.name = name
        self.price = price
        self.rate = rate
        self.value = round((self.price * (1 + self.rate / 100)), 2)
        self.gain = round(((self.price / 100) * self.rate), 2)

    def __repr__(self) -> str:
        return f"{self.name}, price : {self.price}, rate : {self.rate}, value : {self.value}, gain : {self.gain}"
