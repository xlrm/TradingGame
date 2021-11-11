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
def Writetext(text,fontsize,x,y):        #문자열,폰트크기,생성할 위치
    if str(text).isdigit()==True:
        text=str(text)
    site=(x,y)                         
    font=pg.font.SysFont("malgungothic",fontsize)
    text=font.render(text,True, BLACK)
    screen.blit(text,site)
    return None

pg.display.set_caption("주식 게임")

#이미지
mainmenu_img = pg.image.load('image\메인화면.png')
howtomenu_img= pg.image.load('image\게임설명.png')

entervolume_img = pg.image.load('image\개수입력.png')

startbutton_img = pg.image.load('image\게임시작버튼.png')
howtobutton_img = pg.image.load('image\게임방법버튼.png')
cancelbutton_img = pg.image.load('image\취소버튼.png')

<<<<<<< Updated upstream
=======
seedicon_img = pg.image.load('image\시드머니아이콘.png')
goal_img=pg.image.load('image\목표자산.png')

stockbox_img=pg.image.load('image\주식박스.png')
stock1_img=pg.image.load('image\주식1.png')
stock2_img=pg.image.load('image\주식2.png')
stock3_img=pg.image.load('image\주식3.png')

show_img=pg.image.load('image\창.png')

#버튼

>>>>>>> Stashed changes
start_button = button.Button(650, 500, startbutton_img, 0.5)
howto_button = button.Button(650, 600, howtobutton_img, 0.5)
cancle_button = button.Button(650, 500, cancelbutton_img, 0.5) #좌표 수정 필요

#game 화면 실행 변수들
main_menu = True
run = True
game_menu = False
howto_menu = False
stock_menu1= False
stock_menu2= False
stock_menu3= False


#유저 초기 정보
goal=1000    #목표 금액
seed=0    #초기 금액

while run:

    clock.tick(60)
    stock1_button = button.Button(80,380,stock1_img,1)
    stock2_button = button.Button(80,500,stock2_img,1)
    stock3_button = button.Button(80,620,stock3_img,1)
    cancel_button = button.Button(1190,700,cancelbutton_img,0.5)


    if main_menu == True:
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
<<<<<<< Updated upstream
            
=======

    if game_menu == True:
        imgdraw(gamebg_img,1500,800,0,0,1)
        imgdraw(seedicon_img,150,200,5,60,0.5)
        Writetext(seed,50,200,80)      
        imgdraw(goal_img,150,200,1025,60,1)
        Writetext(goal,50,1245,80)
        imgdraw(stockbox_img,500,570,70,200,1)
        

#메뉴 1 클릭
        if stock1_button.draw(screen)==True:
            stock_menu1=True
        if stock_menu1==True:
            imgdraw(show_img,830,570,600,200,1)

            if cancel_button.draw(screen)==True:
                stock_menu1=False

#메뉴 2 클릭
        if stock2_button.draw(screen)==True:
            stock_menu2=True
        if stock_menu2==True:
            imgdraw(show_img,830,570,600,200,1)

            if cancel_button.draw(screen)==True:
                stock_menu2=False

#메뉴 3 클릭
        if stock3_button.draw(screen)==True:
            stock_menu3=True
        if stock_menu3==True:
            imgdraw(show_img,830,570,600,200,1)
 
            if cancel_button.draw(screen)==True:
                stock_menu3=False


>>>>>>> Stashed changes

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
<<<<<<< Updated upstream
 
=======
        
>>>>>>> Stashed changes
    pg.display.flip()

pg.quit()