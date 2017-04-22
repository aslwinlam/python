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
    for index in range(len(ROWSOFSTOCKINF) - 1 - 20, 1, -1):
        sum_close_price = 0.0
        for x in range(index + 1, index + 21):   # sum of 20 days loop 21-1
            # close_price = float(closeList[x]) .----..MOD BY USING CLASS
            close_price = float(ROWSOFSTOCKINF[x].trade_close)
            sum_close_price = sum_close_price + close_price
# buy_or_sell(sum_close_price,lowList[index], highList[index])--..MOD BY
        buy_or_sell(sum_close_price, ROWSOFSTOCKINF[index].trade_low, ROWSOFSTOCKINF[index].trade_high)

    # Looping complete, selling the remain stock if any at the high price of
    # the day  highList[0]
    cash = RowOfStockinf.cash
    if RowOfStockinf.numOfStock > 0:
     #   cash = RowOfStockinf.numOfStock * float(highList[1]) ............ MOD by USING CLASS
        cash = RowOfStockinf.numOfStock * float(ROWSOFSTOCKINF[1].trade_high)
    return 0, cash

def buy_or_sell(sum_of_close_price, exe_low, exe_high):
    """ make a buy of sell decison with ratio to closing avg """
    buying_price = (sum_of_close_price / 20) * .9  # .90 want to buy low (use 10%)
    # 1.1 want to sell high (use 10%)
    selling_price = (sum_of_close_price / 20) * 1.1
# global stockHolding ......MOD BY USE OF CLASS
# global money......MOD BY USE OF CLASS
# global stockHolding replaced by RowOfStockinf.numOfStock
# global money replaced by RowOfStockinf.Cash
    if buying_price < float(exe_high) and buying_price > float(exe_low):
       # if money > 0:
        if RowOfStockinf.cash > 0:
            #stockHolding = money/float(exe_low)  .......MOD BY USE OF CLASS
            #money=0.0  ......MOD BY USE OF CLASS
            RowOfStockinf.numOfStock = RowOfStockinf.cash / float(exe_low)
            RowOfStockinf.cash = 0.0
        #    print("BUY")
    elif selling_price > float(exe_low) and selling_price < float(exe_high):
        # if stockHolding > 0: ......MOD BY USE OF CLASS
        #   money = stockHolding*float(exe_high) ......MOD BY USE OF CLASS
        #stockHolding = 0 ......MOD BY USE OF CLASS
        if RowOfStockinf.numOfStock > 0:
            RowOfStockinf.cash = RowOfStockinf.numOfStock * float(exe_high)
            RowOfStockinf.numOfStock = 0
           # print("SELL")


main()
