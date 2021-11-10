import numpy as np
import matplotlib.pyplot as plt

date = [1]
nowdate = 1

def append():
    date.append(nowdate)
def plusdate():
    global nowdate
    nowdate += 1
def nextday():
    plusdate()
    append()
def drawgraph(stock):
    plt.plot((date), (stock.prices))
    plt.show()

class Stock():
    def __init__(self, issue):
        self.issue = issue
        self.price = issue
        self.prices = [issue]
    def fluctuation(self):
        coeff = np.random.randn()
        self.price += self.price * coeff
        self.prices.append(self.price)
        return self.price
