from ibapi.client import EClient
from ibapi.common import BarData
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import *
import pandas as pd

class TestApp(EWrapper,EClient): # reading, and sending messages
    def __init__(self):
        EWrapper.__init__(self)
        EClient.__init__(self, wrapper=self)

    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)
        self.nextorderId = orderId
        print('The next valid order id is: ', self.nextorderId)
        self.start()

    def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId,
                    whyHeld, mktCapPrice):
        print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining,
              'lastFillPrice', lastFillPrice)

    def openOrder(self, orderId, contract, order, orderState):
        print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action,
              order.orderType, order.totalQuantity, orderState.status)

    def execDetails(self, reqId, contract, execution):
        print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId,
              execution.orderId, execution.shares, execution.lastLiquidity)


    def error(self, reqId, errorCode, errorString):
        # these messages can come anytime.
        print("Error. Id: ", reqId, " Code: ", errorCode, " Msg: ", errorString)

    def contractDetails(self, reqID, contractDetails):  #EWrapper
        print('contractDetails: ', reqID, " ", contractDetails)

    def contractCreate(self):
        # Fills out the contract object
        contract1 = Contract()  # Creates a contract object from the import
        contract1.symbol = "AAPL"  # Sets the ticker symbol
        contract1.secType = "STK"  # Defines the security type as stock
        contract1.currency = "USD"  # Currency is US dollars
        # In the API side, NASDAQ is always defined as ISLAND in the exchange field
        contract1.exchange = "SMART"
        # contract1.PrimaryExch = "NYSE"
        return contract1  # Returns the contract object

    def orderCreate(self):
        # Fills out the order object
        order1 = Order()  # Creates an order object from the import
        order1.action = "BUY"  # Sets the order action to buy
        order1.orderType = "MKT"  # Sets order type to market buy
        order1.transmit = True
        order1.totalQuantity = 10  # Setting a static quantity of 10
        return order1  # Returns the order object

    def orderExecution(self,nextID,contractObject,orderObject):
        # Places the order with the returned contract and order objects


        app.placeOrder(nextID, contractObject, orderObject)
        print("order was placed")

    def start(self):
        contractObject = self.contractCreate()
        orderObject = self.orderCreate()
        self.orderExecution(self.nextorderId,contractObject,orderObject)





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

