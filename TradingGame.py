import pygame as pg
import matplotlib.pyplot as plt
import numpy as np

pg.init()

BLACK= ( 0,  0,  0)
WHITE= (255,255,255)
 
size  = [1500,800]
screen= pg.display.set_mode(size)
  
pg.display.set_caption("주식 게임")
  
done= False
clock= pg.time.Clock()

while not done: 
  
    clock.tick(60)
     
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done=True

    screen.fill(WHITE)
 
    pg.display.flip()



pg.quit()
#양준서
