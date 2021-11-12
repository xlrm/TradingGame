import pygame as pg
import matplotlib.pyplot as plt
import numpy as np
import button, sys, stock, trade

pg.init()

WHITE= (255,255,255)
BLACK=(0,0,0)
size  = [1500,800]
screen= pg.display.set_mode(size)
clock = pg.time.Clock()

#text 생성해서 화면에 표시하는 함수
def Writetext(text,fontsize,color,x,y):        #문자열,폰트크기,생성할 위치
    if str(text).isdigit()==True:
        text=str(text)
    site=(x,y)                         
    font=pg.font.SysFont("malgungothic",fontsize)
    text=font.render(text,True, color)
    screen.blit(text,site)

def imgdraw(img,w,h,x,y,scale):
    pg.transform.scale(img,(w*scale,h*scale))
    screen.blit(img,[x,y])

def showinfo(hold):                          #메뉴 클릭시 정보 보여주는 창
    imgdraw(show_img,830,570,600,200,1)      #나중에 주식 보유량 넣어주시면 됩니다
    imgdraw(holdstock_img,280,180,1125,230,1)#나중에 수익률을 넣을 때 고치겠습니다
    Writetext(hold,50,BLACK,1200,300)

pg.display.set_caption("주식 게임")

#이미지
mainmenu_img = pg.image.load('image\메인화면.png')
howtomenu_img= pg.image.load('image\게임설명.png')
gamebg_img=pg.image.load('image\게임화면.png')
entervolume_img = pg.image.load('image\개수입력.png')

startbutton_img = pg.image.load('image\게임시작버튼.png')
howtobutton_img = pg.image.load('image\게임방법버튼.png')
cancelbutton_img = pg.image.load('image\취소버튼.png')

gamebg_img=pg.image.load('image\게임화면.png')
seedicon_img = pg.image.load('image\시드머니아이콘.png')
goal_img=pg.image.load('image\목표자산.png')

seedicon_img = pg.image.load('image\시드머니아이콘.png')
goal_img=pg.image.load('image\목표자산.png')

stockbox_img=pg.image.load('image\주식박스.png')
stock1_img=pg.image.load('image\주식1.png')
stock2_img=pg.image.load('image\주식2.png')
stock3_img=pg.image.load('image\주식3.png')

show_img=pg.image.load('image\창.png')

sell_img=pg.image.load('image\매도버튼.png')
buy_img=pg.image.load('image\매수버튼.png')
nextday_img=pg.image.load('image\다음날로.png')
holdstock_img=pg.image.load('image\주식보유량.png')

showsell_img = pg.image.load('image\매수창.png')
sellten_img = pg.image.load('image\\10주매수.png')
sellthrteen_img = pg.image.load('image\\30주매수.png')
sellfivteen_img = pg.image.load('image\\50주매수.png')
sellhund_img = pg.image.load('image\\100주매수.png')
decidesell_img = pg.image.load('image\매수결정.png')

#버튼
start_button = button.Button(650, 500, startbutton_img, 0.5)
howto_button = button.Button(650, 600, howtobutton_img, 0.5)
#cancel_button = button.Button(650, 500, cancelbutton_img, 0.5) #좌표 수정 필요

#game 화면 실행 변수들
main_menu = True
run = True
game_menu = False
howto_menu = False
stock_menu1= False
stock_menu2= False
stock_menu3= False
sell_menu = False

#유저 초기 정보
goal=100000   #목표 금액
seed=1000      #초기 금액


while run:

    clock.tick(60)

    if main_menu == True:
        imgdraw(mainmenu_img,1500,800,0,0,1)
        if start_button.draw(screen) == True:
            print('GAME START')
            main_menu = False
            game_menu=True

        if howto_button.draw(screen) == True:
            print('HOW TO PLAY THE GAME')
            main_menu = False
            howto_menu=True
            
    
    if howto_menu == True:
        screen.blit(howtomenu_img,(100,100))
        pg.display.flip()
        start_button = button.Button(1200, 600, startbutton_img, 0.5)
        if start_button.draw(screen) == True:
            print('GAME START')
            howto_menu = False
            game_menu = True
            
    if game_menu == True:
# 초기 설정
        imgdraw(gamebg_img,1500,800,0,0,1)
        imgdraw(seedicon_img,150,200,5,60,0.5)
        Writetext(seed,50,WHITE,200,80)      
        imgdraw(goal_img,150,200,1025,60,1)
        Writetext(goal,50,WHITE,1245,80)
        imgdraw(stockbox_img,500,570,70,200,1)
        cancel_button = button.Button(1180,700,cancelbutton_img,0.5)
        
        stock1_button = button.Button(80,380,stock1_img,1)
        stock2_button = button.Button(80,500,stock2_img,1)
        stock3_button = button.Button(80,620,stock3_img,1)
        
        nextday_button = button.Button(1120,650,nextday_img,1)
        sell_button = button.Button(1125,570,sell_img,1)
        buy_button = button.Button(1125,440,buy_img,1)
        decide_button = button.Button(350,600,decidesell_img,0.7)
        
        entervolume_button = button.Button(400,200,entervolume_img,1.2)
        sellten_button = button.Button(320,400,sellten_img,1)
        sellthr_button = button.Button(540,400,sellthrteen_img,1)
        sellfiv_button = button.Button(760,400,sellfivteen_img,1)
        sellhund_button = button.Button(980,400,sellhund_img,1)

#다음날로 가는 버튼
        if nextday_button.draw(screen)==True:
            if stock_menu1==True or stock_menu2==True or stock_menu3==True:
                False
            else:
                print("다음날로")#다음날 이동 이벤트 코드

#메뉴 1 클릭
        if stock1_button.draw(screen)==True:
            stock_menu1=True

        if stock_menu1==True:
            showinfo("hold")
            if cancel_button.draw(screen)==True:
                if sell_menu==True:
                    False
                else:
                    stock_menu1=False
            
            if sell_button.draw(screen)==True:
                print("buy_stock")
            if buy_button.draw(screen)==True:
                print("show_win")
                sell_menu=True
            
#메뉴 2 클릭
        if stock2_button.draw(screen)==True:
            stock_menu2=True

        if stock_menu2==True:
            showinfo("hold")
            if cancel_button.draw(screen)==True:
                if sell_menu==True:
                    False
                else:
                    stock_menu2=False

            if sell_button.draw(screen)==True:
                print("buy_stock")
            if buy_button.draw(screen)==True:
                print("show_win")
                sell_menu=True

#메뉴 3 클릭
        if stock3_button.draw(screen)==True:
            stock_menu3=True

        if stock_menu3==True:
            showinfo("hold")
            if cancel_button.draw(screen)==True:
                if sell_menu==True:
                    False
                else:
                    stock_menu3=False


            if sell_button.draw(screen)==True:
                print("buy_stock")
            if buy_button.draw(screen)==True:
                print("show_win")
                sell_menu=True
            
        if sell_menu==True:
            imgdraw(showsell_img,900,600,300,100,1)
            cancel_button = button.Button(850,600,cancelbutton_img,0.7)
            
            if sellten_button.draw(screen)==True:
                print("sell 10")
            if sellthr_button.draw(screen)==True:
                print("sell 30")
            if sellfiv_button.draw(screen)==True:
                print("sell 50")
            if sellhund_button.draw(screen)==True:
                print("sell 100")
            
            if entervolume_button.draw(screen)==True:
                print("user input")
            
            if cancel_button.draw(screen)==True:
                sell_menu=False
            if decide_button.draw(screen)==True:
                print("succeed trade")     #추후 기능 추가


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.flip()

pg.quit()