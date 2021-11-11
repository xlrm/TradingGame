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
    text=font.render(text,True, WHITE)
    screen.blit(text,site)
    return None

def imgdraw(img,w,h,x,y,scale):
    pg.transform.scale(img,(w*scale,h*scale))
    screen.blit(img,[x,y])

pg.display.set_caption("주식 게임")

mainmenu_img = pg.image.load('image\메인화면.png')
howtomenu_img= pg.image.load('image\게임설명.png')
gamebg_img=pg.image.load('image\게임화면.png')
entervolume_img = pg.image.load('image\개수입력.png')

startbutton_img = pg.image.load('image\게임시작버튼.png')
howtobutton_img = pg.image.load('image\게임방법버튼.png')
cancelbutton_img = pg.image.load('image\취소버튼.png')

seedicon_img = pg.image.load('image\시드머니아이콘.png')
goal_img=pg.image.load('image\목표자산.png')

start_button = button.Button(650, 500, startbutton_img, 0.5)
howto_button = button.Button(650, 600, howtobutton_img, 0.5)
cancle_button = button.Button(650, 500, cancelbutton_img, 0.5) #좌표 수정 필요

#game 화면 실행 변수들
main_menu = True
run = True
game_menu = False
howto_menu = False

#유저 초기 정보
goal=0    #목표 금액
seed=0    #초기 금액

while run:
    clock.tick(60)

    screen.fill(WHITE)
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
        imgdraw(howtomenu_img,1500,800,0,0,1)
        start_button = button.Button(1200, 620, startbutton_img, 0.5)
        
        if start_button.draw(screen) == True:
            print('GAME START')
            howto_menu = False
            game_menu = True
            
    if game_menu == True:
        imgdraw(gamebg_img,1500,800,0,0,1)

        imgdraw(seedicon_img,150,200,5,60,0.5)
        Writetext(seed,50,200,80)      

        imgdraw(goal_img,150,200,1025,60,1)
        Writetext(goal,50,1245,80)      

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 
 
    pg.display.flip()

pg.quit()
