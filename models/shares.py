class Share:
    # class for a share: Name, Price, Rate and Gain

    def __init__(self, name, price, rate) -> None:
        self.name = name
        self.price = float(price)
        self.rate = float(rate)
        self.gain = (self.price * self.rate) / 100
