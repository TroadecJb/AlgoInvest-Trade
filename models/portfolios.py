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


class PortfolioAlt:
    # class for a portfolio, containing a list of shares. With total purchase cost, total value after two years and total gain.

    def __init__(self, listShares) -> None:
        self.listShares = listShares
        self.price = 0
        self.value = 0
        self.gain = 0

    def __repr__(self) -> str:
        return f"Buy cost : {self.price}, Value : {self.value}, Gain : {self.gain}\n {[share.name for share in self.listShares]}"

    def getPrice(self):
        self.price = round(sum([share.price for share in self.listShares]), 2)

    def getValue(self):
        self.value = round((sum([share.value for share in self.listShares])), 2)

    def getGain(self):
        self.gain = round(sum([share.gain for share in self.listShares]), 2)
