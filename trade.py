#import pygame as py
#import button

class trade():
    hold=0                                         #주식 보유량
    def __init__(self, stockname, stockprice):     #주식 이름, 주식의 현재 값
        self.name = stockname
        self.price = stockprice
        self.dic = {"stockname":self.name,
                    "stockprice":self.price,
                    "stockhold": trade.hold}       #주식 딕셔너리 생성.{이름, 현재 주식의 값, 유저의 주식보유량}


#살 숫자와 유저의 돈을 넣으면 출력
    def buystock(self, num, money):
        if money < (num * self.price):
            return 0

        trade.hold += num
        self.dic["stockhold"] = trade.hold
        
        outcome = (num * self.price)
        return outcome


#판매할 값을 넣으면 수입을 반환
    def salestock(self,num):
        
        if trade.hold < num:
            return 0
        
        trade.hold -= num
        self.dic["stockhold"] = trade.hold
        
        income = num * self.price
        return income

#딕셔너리 반환
    def returndic(self):
        return self.dic