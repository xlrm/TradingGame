import numpy as np


class Stock:
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
        return int(self.price)
