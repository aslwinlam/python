"""
The program 's function read csv file of MSFT or APPL
It reads data on each day and make buy and sell decision from prior 21 days close avg
Program start from the past and end to the current day
"""

import csv

class RowOfStockinf(object):
    """A class to store row of trading inf:

    """
    numOfStock = 0.0
    cash = 1000

    def __init__(self, trade_date, trade_open, trade_high, trade_low, trade_close, trade_adj_close):
        self.trade_date = trade_date
        self.trade_open = trade_open
        self.trade_high = trade_high
        self.trade_low = trade_low
        self.trade_close = trade_close
        self.trade_adj_close = trade_adj_close
    # END OF CLASS


ROWSOFSTOCKINF = []  # ..........NEW FOR USING CLASS

# money =1000.0    ..............REPLACED BY USING CLASS
# stockHolding =0.0..............REPLACED BY USING CLASS


def main():
    """ Main module"""
    #using MSFT.csv or AAPL.csv
    filename = input("Enter the filename for stock data(CSV format)")
    alg1_balance = alg_moving_avg(filename)
    print(alg1_balance)


def alg_moving_avg(filename):
    """ Calc closing avg"""
    # closeList =[]  ..............REPLACED BY USING CLASS
    # highList=[]     ..............REPLACED BY USING CLASS
    # lowList=[]    ..............REPLACED BY USING CLASS
    csvfile = open(filename, "r")
    rows = csv.reader(csvfile, delimiter=',')
    for row in rows:
        # lowList.append((row[3]))..............REPLACED BY USING CLASS
        # highList.append((row[2]))..............REPLACED BY USING CLASS
        # closeList.append((row[4]))..............REPLACED BY USING CLASS
        stock_inf_obj = RowOfStockinf(
            row[0], row[2], row[2], row[3], row[4], row[5])  # create Object
        ROWSOFSTOCKINF.append(stock_inf_obj)
    csvfile.close()

# for index in range(len(closeList),len(closeList)-1):..MOD BY USING CLASS..
    # the trading is on the 21 days counting backward
# Buy $1000 of stock base on the the last row's lowest price

cash =1000
stock =0


    lastRow =len(ROWSOFSTOCKINF) - 1
    lowPrice = float(ROWSOFSTOCKINF[lastRow].trade_low)
    highPrice= float(ROWSOFSTOCKINF[lastRow].trade_high)    
    avgPrice = (lowPrice+highPrice)/2

    pricePay = avgPrice
    stockHold = 1000/avgPrice
    cash = 0
    priceTosell = pricePay + 100/stockHold

# Day trading program
""" Profit to make $100 per transaction """





    for index in range(len(ROWSOFSTOCKINF) - 2, 1, -1):
        toDaylowPrice = float(ROWSOFSTOCKINF[index].trade_low)    
        toDayHighPrice = float(ROWSOFSTOCKINF[index].trade_high)
        executePrice = (toDaylowPrice + toDayHighPrice) / 2
        

        # SELL CONDITION
        if cash=0:      
            if priceTosell < toDayHighPrice and priceTosell > toDaylowPrice:
            # do my selling
            cash = stockHold * executePrice
            stockHold = 0
            priceToBuy = executePrice * .90

        if stockHold =0:
            if priceToBuy < toDayHighPrice and priceToBuy > toDaylowPrice:
                # do my buy
            stockHold =  cash/ executePrice
            cash = 0
            priceTosell = executePrice + 100/stockHold







       


main()
