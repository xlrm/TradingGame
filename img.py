import pygame as pg
import button


class ImageList:
    def __init__(self):
        self.mainmenu_img = pg.image.load("image/screen/메인화면.png")
        self.howtomenu_img = pg.image.load("image/screen/게임설명.png")
        self.gamebg_img = pg.image.load("image/screen/게임화면.png")
        self.showbuy_img = pg.image.load("image/screen/매수창.png")
        self.gameclear_img = pg.image.load("image/screen/게임승리.png")
        self.gameover_img = pg.image.load("image/screen/게임오버.png")

        self.startbutton_img = pg.image.load("image/button/게임시작버튼.png")
        self.howtobutton_img = pg.image.load("image/button/게임방법버튼.png")
        self.cancelbutton_img = pg.image.load("image/button/취소버튼.png")

        self.sell_img = pg.image.load("image/button/매도버튼.png")
        self.decidesell_img = pg.image.load("image/button/매도결정.png")
        self.nextday_img = pg.image.load("image/button/다음날로.png")
        self.ten_img = pg.image.load("image/button/10주.png")
        self.thirty_img = pg.image.load("image/button/30주.png")
        self.fifty_img = pg.image.load("image/button/50주.png")
        self.hundred_img = pg.image.load("image/button/100주.png")
        self.decidebuy_img = pg.image.load("image/button/매수결정.png")
        self.buy_img = pg.image.load("image/button/매수버튼.png")
        self.tradeall_img = pg.image.load("image/button/전체수량.png")

        self.playagain_img = pg.image.load("image/button/다시하기.png")
        self.exitgame_img = pg.image.load("image/button/게임종료.png")
        self.seedicon_img = pg.image.load("image/etc/시드머니아이콘.png")
        self.goal_img = pg.image.load("image/etc/목표자산.png")
        self.stock1_img = pg.image.load("image/etc/주식1.png")
        self.stock2_img = pg.image.load("image/etc/주식2.png")
        self.stock3_img = pg.image.load("image/etc/주식3.png")
        self.holdstock_img = pg.image.load("image/etc/주식보유량.png")
        self.tradevolume_img = pg.image.load("image/etc/거래량.png")

        self.sellalarm1_img = pg.image.load("image/etc/매도량알람1.png")
        self.buyalarm1_img = pg.image.load("image/etc/매수량알람1.png")
        self.sellalarm2_img = pg.image.load("image/etc/매도량알람2.png")
        self.buyalarm2_img = pg.image.load("image/etc/매수량알람2.png")
        self.successalarm_img = pg.image.load("image/etc/거래성공알람.png")

    def IMAGEDIC(self):
        dic = {
            "mainmenu_img": self.mainmenu_img,
            "howtomenu_img": self.howtomenu_img,
            "gamebg_img": self.gamebg_img,
            "showbuy_img": self.showbuy_img,
            "gameclear_img": self.gameclear_img,
            "gameover_img": self.gameover_img,
            "startbutton_img": self.startbutton_img,
            "howtobutton_img": self.howtobutton_img,
            "cancelbutton_img": self.cancelbutton_img,
            "sell_img": self.sell_img,
            "nextday_img": self.nextday_img,
            "ten_img": self.ten_img,
            "thirty_img": self.thirty_img,
            "fifty_img": self.fifty_img,
            "hundred_img": self.hundred_img,
            "decidebuy_img": self.decidebuy_img,
            "decidesell_img": self.decidesell_img,
            "buy_img": self.buy_img,
            "tradeall_img": self.tradeall_img,
            "playagain_img": self.playagain_img,
            "exitgame_img": self.exitgame_img,
            "seedicon_img": self.seedicon_img,
            "goal_img": self.goal_img,
            "stock1_img": self.stock1_img,
            "stock2_img": self.stock2_img,
            "stock3_img": self.stock3_img,
            "holdstock_img": self.holdstock_img,
            "tradevolume_img": self.tradevolume_img,
            "sellalarm1_img": self.sellalarm1_img,
            "buyalarm1_img": self.buyalarm1_img,
            "sellalarm2_img": self.sellalarm2_img,
            "buyalarm2_img": self.buyalarm2_img,
            "sellalarm1_img": self.sellalarm1_img,
            "successalarm_img": self.successalarm_img,
        }
        return dic

    # 버튼
    def BUTTONDIC(self):
        IMAGE = ImageList()
        IMAGES = IMAGE.IMAGEDIC()
        self.start_button = button.Button(650, 500, IMAGES["startbutton_img"], 0.5)
        self.howto_button = button.Button(650, 600, IMAGES["howtobutton_img"], 0.5)
        self.stock1_button = button.Button(30, 240, IMAGES["stock1_img"], 1)
        self.stock2_button = button.Button(30, 425, IMAGES["stock2_img"], 1)
        self.stock3_button = button.Button(30, 610, IMAGES["stock3_img"], 1)
        self.nextday_button = button.Button(1150, 650, IMAGES["nextday_img"], 1)
        self.sell_button = button.Button(1150, 540, IMAGES["sell_img"], 1)
        self.buy_button = button.Button(1150, 430, IMAGES["buy_img"], 1)
        self.decidebuy_button = button.Button(330, 510, IMAGES["decidebuy_img"], 0.7)
        self.decidesell_button = button.Button(330, 510, IMAGES["decidesell_img"], 0.7)
        self.sellten_button = button.Button(325, 325, IMAGES["ten_img"], 0.7)
        self.sellthr_button = button.Button(545, 325, IMAGES["thirty_img"], 0.7)
        self.sellfif_button = button.Button(765, 325, IMAGES["fifty_img"], 0.7)
        self.sellhund_button = button.Button(985, 325, IMAGES["hundred_img"], 0.7)
        self.buyten_button = button.Button(325, 355, IMAGES["ten_img"], 0.7)
        self.buythr_button = button.Button(545, 355, IMAGES["thirty_img"], 0.7)
        self.buyfif_button = button.Button(765, 355, IMAGES["fifty_img"], 0.7)
        self.buyhund_button = button.Button(985, 355, IMAGES["hundred_img"], 0.7)
        self.tradeall_button = button.Button(657, 420, IMAGES["tradeall_img"], 0.7)
        self.playagain_button = button.Button(300, 630, IMAGES["playagain_img"], 0.8)
        self.exitgame_button = button.Button(800, 630, IMAGES["exitgame_img"], 0.8)
        dic = {
            "start_button": self.start_button,
            "howto_button": self.howto_button,
            "stock1_button": self.stock1_button,
            "stock2_button": self.stock2_button,
            "stock3_button": self.stock3_button,
            "nextday_button": self.nextday_button,
            "sell_button": self.sell_button,
            "buy_button": self.buy_button,
            "decidebuy_button": self.decidebuy_button,
            "decidesell_button": self.decidesell_button,
            "sellten_button": self.sellten_button,
            "sellthr_button": self.sellthr_button,
            "sellfif_button": self.sellfif_button,
            "sellhund_button": self.sellhund_button,
            "buyten_button": self.buyten_button,
            "buythr_button": self.buythr_button,
            "buyfif_button": self.buyfif_button,
            "buyhund_button": self.buyhund_button,
            "tradeall_button": self.tradeall_button,
            "playagain_button": self.playagain_button,
            "exitgame_button": self.exitgame_button,
        }
        return dic
