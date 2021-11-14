# 사운드 출처 https://www.bensound.com/

import pygame as pg
import matplotlib.pyplot as plt
import numpy as np
from pygame.time import get_ticks
import button, sys, stock, trade, img

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
size = [1500, 800]
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
pg.display.set_caption("주식 게임")
Imagedic = img.ImageList()
imagedic = Imagedic.IMAGEDIC()
buttondic = Imagedic.BUTTONDIC()

# 사운드

bgm = pg.mixer.Sound("sound/bensound-ukulele.mp3")
main_sound = pg.mixer.Sound("sound/메인메뉴효과음.mp3")
menu_sound = pg.mixer.Sound("sound/메뉴클릭효과음.mp3")
fail_sound = pg.mixer.Sound("sound/매수매매실패효과음.mp3")
success_sound = pg.mixer.Sound("sound/매수매매성공효과음.mp3")
gameclear_sound = pg.mixer.Sound("sound/게임승리효과음.mp3")
gameover_sound = pg.mixer.Sound("sound/게임실패효과음.mp3")

# game 화면 실행 변수들
main_menu = True
run = True
game_menu = False
howto_menu = False
stock_menu1 = False
stock_menu2 = False
stock_menu3 = False
buy_menu1 = False
buy_menu2 = False
buy_menu3 = False
sell_menu1 = False
sell_menu2 = False
sell_menu3 = False
gameover_menu = False
gameclear_menu = False

# 유저 초기 정보
seed = 1000000
goal = 5000000
date = [1]
nowdate = 1

stock1 = stock.Stock(3000)
stock2 = stock.Stock(5000)
stock3 = stock.Stock(10000)

trade1 = trade.Trade(("stock1"), stock1.price)
trade2 = trade.Trade(("stock2"), stock2.price)
trade3 = trade.Trade(("stock3"), stock3.price)

hold1 = trade1.dic.get("stockhold")
hold2 = trade2.dic.get("stockhold")
hold3 = trade3.dic.get("stockhold")

asset = int(
    (seed) + (stock1.price) * hold1 + (stock2.price) * hold2 + (stock3.price) * hold3
)
earning_rate = int(((asset / 1000000) - 1) * 100)

buyvolume1 = 0
buyvolume2 = 0
buyvolume3 = 0
sellvolume1 = 0
sellvolume2 = 0
sellvolume3 = 0


# 함수


def Writetext(text, fontsize, color, x, y):
    if str(text).isdigit() == True:
        text = str(text)
    site = (x, y)
    font = pg.font.SysFont("malgungothic", fontsize)
    text = font.render(text, True, color)
    screen.blit(text, site)


def imgdraw(img, w, h, x, y, scale):
    img = pg.transform.scale(img, (w * scale, h * scale))
    screen.blit(img, [x, y])


def showhold(hold):
    imgdraw(imagedic["holdstock_img"], 280, 180, 1150, 240, 1)
    Writetext((str(str(hold) + "주")), 50, BLACK, 1200, 300)


def showinfo(stock):
    updownrate = str(
        int(((stock.prices[nowdate - 1]) / (stock.prices[nowdate - 6]) - 1) * 100)
    )
    Writetext((str("주가: " + str(int(stock.price)) + "원")), 50, BLACK, 640, 600)
    if float(updownrate) >= 0:
        Writetext(("(전일대비 +" + updownrate + "%)"), 50, BLACK, 640, 650)
    else:
        Writetext(("(전일대비 " + updownrate + "%)"), 50, BLACK, 640, 650)


def appenddate():
    date.append(nowdate)


def plusdate():
    global nowdate
    nowdate += 1


def nextday():
    global seed, asset, earning_rate
    for i in range(5):
        plusdate()
        appenddate()
        stock1.fluctuation()
        stock2.fluctuation()
        stock3.fluctuation()
    seed -= 50000
    asset = int(
        (seed)
        + (stock1.price) * hold1
        + (stock2.price) * hold2
        + (stock3.price) * hold3
    )
    earning_rate = int(((asset / 1000000) - 1) * 100)


def savegraph(stock):
    plt.plot((date), (stock.prices))
    plt.savefig("image/figures/figure.png")


# 주식창 열때 설정
def menuclick(stock):
    plt.cla()
    savegraph(stock)
    return pg.image.load("image/figures/figure.png")


# 주식 사거나 팔때 창 설정
def showtrade(volume):
    global game_menu, cancel_button
    game_menu = False
    imgdraw(imagedic["showbuy_img"], 900, 600, 300, 200 - 150, 1)
    imgdraw(imagedic["tradevolume_img"], 575, 115, 470, 180, 1)
    Writetext(volume, 50, WHITE, 510, 200)
    cancel_button = button.Button(850, 540, imagedic["cancelbutton_img"], 0.7)


def howmuch(volume):
    if buttondic["sellten_button"].draw(screen) == True:
        menu_sound.play(0)
        volume += 10
    if buttondic["sellthr_button"].draw(screen) == True:
        menu_sound.play(0)
        volume += 30
    if buttondic["sellfif_button"].draw(screen) == True:
        menu_sound.play(0)
        volume += 50
    if buttondic["sellhund_button"].draw(screen) == True:
        menu_sound.play(0)
        volume += 100
    return volume


def howmuchsell(sellvolume, hold):
    sellvolume = howmuch(sellvolume)
    if buttondic["tradeall_button"].draw(screen) == True:
        sellvolume = hold
    return sellvolume


def buydecide(price, buyvolume, hold):
    global game_menu, seed, buy_menu1, stock1
    game_menu = False
    if buttondic["decidebuy_button"].draw(screen) == True:
        if seed <= price * buyvolume:
            buyvolume = 0
            imgdraw(imagedic["buyalarm1_img"], 400, 150, 580, 660, 0.8)
            fail_sound.play(0)

        elif buyvolume == 0:
            imgdraw(imagedic["buyalarm2_img"], 400, 150, 580, 660, 0.8)
            fail_sound.play(0)
        else:
            seed -= price * buyvolume
            hold += buyvolume
            game_menu = True
            success_sound.play(0)
            imgdraw(imagedic["successalarm_img"], 400, 150, 580, 660, 0.8)
        buyvolume = 0
    return [buyvolume, hold]


def selldecide(price, sellvolume, hold):
    global game_menu, seed, sell_menu1
    game_menu = False
    if buttondic["decidesell_button"].draw(screen) == True:
        if hold < sellvolume:
            imgdraw(imagedic["sellalarm1_img"], 400, 150, 580, 660, 0.8)
            fail_sound.play(0)

        elif sellvolume == 0:
            fail_sound.play(0)
            imgdraw(imagedic["sellalarm2_img"], 400, 150, 580, 660, 0.8)

        else:
            seed += price * sellvolume
            hold -= sellvolume
            game_menu = True
            imgdraw(imagedic["successalarm_img"], 400, 150, 580, 660, 0.8)
            success_sound.play(0)
        sellvolume = 0
    return [sellvolume, hold]


# 게임 시작 전 주식을 10번 fluctuation함으로써 그래프를 만드는 작업.
for i in range(10):
    plusdate()
    appenddate()
    stock1.fluctuation()
    stock2.fluctuation()
    stock3.fluctuation()

# 배경음악 설정
bgm.set_volume(0.25)
bgm.play(-1)

while run:

    clock.tick(60)
    mouse = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.flip()

    if main_menu == True:
        imgdraw(imagedic["mainmenu_img"], 1500, 800, 0, 0, 1)
        if buttondic["start_button"].draw(screen) == True:
            main_sound.play(0)
            main_menu = False
            game_menu = True

        if buttondic["howto_button"].draw(screen) == True:
            main_sound.play(0)
            main_menu = False
            howto_menu = True

    if howto_menu == True:
        screen.blit(imagedic["howtomenu_img"], (0, 0))
        start_button = button.Button(1200, 600, imagedic["startbutton_img"], 0.5)
        if start_button.draw(screen) == True:
            main_sound.play(0)
            howto_menu = False
            game_menu = True

    if game_menu == True:
        if (
            buy_menu1
            or buy_menu2
            or buy_menu3
            or sell_menu1
            or sell_menu2
            or sell_menu3
        ) == False:
            imgdraw(imagedic["gamebg_img"], 1500, 800, 0, 0, 1)
        Writetext(("수익률: " + str(earning_rate) + "%"), 50, WHITE, 500, 70)
        imgdraw(imagedic["seedicon_img"], 400, 100, 5, 60, 1)
        if seed <= 50000:
            Writetext(str(int(seed)), 50, RED, 170, 70)
        else:
            Writetext(str(int(seed)), 50, WHITE, 170, 70)
        imgdraw(imagedic["goal_img"], 450, 100, 1025, 60, 1)
        Writetext(str(goal), 50, WHITE, 1220, 73)
        cancel_button = button.Button(720, 720, imagedic["cancelbutton_img"], 0.5)

        # 다음날로 가는 버튼
        if buttondic["nextday_button"].draw(screen) == True:
            menu_sound.play(0)
            nextday()

        # 메뉴 1 클릭
        if buttondic["stock1_button"].draw(screen) == True:
            menu_sound.play(0)
            stockimg = menuclick(stock1)
            stock_menu2 = False
            stock_menu3 = False
            stock_menu1 = True

        if stock_menu1 == True:
            showhold(hold1)
            if (buy_menu1 or sell_menu1) == False:
                showinfo(stock1)
                if cancel_button.draw(screen) == True:
                    menu_sound.play(0)
                    if buy_menu1 == True:
                        False
                    else:
                        stock_menu1 = False
                        plt.cla()
            imgdraw(stockimg, 640, 480, 650, 250, 0.7)  # 크기나 위치 수정 필요
            if buttondic["sell_button"].draw(screen) == True:
                menu_sound.play(0)

                sell_menu1 = True

            if buttondic["buy_button"].draw(screen) == True:
                menu_sound.play(0)
                buy_menu1 = True

        # 메뉴 2 클릭
        if buttondic["stock2_button"].draw(screen) == True:
            menu_sound.play(0)
            stockimg = menuclick(stock2)
            stock_menu1 = False
            stock_menu3 = False
            stock_menu2 = True

        if stock_menu2 == True:
            showhold(hold2)
            if (buy_menu2 or sell_menu2) == False:
                showinfo(stock2)
                if cancel_button.draw(screen) == True:
                    menu_sound.play(0)
                    if buy_menu2 == True:
                        False
                    else:
                        stock_menu2 = False
                        plt.cla()
            imgdraw(stockimg, 640, 480, 650, 250, 0.7)

            if buttondic["sell_button"].draw(screen) == True:
                menu_sound.play(0)
                # print("show_win2")
                sell_menu2 = True

            if buttondic["buy_button"].draw(screen) == True:
                menu_sound.play(0)
                buy_menu2 = True

        # 메뉴 3 클릭
        if buttondic["stock3_button"].draw(screen) == True:
            menu_sound.play(0)
            stockimg = menuclick(stock3)
            stock_menu1 = False
            stock_menu2 = False
            stock_menu3 = True

        if stock_menu3 == True:
            showhold(hold3)
            if (buy_menu3 or sell_menu3) == False:
                showinfo(stock3)
                if cancel_button.draw(screen) == True:
                    menu_sound.play(0)
                    if buy_menu2 == True:
                        False
                    else:
                        stock_menu2 = False
                        plt.cla()
            imgdraw(stockimg, 640, 480, 650, 250, 0.7)

            if buttondic["sell_button"].draw(screen) == True:
                menu_sound.play(0)
                sell_menu3 = True

            if buttondic["buy_button"].draw(screen) == True:
                menu_sound.play(0)
                buy_menu3 = True

    # 주식1 매수창
    if buy_menu1 == True:
        showtrade(buyvolume1)
        buyvolume1 = howmuch(buyvolume1)
        l = buydecide(stock1.price, buyvolume1, hold1)
        buyvolume1 = l[0]
        hold1 = l[1]
        d = pg.time.delay(10)
        if cancel_button.draw(screen) == True:
            menu_sound.play(0)
            buy_menu1 = False
            game_menu = True
            buyvolume1 = 0

    # 주식2 매수창
    if buy_menu2 == True:
        showtrade(buyvolume2)
        buyvolume2 = howmuch(buyvolume2)
        l = buydecide(stock2.price, buyvolume2, hold2)
        buyvolume2 = l[0]
        hold2 = l[1]

        if cancel_button.draw(screen) == True:
            menu_sound.play(0)
            buy_menu2 = False
            game_menu = True
            buyvolume2 = 0

    # 주식3 매수창
    if buy_menu3 == True:
        showtrade(buyvolume3)
        buyvolume3 = howmuch(buyvolume3)
        l = buydecide(stock3.price, buyvolume3, hold3)
        buyvolume3 = l[0]
        hold3 = l[1]

        if cancel_button.draw(screen) == True:
            menu_sound.play(0)
            buy_menu3 = False
            game_menu = True
            buyvolume3 = 0

    # 주식1 매도창
    if sell_menu1 == True:
        showtrade(sellvolume1)
        sellvolume1 = howmuchsell(sellvolume1, hold1)
        l = selldecide(stock1.price, sellvolume1, hold1)
        sellvolume1 = l[0]
        hold1 = l[1]

        if cancel_button.draw(screen) == True:
            sell_menu1 = False
            game_menu = True
            sellvolume1 = 0

    # 주식2 매도창
    if sell_menu2 == True:
        showtrade(sellvolume2)
        sellvolume2 = howmuchsell(sellvolume2, hold2)
        l = selldecide(stock2.price, sellvolume2, hold2)
        sellvolume2 = l[0]
        hold2 = l[1]

        if cancel_button.draw(screen) == True:
            sell_menu2 = False
            game_menu = True
            sellvolume2 = 0

    # 주식3 매도창
    if sell_menu3 == True:
        showtrade(sellvolume3)
        sellvolume3 = howmuchsell(sellvolume3, hold3)
        l = selldecide(stock3.price, sellvolume3, hold3)
        sellvolume3 = l[0]
        hold3 = l[1]

        if cancel_button.draw(screen) == True:
            sell_menu3 = False
            game_menu = True
            sellvolume3 = 0

    # 게임 종료
    if seed >= goal:
        bgm.stop()
        gameclear_sound.play()
        screen.fill(BLACK)
        game_menu = False
        howto_menu = False
        stock_menu1 = False
        stock_menu2 = False
        stock_menu3 = False
        buy_menu1 = False
        buy_menu2 = False
        buy_menu3 = False
        sell_menu1 = False
        sell_menu2 = False
        sell_menu3 = False
        gameclear_menu = True
        imgdraw(imagedic["gameclear_img"], 1500, 800, 0, 0, 1)
    if gameclear_menu == True:
        Writetext((str(int(asset)) + "원 (+" + str(earning_rate) + "%)"), 80, BLACK, 585, 355)
        seed = 1000000
        if buttondic["playagain_button"].draw(screen) == True:
            gameclear_sound.stop()
            bgm.play(-1)
            seed = 1000000
            goal = 5000000
            date = [1]
            nowdate = 1

            stock1 = stock.Stock(3000)
            stock2 = stock.Stock(5000)
            stock3 = stock.Stock(10000)

            trade1 = trade.Trade(("stock1"), stock1.price)
            trade2 = trade.Trade(("stock2"), stock2.price)
            trade3 = trade.Trade(("stock3"), stock3.price)

            hold1 = trade1.dic.get("stockhold")
            hold2 = trade2.dic.get("stockhold")
            hold3 = trade3.dic.get("stockhold")

            asset = int(
                (seed)
                + (stock1.price) * hold1
                + (stock2.price) * hold2
                + (stock3.price) * hold3
            )
            earning_rate = int(((asset / 1000000) - 1) * 100)

            buyvolume1 = 0
            buyvolume2 = 0
            buyvolume3 = 0
            sellvolume1 = 0
            sellvolume2 = 0
            sellvolume3 = 0
            for i in range(10):
                plusdate()
                appenddate()
                stock1.fluctuation()
                stock2.fluctuation()
                stock3.fluctuation()
            gameclear_menu = False
            game_menu = True
        elif buttondic["exitgame_button"].draw(screen) == True:
            pg.quit()

    elif seed <= 0:
        bgm.stop()
        gameover_sound.play()
        gameover_menu = True

    if gameover_menu == True:
        seed = 1000000
        game_menu = False
        howto_menu = False
        stock_menu1 = False
        stock_menu2 = False
        stock_menu3 = False
        buy_menu1 = False
        buy_menu2 = False
        buy_menu3 = False
        sell_menu1 = False
        sell_menu2 = False
        sell_menu3 = False
        screen.fill(BLACK)
        imgdraw(imagedic["gameover_img"], 1500, 800, 0, 0, 1)
        pg.time.delay(60)
        if buttondic["playagain_button"].draw(screen) == True:
            gameover_sound.stop()
            bgm.play(-1)
            goal = 5000000
            date = [1]
            nowdate = 1

            stock1 = stock.Stock(3000)
            stock2 = stock.Stock(5000)
            stock3 = stock.Stock(10000)

            trade1 = trade.Trade(("stock1"), stock1.price)
            trade2 = trade.Trade(("stock2"), stock2.price)
            trade3 = trade.Trade(("stock3"), stock3.price)

            hold1 = trade1.dic.get("stockhold")
            hold2 = trade2.dic.get("stockhold")
            hold3 = trade3.dic.get("stockhold")

            asset = int(
                (seed)
                + (stock1.price) * hold1
                + (stock2.price) * hold2
                + (stock3.price) * hold3
            )
            earning_rate = int(((asset / 1000000) - 1) * 100)

            buyvolume1 = 0
            buyvolume2 = 0
            buyvolume3 = 0
            sellvolume1 = 0
            sellvolume2 = 0
            sellvolume3 = 0
            for i in range(10):
                plusdate()
                appenddate()
                stock1.fluctuation()
                stock2.fluctuation()
                stock3.fluctuation()
            gameover_menu = False
            game_menu = True
        elif buttondic["exitgame_button"].draw(screen) == True:
            pg.quit()
pg.quit()
