import pygame as pg

pg.init()

backgroundcolor=((0, 10, 30))

running=True
WIDTH=1920
HEIGHT=1080
tx = WIDTH/2
ty = HEIGHT-350
ts = 30
clock=pg.time.Clock()
font = pg.font.Font('freesansbold.ttf',ts)
text = font.render('Petlja Metrolines', True, "White", backgroundcolor)
textRect = text.get_rect()
textRect.center = (tx,ty)
screen=pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(backgroundcolor)
pg.time.wait(250)
pg.display.update()
pg.draw.line(screen,(24, 188, 156),(WIDTH/2-85,HEIGHT/2-80),(WIDTH/2-185,HEIGHT/2),10)
pg.time.wait(400)
pg.display.update()
pg.draw.line(screen,(24, 188, 156),(WIDTH/2-185,HEIGHT/2),(WIDTH/2-85,HEIGHT/2+80),10)
pg.time.wait(400)
pg.display.update()
pg.draw.line(screen,(24, 188, 156),(WIDTH/2-85,HEIGHT/2+80),(WIDTH/2+80,HEIGHT/2-80),10)
pg.time.wait(400)
pg.display.update()
pg.draw.line(screen,(24, 188, 156),(WIDTH/2+80,HEIGHT/2-80),(WIDTH/2+180,HEIGHT/2),10)
pg.time.wait(400)
pg.display.update()
pg.draw.line(screen,(24, 188, 156),(WIDTH/2+80,HEIGHT/2-80),(WIDTH/2+180,HEIGHT/2),10)
pg.time.wait(400)
pg.display.update()
pg.draw.line(screen,(24, 188, 156),(WIDTH/2+180,HEIGHT/2),(WIDTH/2+80,HEIGHT/2+80),10)
pg.time.wait(400)
pg.display.update()
pg.draw.line(screen,(24, 188, 156),(WIDTH/2+80,HEIGHT/2+80),(WIDTH/2-85,HEIGHT/2-80),10)
pg.time.wait(400)
pg.display.update()
pg.draw.circle(screen,"White",(WIDTH/2-85,HEIGHT/2-80),15)
pg.time.wait(400)
pg.display.update()
pg.draw.circle(screen,"White",(WIDTH/2-185,HEIGHT/2),15)
pg.time.wait(400)
pg.display.update()
pg.draw.circle(screen,"White",(WIDTH/2-85,HEIGHT/2+80),15)
pg.time.wait(400)
pg.display.update()
pg.draw.circle(screen,"White",(WIDTH/2+80,HEIGHT/2-80),15)
pg.time.wait(400)
pg.display.update()
pg.draw.circle(screen,"White",(WIDTH/2+180,HEIGHT/2),15)
pg.time.wait(400)
pg.display.update()
pg.draw.circle(screen,"White",(WIDTH/2+80,HEIGHT/2+80),15)
pg.time.wait(400)
pg.display.update()
screen.blit(text, textRect)
pg.display.update()
pg.time.wait(800)


while running:
    screen.fill(backgroundcolor)
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            running=False
    """pg.draw.line(screen,(24, 188, 156),(WIDTH/2-85,HEIGHT/2-80),(WIDTH/2-185,HEIGHT/2),10)
    pg.draw.line(screen,(24, 188, 156),(WIDTH/2-185,HEIGHT/2),(WIDTH/2-85,HEIGHT/2+80),10)
    pg.draw.line(screen,(24, 188, 156),(WIDTH/2-85,HEIGHT/2+80),(WIDTH/2+80,HEIGHT/2-80),10)
    pg.draw.line(screen,(24, 188, 156),(WIDTH/2+80,HEIGHT/2-80),(WIDTH/2+180,HEIGHT/2),10)
    pg.draw.line(screen,(24, 188, 156),(WIDTH/2+80,HEIGHT/2-80),(WIDTH/2+180,HEIGHT/2),10)
    pg.draw.line(screen,(24, 188, 156),(WIDTH/2+180,HEIGHT/2),(WIDTH/2+80,HEIGHT/2+80),10)
    pg.draw.line(screen,(24, 188, 156),(WIDTH/2+80,HEIGHT/2+80),(WIDTH/2-85,HEIGHT/2-80),10)
    pg.draw.circle(screen,"White",(WIDTH/2-185,HEIGHT/2),15)
    pg.draw.circle(screen,"White",(WIDTH/2-85,HEIGHT/2+80),15)
    pg.draw.circle(screen,"White",(WIDTH/2-85,HEIGHT/2-80),15)
    pg.draw.circle(screen,"White",(WIDTH/2+180,HEIGHT/2),15)
    pg.draw.circle(screen,"White",(WIDTH/2+80,HEIGHT/2+80),15)
    pg.draw.circle(screen,"White",(WIDTH/2+80,HEIGHT/2-80),15)
    screen.blit(text, textRect)
    if ty>=300:
        ty -= 100
        ts+=2"""
    pg.time.wait(200)

            
            
            
            
            
            
            
            
            
            
    pg.display.update()
    clock.tick(60)
    