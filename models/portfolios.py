class Portfolio:
    # class for a portfolio, containing a list of shares. With total purchase cost, total value after two years and total gain.

    def __init__(self, listShares) -> None:
        self.listShares = listShares
        self.price = 0
        self.value = 0
        self.gain = 0

    def __repr__(self) -> str:
        return f"\nBuy cost : {self.price}, Value : {self.value}, Gain : {self.gain}\n {[share.name for share in self.listShares]}\n"

    def getPrice(self):
        self.price = round(sum([share.price for share in self.listShares]), 2)

    def getValue(self):
        self.value = round((sum([share.value for share in self.listShares])), 2)

    def getGain(self):
        self.gain = round(sum([share.gain for share in self.listShares]), 2)
