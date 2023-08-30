import pygame as pg

pg.init()


backgroundcolor=((0, 10, 30))

running=True

WIDTH=1920
HEIGHT=1080

screen=pg.display.set_mode((WIDTH, HEIGHT))

while running:
    screen.fill(backgroundcolor)
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            running=False
    
            
            
            
            
            
            
            
            
            
            
    pg.display.update()
    