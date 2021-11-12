from ibapi.client import EClient
from ibapi.common import BarData
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import pandas as pd

class TestApp(EWrapper,EClient): # reading, and sending messages
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)
        self.df = pd.DataFrame()
        self.data=[]
    def nextValidId(self, orderId:int):
        #4 first message received is this one
        print("setting nextValidOrderId: %d", orderId)
        self.nextValidOrderId = orderId
        self.start()


    def error(self, reqId, errorCode, errorString):
        # these messages can come anytime.
        print("Error. Id: ", reqId, " Code: ", errorCode, " Msg: ", errorString)

    def contractDetails(self, reqID, contractDetails):  #EWrapper
        print('contractDetails: ', reqID, " ", contractDetails)

    def historicalData(self, reqId: int, bar: BarData):
        print('Historical Data: ',reqId,"Date: ",bar.date,"Open: ",bar.open,"Close: ",bar.close,"High: ",bar.high,"Low: ",bar.low,"Volume: ",bar.volume,"Count: ",bar.barCount,"WAP: ",bar.average)
        year =bar.date[:4]
        month =bar.date[4:6]
        day=bar.date[6:]
        date = '-'.join([year,month,day])
        self.data.append([date,bar.open,bar.close,bar.high,bar.low])


    def historicalDataEnd(self, reqId: int, start: str, end: str):
        #8 data is finished
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        self.df = pd.DataFrame(self.data,columns=['date','open','close','high','low'])
        self.df.to_csv("apple_stock_data.csv")
        print('finished')
        app.disconnect()
        #9 this is the logical end of your program

    def start(self):
        apple_contract = Contract()
        apple_contract.symbol = 'AAPL'
        apple_contract.secType = 'STK'
        apple_contract.exchange = 'SMART'
        apple_contract.currency = 'USD'
        app.reqHistoricalData(4, apple_contract, '', "6 M", "1 day", "MIDPOINT", 1, 1, False, [])




if __name__ == '__main__':
    app = TestApp()
    app.connect("127.0.0.1", 7497, clientId=0)


    app.run()
    # app.reqContractDetails(1,apple_contract) # EClient function

    # app.run()
    # time.sleep(4)
    # app.disconnect()


# plot the candle stick graph for apple stock for the past 3 month, with your name in the title
# use pandas, seaborn or something like that for graphing
# research about stock features (market cap, volumn traded, PE ratio)
# get familiar with sci-kit learn

# extract features from stocks ---> make a big dataframe --> try clustering or something like that

