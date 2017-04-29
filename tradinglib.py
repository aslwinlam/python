class RowOfStockinf(object):
    """A class to store row of trading inf:

    """
    numOfStock = [0.0,0.0,0.0,0.0]
    cash = [2000.0,2000.0,2000.0,2000.0]
    buyMargin = [.97, .95, .93, .91]
    numOfSales=[0,0,0,0]

    def __init__(self, trade_date, trade_open, trade_high, trade_low, trade_close, trade_vol, trade_adj_close):
        self.trade_date = trade_date
        self.trade_open = trade_open
        self.trade_high = trade_high
        self.trade_low = trade_low
        self.trade_close = trade_close
        self.trade_vol = trade_vol
        self.trade_adj_close = trade_adj_close
    # END OF CLASS
