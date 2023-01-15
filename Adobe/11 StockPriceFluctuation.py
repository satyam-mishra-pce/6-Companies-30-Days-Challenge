class StockPrice:

    def __init__(self):
        self.records = dict()
        self.latesttimestamp = None
        from sortedcontainers import SortedList
        self.prices = SortedList()

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.records:
            self.prices.remove(self.records[timestamp])
        self.records[timestamp] = price
        self.prices.add(price)
        if self.latesttimestamp is None:
            self.latesttimestamp  = timestamp
        else:
            self.latesttimestamp = max(self.latesttimestamp, timestamp)

    def current(self) -> int:
        return self.records[self.latesttimestamp] 

    def maximum(self) -> int:
        return self.prices[~0]

    def minimum(self) -> int:
        return self.prices[0]
