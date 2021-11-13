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
#사운드 출처 https://www.bensound.com/

bgm=pg.mixer.Sound("sound/bensound-ukulele.mp3")
main_sound=pg.mixer.Sound("sound/메인메뉴효과음.mp3")
menu_sound=pg.mixer.Sound("sound/메뉴클릭효과음.mp3")
fail_sound=pg.mixer.Sound("sound/매수매매실패효과음.mp3")
succese_sound=pg.mixer.Sound("sound/매수매매성공효과음.mp3")
gameclear_sound=pg.mixer.Sound("sound/게임승리효과음.mp3")
gameover_sound=pg.mixer.Sound("sound/게임실패효과음.mp3")

# 이미지
mainmenu_img = pg.image.load('image/screen/메인화면.png')
howtomenu_img = pg.image.load('image/screen/게임설명.png')
gamebg_img = pg.image.load('image/screen/게임화면.png')
showbuy_img = pg.image.load('image/screen/매수창.png')
show_img = pg.image.load('image/screen/창.png')
stockbox_img = pg.image.load('image/screen/주식박스.png')
gameclear_img = pg.image.load('image/screen/게임승리.png')
gameover_img = pg.image.load('image/screen/게임오버.png')

startbutton_img = pg.image.load('image/button/게임시작버튼.png')
howtobutton_img = pg.image.load('image/button/게임방법버튼.png')
cancelbutton_img = pg.image.load('image/button/취소버튼.png')
sell_img = pg.image.load('image/button/매도버튼.png')
nextday_img = pg.image.load('image/button/다음날로.png')
ten_img = pg.image.load('image/button/10주.png')
thirty_img = pg.image.load('image/button/30주.png')
fifty_img = pg.image.load('image/button/50주.png')
hundred_img = pg.image.load('image/button/100주.png')
decidebuy_img = pg.image.load('image/button/매수결정.png')
buy_img = pg.image.load('image/button/매수버튼.png')
tradeall_img = pg.image.load('image/button/전체수량.png')
playagain_img = pg.image.load('image/button/다시하기.png')
exitgame_img = pg.image.load('image/button/게임종료.png')

seedicon_img = pg.image.load('image/etc/시드머니아이콘.png')
goal_img = pg.image.load('image/etc/목표자산.png')
seedicon_img = pg.image.load('image/etc/시드머니아이콘.png')
stock1_img = pg.image.load('image/etc/주식1.png')
stock2_img = pg.image.load('image/etc/주식2.png')
stock3_img = pg.image.load('image/etc/주식3.png')
holdstock_img = pg.image.load('image/etc/주식보유량.png')
tradevolume_img = pg.image.load('image/etc/거래량.png')

# 버튼
start_button = button.Button(650, 500, startbutton_img, 0.5)
howto_button = button.Button(650, 600, howtobutton_img, 0.5)
stock1_button = button.Button(80, 380, stock1_img, 1)
stock2_button = button.Button(80, 500, stock2_img, 1)
stock3_button = button.Button(80, 620, stock3_img, 1)

nextday_button = button.Button(1100, 650, nextday_img, 1)
sell_button = button.Button(1125, 570, sell_img, 1)
buy_button = button.Button(1125, 440, buy_img, 1)
decide_button = button.Button(350, 600, decidebuy_img, 0.7)

sellten_button = button.Button(320, 350, ten_img, 1)
sellthr_button = button.Button(540, 350, thirty_img, 1)
sellfif_button = button.Button(760, 350, fifty_img, 1)
sellhund_button = button.Button(980, 350, hundred_img, 1)
tradeall_button = button.Button(650, 470, tradeall_img, 1)

playagain_button = button.Button(400, 550, playagain_img, 1)
exitgame_button = button.Button(900, 550, exitgame_img, 1)

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
    imgdraw(show_img, 830, 570, 600, 200, 1)
    imgdraw(holdstock_img, 280, 180, 1125, 230, 1)
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


def menuclick(stock):
    global stockimg
    plt.cla()
    savegraph(stock)
    stockimg = pg.image.load('image/figures/figure.png')


def showtrade(volume):
    global game_menu, cancel_button
    game_menu = False
    imgdraw(showbuy_img, 900, 600, 300, 100, 1)
    imgdraw(tradevolume_img, 575, 115, 480, 200, 1)
    Writetext(volume, 50, WHITE, 570, 220)
    cancel_button = button.Button(850, 600, cancelbutton_img, 0.7)

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
    if decide_button.draw(screen) == True:
        if seed <= price * buyvolume:
            Writetext(('돈이 부족합니다.'), 50, WHITE, 570, 500)
            fail_sound.play(0)
            buyvolume = 0
        
        elif buyvolume == 0:
            Writetext(('매수량이 0입니다.'), 50, WHITE, 570, 500)
            fail_sound.play(0)
        
        else:
            seed -= price * buyvolume
            hold += buyvolume
            Writetext(('거래 완료'), 50, WHITE, 570, 500)
            succese_sound.play(0)
            buyvolume = 0          
            Writetext(str(int(seed)), 50, WHITE, 200, 70)
    
    return [buyvolume, hold]

def selldecide(price,sellvolume,hold):
    global game_menu,seed
    game_menu = False
    if decide_button.draw(screen) == True:
        if hold < sellvolume:
            Writetext(('주식 보유량이 부족합니다.'), 50, WHITE, 570, 220)
            fail_sound.play(0)
            sellvolume = 0
            
        elif sellvolume == 0:
            Writetext(('매도량이 0입니다.'), 50, WHITE, 570, 220)
            fail_sound.play(0)
        
        else:
            seed += price * sellvolume
            hold -= sellvolume
            Writetext(('거래 완료'), 50, WHITE, 570, 220)
            succese_sound.play(0)
            sellvolume = 0
            Writetext(str(int(seed)), 50, WHITE, 200, 70)

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
        imgdraw(goal_img, 400, 100, 1025, 60, 1)
        Writetext(str(goal), 50, WHITE, 1200, 70)
        imgdraw(stockbox_img, 500, 570, 70, 200, 1)
        cancel_button = button.Button(1180, 700, cancelbutton_img, 0.5)

# 다음날로 가는 버튼
        if (nextday_button.draw(screen) == True) and (stock_menu1 == False) and (stock_menu2 == False) and (stock_menu3 == False):
            print('NEXT DAY')
            menu_sound.play(0)
            nextday()
# 메뉴 1 클릭
        if stock1_button.draw(screen) == True:
            menu_sound.play(0)                
            print("stock1")
            menuclick(stock1)
            stock2_menu = False
            stock3_menu = False
            stock_menu1 = True

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
            menuclick(stock1)
            stock_menu1 = False
            stock_menu3 = False
            stock_menu2 = stock2

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
            menuclick()
            stock_menu1 = False
            stock_menu2 = False
            stock_menu3 = stock3

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
            gameclear_sound.play(0)
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
            gameover_sound.play(0)
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