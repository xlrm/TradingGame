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
        coeff = np.random.rand()
        sign = np.random.randint(2)
        if sign == 0:
            self.price += self.price * coeff
        elif sign == 1:
            self.price -= self.price * coeff * (1 / 2)
        if self.price <= 0:
            self.price = 0
        self.prices.append(self.price)
        return self.price
def test(stock):
    for i in range(40):
        stock.fluctuation()
    for i in range(40):
        nextday()
    drawgraph(stock)
