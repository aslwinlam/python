import csv

"""
The program 's function read csv file of MSFT or APPL
It reads data on each day and make buy and sell decision from prior 21 days close avg
Program start from the past and end to the current day
"""

class cannonball:
    def getvolcity(self):
        x= time*speed
        return x

    def getBuster():
        print('blak')
    

    time=11
    speed=13

cannonObject = cannonball()
y = cannonObject.getvolcity()


class StockDailyInf:
    """ Class to carry daily stock information"""
    moneyTobuy = 1000
    stockBought = 0.0

    def __init__(self, tradeDay, openPrice, highPrice, lowPrice, closePrice, volumn, adjCLosePrice):
        self.tradeDay = tradeDay
        self.openPrice = openPrice
        self.highPrice = highPrice
        self.lowPrice = lowPrice
        self.closePrice = closePrice
        self.volumn = volumn
        self.adjClosePrice = adjCLosePrice






money =1000.0     # starting $1000 - to be changes per trade 
stockHolding =0.0

def main():
    #using MSFT.csv or AAPL.csv
    filename = input("Enter the filename for stock data(CSV format)")
    alg1_balance = alg_moving_avg(filename)
    print(alg1_balance)
# copy here

def alg_moving_avg(filename):

    """
    #closeList =[]   # list to how close column from the csv file 
    #highList=[]     # list to how high column from the csv file (buy/sell decison)
    #lowList=[]      # list to how low column from the csv file (buy/sell decison)
    """
    allTradingInf =[]
    csvfile = open(filename,"r")
    rows = csv.reader(csvfile, delimiter=',')

    for row in rows:
        tradingInfObj = StockDailyInf(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        allTradingInf.append(tradingInfObj)
    #BEFORE USING CLASS " 
    """     
        #lowList.append((row[3]))
        #highList.append((row[2]))
        #closeList.append((row[4]))
    """
    #BEFORE USING CLASS"

    csvfile.close()
     
   
    for index in range(len(allTradingInf)-1-20,1,-1):    # the trading is on the 21 days counting backward   
        sumClosingPrice= 0.0
        for x in range(index+1, index+21):   # sum of 20 days loop 21-1
           # closePrice = float(closeList[x]) 
            closePrice = float(allTradingInf[x].closePrice) 
            sumClosingPrice = sumClosingPrice + closePrice
        buyOrSell(sumClosingPrice,allTradingInf[index].lowPrice, allTradingInf[index].highPrice) # reach the sum of 20 days here
    # Looping complete, selling the remain stock if any at the high price of the day  highList[0]
    cash = money
    if stockHolding > 0:
        cash = stockHolding*float(allTradingInf[1].highPrice)

       # C:\Users\PCUser\AppData\Local\Programs\Python\Python36-32\,vscode\milestone2a.py
       
    return 0,cash
    

def buyOrSell(sumOfClosePrice, exeLow, exeHigh):   
    buyingPrice = (sumOfClosePrice/20)*.9   #  .90 want to buy low (use 10%)
    sellingPrice = (sumOfClosePrice/20)*1.1 # 1.1 want to sell high (use 10%)
    global stockHolding
    global money
    if buyingPrice < float(exeHigh) and buyingPrice > float(exeLow):
        if money > 0:
            stockHolding = money/float(exeLow)          
            money=0.0
        #    print("BUY")
    elif sellingPrice > float(exeLow) and sellingPrice < float(exeHigh) :
        if stockHolding > 0:
            money = stockHolding*float(exeHigh)
            stockHolding = 0
           # print("SELL")
           
  #<--- end copy 



main()
        

   

