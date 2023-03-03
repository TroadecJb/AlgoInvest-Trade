class Portfolio:
    # class for a portfolio, containing a list of shares. With total purchase cost and total gain.

    def __init__(self, name, listShares: tuple) -> None:
        self.name = name
        self.listShares = listShares
        self.price = sum([share.price for share in self.listShares])
        self.gain = sum([share.gain for share in self.listShares])

    # def getPrice(self) -> float:
    #     # return the price to acquire each shares in the listShares
    #     self.price = sum([share.price for share in self.listShares])

    # def getGain(self) -> float:
    #     # return the gain made with every shares in the listShares
    #     self.gain = sum([share.gain for share in self.listShares])

    def __repr__(self) -> str:
        return f"{self.name} Buy cost : {self.price}, Gain : {self.gain}\n {[share.name for share in self.listShares]}\n"
