import pygame as pg
import matplotlib.pyplot as plt
import numpy as np
import button, sys

pg.init()
WHITE= (255,255,255)
size  = [1500,800]
screen= pg.display.set_mode(size)
clock = pg.time.Clock()

pg.display.set_caption("주식 게임")

start_img = pg.image.load('게임시작.png')
howto_img = pg.image.load('게임방법.png')



start_button = button.Button(650, 500, start_img, 1)
howto_button = button.Button(650, 600, howto_img, 1)


run = True
while run:
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
    screen.fill(WHITE)

    if start_button.draw(screen) == True:
        print('GAME START')
    if howto_button.draw(screen) == True:
        print('HOW TO PLAY THE GAME')
 
    pg.display.flip()

pg.quit()
