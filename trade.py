class Trade:
    hold = 0  # 주식 보유량

    def __init__(self, stockname, price):  # 주식 이름, 주식의 현재 값
        self.name = stockname
        # self.pricelist=pricelist
        self.price = price
        self.dic = {
            "stockname": self.name,
            "cur_price": self.price,
            "stockhold": Trade.hold,
        }  # 주식 딕셔너리 생성.{이름, 현재 주식의 값, (주식이름) 주식보유량}

    # 살 개수와 유저의 돈을 넣으면 출력
    def buystock(self, num, money):
        if money < (num * self.price):
            return 0

        Trade.hold += num
        self.dic["stockhold"] = Trade.hold

        outcome = num * self.price
        return outcome

    # 판매할 값을 넣으면 수입을 반환
    def sellstock(self, num):

        if Trade.hold < num:
            return 0

        Trade.hold -= num
        self.dic["stockhold"] = Trade.hold

        income = num * self.price
        return income

    # 딕셔너리 반환
    def returndic(self):
        return self.dic

    # 플레이어 주식 보유량 반환
    def returnhold(self):
        return Trade.hold
