#사운드 출처 https://www.bensound.com/

import pygame as pg
import matplotlib.pyplot as plt
import numpy as np
from pygame.time import get_ticks
import button, sys, stock, trade,time

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
size = [1500, 800]
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
pg.display.set_caption("주식 게임")

#사운드

bgm=pg.mixer.Sound("sound/bensound-ukulele.mp3")
main_sound=pg.mixer.Sound("sound/메인메뉴효과음.mp3")
menu_sound=pg.mixer.Sound("sound/메뉴클릭효과음.mp3")
fail_sound=pg.mixer.Sound("sound/매수매매실패효과음.mp3")
success_sound=pg.mixer.Sound("sound/매수매매성공효과음.mp3")
gameclear_sound=pg.mixer.Sound("sound/게임승리효과음.mp3")
gameover_sound=pg.mixer.Sound("sound/게임실패효과음.mp3")

# 이미지 #해결된 거 옆에 주석처리^^
mainmenu_img = pg.image.load('image/screen/메인화면.png') #
howtomenu_img = pg.image.load('image/screen/게임설명.png') #추후 수정
gamebg_img = pg.image.load('image/screen/게임화면.png') #
showbuy_img = pg.image.load('image/screen/매수창.png')#
gameclear_img = pg.image.load('image/screen/게임승리.png')
gameover_img = pg.image.load('image/screen/게임오버.png')

startbutton_img = pg.image.load('image/button/게임시작버튼.png')
howtobutton_img = pg.image.load('image/button/게임방법버튼.png')
cancelbutton_img = pg.image.load('image/button/취소버튼.png')#
sell_img = pg.image.load('image/button/매도버튼.png')#
nextday_img = pg.image.load('image/button/다음날로.png')#
ten_img = pg.image.load('image/button/10주.png')
thirty_img = pg.image.load('image/button/30주.png')
fifty_img = pg.image.load('image/button/50주.png')
hundred_img = pg.image.load('image/button/100주.png')
decidebuy_img = pg.image.load('image/button/매수결정.png')#
buy_img = pg.image.load('image/button/매수버튼.png')#
tradeall_img = pg.image.load('image/button/전체수량.png')#
playagain_img = pg.image.load('image/button/다시하기.png')
exitgame_img = pg.image.load('image/button/게임종료.png')

seedicon_img = pg.image.load('image/etc/시드머니아이콘.png')#
goal_img = pg.image.load('image/etc/목표자산.png')#
stock1_img = pg.image.load('image/etc/주식1.png')#
stock2_img = pg.image.load('image/etc/주식2.png')#
stock3_img = pg.image.load('image/etc/주식3.png')#
holdstock_img = pg.image.load('image/etc/주식보유량.png')#
tradevolume_img = pg.image.load('image/etc/거래량.png')#

#추가 이미지
sellalarm1_img=pg.image.load('image/etc/매도량알람1.png')
buyalarm1_img=pg.image.load('image/etc/매수량알람1.png')
sellalarm2_img=pg.image.load('image/etc/매도량알람2.png')
buyalarm2_img=pg.image.load('image/etc/매수량알람2.png')
sellalarm1_img=pg.image.load('image/etc/매도량알람2.png')
successalarm_img=pg.image.load('image/etc/거래성공알람.png')


# 버튼
start_button = button.Button(650, 500, startbutton_img, 0.5)#
howto_button = button.Button(650, 600, howtobutton_img, 0.5)#
stock1_button = button.Button(30, 240, stock1_img, 1)#
stock2_button = button.Button(30, 425, stock2_img, 1)#
stock3_button = button.Button(30, 610, stock3_img, 1)#

nextday_button = button.Button(1150, 650, nextday_img, 1)#
sell_button = button.Button(1150, 540, sell_img, 1)#
buy_button = button.Button(1150, 430, buy_img, 1)#
decide_button = button.Button(330, 540, decidebuy_img, 0.7)#

sellten_button = button.Button(325, 330, ten_img, 0.7)#
sellthr_button = button.Button(545, 330, thirty_img, 0.7)#
sellfif_button = button.Button(765, 330, fifty_img, 0.7)#
sellhund_button = button.Button(985, 330, hundred_img, 0.7)#
tradeall_button = button.Button(640, 420, tradeall_img, 0.8)#

playagain_button = button.Button(300, 550, playagain_img, 1)
exitgame_button = button.Button(800, 550, exitgame_img, 1)

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

trade1 = trade.Trade(('stock1'), stock1.price)
trade2 = trade.Trade(('stock2'), stock2.price)
trade3 = trade.Trade(('stock3'), stock3.price)

hold1 = trade1.dic.get('stockhold')
hold2 = trade2.dic.get('stockhold')
hold3 = trade3.dic.get('stockhold')

asset = int((seed) + (stock1.price) * hold1 +
            (stock2.price) * hold2 + (stock3.price) * hold3)
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
    img = pg.transform.scale(img, (w*scale, h*scale))
    screen.blit(img, [x, y])

def showinfo(stock, hold):
    updownrate = str(
        int(((stock.prices[nowdate - 1]) / (stock.prices[nowdate - 6]) - 1) * 100))
    imgdraw(holdstock_img, 280, 180, 1150, 240, 1)
    Writetext((str(str(hold) + '주')), 50, BLACK, 1200, 300)
    Writetext((str('주가: ' + str(int(stock.price)) + '원')), 50, BLACK, 640, 600)
    if float(updownrate) >= 0:
        Writetext(('(전일대비 +' + updownrate + '%)'), 50, BLACK, 640, 650)
    else:
        Writetext(('(전일대비 ' + updownrate + '%)'), 50, BLACK, 640, 650)


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
    asset = int((seed) + (stock1.price) * hold1 +
                (stock2.price) * hold2 + (stock3.price) * hold3)
    earning_rate = int(((asset / 1000000) - 1) * 100)


def savegraph(stock):
    plt.plot((date), (stock.prices))
    plt.savefig('image/figures/figure.png')

#주식창 열때 설정
def menuclick(stock):
    #global stockimg
    plt.cla()
    savegraph(stock)
    #stockimg = pg.image.load('image/figures/figure.png')
    return pg.image.load('image/figures/figure.png')

#주식 사거나 팔때 창 설정
def showtrade(volume):
    global game_menu, cancel_button
    game_menu = False
    imgdraw(showbuy_img, 900, 600, 300, 200-150, 1)
    imgdraw(tradevolume_img, 575, 115, 470, 180, 1)
    Writetext(volume, 50, WHITE, 520, 180)
    cancel_button = button.Button(850, 540, cancelbutton_img, 0.7)

def howmuch(volume):
    if sellten_button.draw(screen) == True:
        print("+10")
        menu_sound.play(0)
        volume += 10
    if sellthr_button.draw(screen) == True:
        print("+30")
        menu_sound.play(0)
        volume += 30
    if sellfif_button.draw(screen) == True:
        print("+50")
        menu_sound.play(0)
        volume += 50
    if sellhund_button.draw(screen) == True:
        print("+100")
        menu_sound.play(0)
        volume += 100
    return volume

def howmuchsell(sellvolume, hold):
    sellvolume = howmuch(sellvolume)
    if tradeall_button.draw(screen) == True:
        sellvolume = hold
    return sellvolume

def buydecide(price,buyvolume,hold):
    global game_menu,seed
    game_menu=False
    t=0
    if decide_button.draw(screen) == True:
        if seed <= price * buyvolume:
            buyvolume = 0
            imgdraw(buyalarm1_img, 400, 150, 480, 600, 1)
            fail_sound.play(0)

        elif buyvolume == 0:
            imgdraw(buyalarm2_img, 400, 150, 480, 600, 1)
            fail_sound.play(0)
        
        else:
            seed -= price * buyvolume
            hold += buyvolume
            imgdraw(successalarm_img, 400, 150, 480, 600, 1)
            success_sound.play(0)
            Writetext(str(int(seed)), 50, WHITE, 200, 70)
        buyvolume=0
    
    return [buyvolume, hold]

def selldecide(price,sellvolume,hold):
    global game_menu,seed,sell_menu1
    t=0
    game_menu = False
    if decide_button.draw(screen) == True:
        if hold < sellvolume:            
            imgdraw(sellalarm1_img, 400, 150, 480, 600, 1)
            fail_sound.play(0)
            
        elif sellvolume == 0:
            fail_sound.play(0)
            imgdraw(sellalarm2_img, 400, 150, 480, 600, 1)
        
        else:
            seed += price * sellvolume
            hold -= sellvolume
            imgdraw(successalarm_img, 400, 150, 480, 600, 1)
            success_sound.play(0)
            Writetext(str(int(seed)), 50, WHITE, 200, 70)
        sellvolume = 0
    
    return [sellvolume, hold] 


# 게임 시작 전 주식을 10번 fluctuation함으로써 그래프를 만드는 작업.
for i in range(10):
    plusdate()
    appenddate()
    stock1.fluctuation()
    stock2.fluctuation()
    stock3.fluctuation()

#배경음악 설정
bgm.play(-1)
bgm.set_volume(0.25)

while run:

    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.flip()

    if main_menu == True:
        imgdraw(mainmenu_img, 1500, 800, 0, 0, 1)
        if start_button.draw(screen) == True:
            print('GAME START')
            main_sound.play(0)
            main_menu = False
            game_menu = True

        if howto_button.draw(screen) == True:
            print('HOW TO PLAY THE GAME')
            main_sound.play(0)
            main_menu = False
            howto_menu = True

    if howto_menu == True:
        screen.blit(howtomenu_img, (0, 0))
        start_button = button.Button(1200, 600, startbutton_img, 0.5)
        if start_button.draw(screen) == True:
            print('GAME START')
            main_sound.play(0)
            howto_menu = False
            game_menu = True

    if game_menu == True:
        imgdraw(gamebg_img, 1500, 800, 0, 0, 1)
        imgdraw(seedicon_img, 400, 100, 5, 60, 1)
        Writetext(str(int(seed)), 50, WHITE, 170, 70)
        Writetext(('수익률: '+ str(earning_rate) + '%'), 50, WHITE, 500, 70)
        imgdraw(goal_img, 450, 100, 1025, 60, 1)
        Writetext(str(goal), 50, WHITE, 1220, 73)
        cancel_button = button.Button(720, 720, cancelbutton_img, 0.5)

# 다음날로 가는 버튼
        if (nextday_button.draw(screen) == True):
            print('NEXT DAY')
            menu_sound.play(0)
            nextday()

# 메뉴 1 클릭
        if stock1_button.draw(screen) == True:
            menu_sound.play(0)                
            print("stock1")
            stockimg=menuclick(stock1)
            stock2_menu = False
            stock3_menu = False
            stock_menu1 = True
            game_menu=True

        if stock_menu1 == True:
            showinfo(stock1, hold1)
            imgdraw(stockimg, 640, 480, 650, 250, 0.7)  # 크기나 위치 수정 필요

            if cancel_button.draw(screen) == True:
                menu_sound.play(0)
                if buy_menu1 == True:
                    False
                else:
                    stock_menu1 = False
                    plt.cla()

            if sell_button.draw(screen) == True:
                menu_sound.play(0)
                print("show_win1")
                sell_menu1 = True

            if buy_button.draw(screen) == True:
                menu_sound.play(0)
                print("show_win1")
                buy_menu1 = True

# 메뉴 2 클릭
        if stock2_button.draw(screen) == True:
            menu_sound.play(0)
            print("stock2")
            stockimg=menuclick(stock2)
            stock_menu1 = False
            stock_menu3 = False
            stock_menu2 = True

        if stock_menu2 == True:
            showinfo(stock2, hold2)
            imgdraw(stockimg, 640, 480, 650, 250, 0.7)
            if cancel_button.draw(screen) == True:
                menu_sound.play(0)        
                if buy_menu2 == True:
                    False
                else:
                    stock_menu2 = False
                    plt.cla()

            if sell_button.draw(screen) == True:
                menu_sound.play(0)        
                print("show_win2")
                sell_menu2 = True

            if buy_button.draw(screen) == True:
                menu_sound.play(0)        
                print("show_win2")
                buy_menu2 = True

# 메뉴 3 클릭
        if stock3_button.draw(screen) == True:
            menu_sound.play(0)        
            print("stock3")
            stockimg=menuclick(stock3)
            stock_menu1 = False
            stock_menu2 = False
            stock_menu3 = True

        if stock_menu3 == True:
            showinfo(stock3, hold3)
            imgdraw(stockimg, 640, 480, 650, 250, 0.7)
            if cancel_button.draw(screen) == True:
                if buy_menu3 == True:
                    False
                else:
                    stock_menu3 = False
                    plt.cla()

            if sell_button.draw(screen) == True:
                menu_sound.play(0)        
                print("show_win3")
                sell_menu3 = True

            if buy_button.draw(screen) == True:
                menu_sound.play(0)        
                print("show_win3")
                buy_menu3 = True

# 주식1 매수창
    if buy_menu1 == True:
        showtrade(buyvolume1)
        buyvolume1 = howmuch(buyvolume1)
        l=buydecide(stock1.price,buyvolume1,hold1)
        buyvolume1=l[0]
        hold1=l[1]

        if cancel_button.draw(screen) == True:
            menu_sound.play(0)        
            buy_menu1 = False
            game_menu = True
            buyvolume1 = 0

# 주식2 매수창
    if buy_menu2 == True:
        showtrade(buyvolume2)
        buyvolume2 = howmuch(buyvolume2)
        l=buydecide(stock2.price,buyvolume2,hold2)
        buyvolume2=l[0]
        hold2=l[1]

        if cancel_button.draw(screen) == True:
            menu_sound.play(0)        
            buy_menu2 = False
            game_menu = True
            buyvolume2 = 0

# 주식3 매수창
    if buy_menu3 == True:
        showtrade(buyvolume3)
        buyvolume3 = howmuch(buyvolume3)
        l=buydecide(stock3.price,buyvolume3,hold3)
        buyvolume3=l[0]
        hold3=l[1]

        if cancel_button.draw(screen) == True:
            menu_sound.play(0)        
            buy_menu3 = False
            game_menu = True
            buyvolume3 = 0

# 주식1 매도창
    if sell_menu1 == True:
        showtrade(sellvolume1)
        sellvolume1 = howmuchsell(sellvolume1, hold1)
        l=selldecide(stock1.price,sellvolume1,hold1)
        sellvolume1=l[0]
        hold1=l[1]

        if cancel_button.draw(screen) == True:
            sell_menu1 = False
            game_menu = True
            sellvolume1 = 0


# 주식2 매도창
    if sell_menu2 == True:
        showtrade(sellvolume2)
        sellvolume2 = howmuchsell(sellvolume2, hold2)
        l=selldecide(stock2.price,sellvolume2,hold2)
        sellvolume2=l[0]
        hold2=l[1]

        if cancel_button.draw(screen) == True:
            sell_menu2 = False
            game_menu = True
            sellvolume2 = 0

# 주식3 매도창
    if sell_menu3 == True:
        showtrade(sellvolume3)
        sellvolume3 = howmuchsell(sellvolume3, hold3)
        l=selldecide(stock3.price,sellvolume3,hold3)
        sellvolume3=l[0]
        hold3=l[1]

        if cancel_button.draw(screen) == True:
            sell_menu3 = False
            game_menu = True
            sellvolume3 = 0

# 게임 종료
    if seed >= goal:
        gameclear_sound.play(0)
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
        if gameclear_menu == True:
            imgdraw(gameclear_img, 1500, 800, 0, 0, 1)
            Writetext((str(int(seed)) + '원'), 60, BLACK, 700, 385)
            if playagain_button.draw(screen) == True:
                print('play again')
                seed = 1000000
                goal = 5000000
                date = [1]
                nowdate = 1

                stock1 = stock.Stock(3000)
                stock2 = stock.Stock(5000)
                stock3 = stock.Stock(10000)

                trade1 = trade.Trade(('stock1'), stock1.price)
                trade2 = trade.Trade(('stock2'), stock2.price)
                trade3 = trade.Trade(('stock3'), stock3.price)

                hold1 = trade1.dic.get('stockhold')
                hold2 = trade2.dic.get('stockhold')
                hold3 = trade3.dic.get('stockhold')

                asset = int((seed) + (stock1.price) * hold1 +
                            (stock2.price) * hold2 + (stock3.price) * hold3)
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
            elif exitgame_button.draw(screen) == True:
                pg.quit()

    elif seed <= 0:
        gameover_sound.play(0)
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
        gameover_menu = True
        if gameover_menu == True:
            imgdraw(gameover_img, 1500, 800, 0, 0, 1)

            if playagain_button.draw(screen) == True:
                print('play again')
                seed = 1000000
                goal = 5000000
                date = [1]
                nowdate = 1

                stock1 = stock.Stock(3000)
                stock2 = stock.Stock(5000)
                stock3 = stock.Stock(10000)

                trade1 = trade.Trade(('stock1'), stock1.price)
                trade2 = trade.Trade(('stock2'), stock2.price)
                trade3 = trade.Trade(('stock3'), stock3.price)

                hold1 = trade1.dic.get('stockhold')
                hold2 = trade2.dic.get('stockhold')
                hold3 = trade3.dic.get('stockhold')

                asset = int((seed) + (stock1.price) * hold1 +
                            (stock2.price) * hold2 + (stock3.price) * hold3)
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
            elif exitgame_button.draw(screen) == True:
                pg.quit()     

pg.quit()
