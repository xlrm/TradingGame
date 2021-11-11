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

start_img = pg.image.load('게임시작.png')
howto_img = pg.image.load('게임방법.png')
howto_bimg= pg.image.load('게임설명.png')

start_button = button.Button(650, 500, start_img, 1)
howto_button = button.Button(650, 600, howto_img, 1)

#game 화면 실행 변수들
main_menu = True
run = True
play = False
gameexp = False

#유저 초기 정보
goal=0    #목표 금액
ceed=0    #초기 금액

while run:
    clock.tick(60)
    screen.fill(WHITE)

    if main_menu == True:
        if start_button.draw(screen) == True:
            print('GAME START')
            play=True
            main_menu = False

        if howto_button.draw(screen) == True:
            print('HOW TO PLAY THE GAME')
            gameexp=True
            main_menu = False
    
    if gameexp==True:
        screen.blit(howto_bimg,[100,100])
        start_button = button.Button(1200, 700, start_img, 1) #추후 버튼 위치 수정
        if start_button.draw(screen) == True:
            print('GAME START')
            play=True
            gameexp=False
        
    if play==True:
        print("let's play")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
 
    pg.display.flip()

pg.quit()