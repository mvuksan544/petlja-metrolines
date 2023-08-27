import pygame as pg
from random import randint
pg.init()

clock=pg.time.Clock()
backgroundcolor=((0, 10, 30))

running=True

WIDTH=1920
HEIGHT=1080
timer=1
screen=pg.display.set_mode((WIDTH, HEIGHT))

RSLocationsH=[]
RSLocationsW=[]
TSLocationsH=[]
TSLocationsW=[]
SSLocationsH=[]
SSLocationsW=[]
CSLocationsH=[]
CSLocationsW=[]
WSLocationsH=[]
WSLocationsW=[]


SLocationsW=[WIDTH//4, WIDTH//7, WIDTH//7, WIDTH//5*4, WIDTH//3*2, WIDTH//8*6, WIDTH//6*5]
SLocationsH=[HEIGHT//5*2, HEIGHT//3*2, HEIGHT//7, HEIGHT//2, HEIGHT//8*3, HEIGHT//7*2, HEIGHT//7*5 ]


RSLocationsH.append(WIDTH//5)
RSLocationsW.append(WIDTH//2)
TSLocationsW.append(WIDTH//3*2)
TSLocationsH.append(WIDTH//3)
SSLocationsW.append(WIDTH//3)
SSLocationsH.append(HEIGHT//4)
CSLocationsW.append(WIDTH//2)
CSLocationsH.append(HEIGHT//2)

WSLocationsH.append(WIDTH//5)
WSLocationsH.append(WIDTH//3)
WSLocationsH.append(HEIGHT//4)
WSLocationsH.append(HEIGHT//2)
WSLocationsW.append(WIDTH//2)
WSLocationsW.append(WIDTH//3)
WSLocationsW.append(WIDTH//3*2)
WSLocationsW.append(WIDTH//2)


LPicker=[[77, 247, 222],[240, 98, 98] , [125, 247, 77], [255, 252, 84], [239, 87, 250]]
LUnlocked=[True, False, False, False, False]

line0=[]
line1=[]
line2=[]
line3=[]
line4=[]

line_selected=-1
while running:
    
    
    

    timer+=1
    screen.fill(backgroundcolor)
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            running=False

    for i in range(len(CSLocationsH)):
        pg.draw.circle(screen, "White", (CSLocationsW[i], CSLocationsH[i]), WIDTH//110, 5)

    for i in range(len(SSLocationsH)):
        pg.draw.rect(screen, "White", (SSLocationsW[i], SSLocationsH[i], WIDTH/70, WIDTH/70),5 )

    for i in range (len(TSLocationsH)):
        pg.draw.lines(screen, "White", True, ((TSLocationsW[i], TSLocationsH[i]),(TSLocationsW[i]-WIDTH/130, TSLocationsH[i]+HEIGHT/40), (TSLocationsW[i]+WIDTH/130, TSLocationsH[i]+HEIGHT/40)), 5)

    
    for i in range (len(RSLocationsH)):
        pg.draw.lines(screen, "White", True, ((RSLocationsW[i], RSLocationsH[i]),(RSLocationsW[i]-WIDTH/128, RSLocationsH[i]+HEIGHT/72),(RSLocationsW[i], RSLocationsH[i]+HEIGHT/36), (RSLocationsW[i]+WIDTH/128, RSLocationsH[i]+HEIGHT/72)), 5)
            
    if timer>=20:
        if len(SLocationsH)>0:
            timer=0
            x=randint(0, 4)
            y=randint(0, len(SLocationsH)-1)
            
            if x == 0:
                CSLocationsH.append(SLocationsH[y])
                CSLocationsW.append(SLocationsW[y])
                WSLocationsH.append(SLocationsH[y]) 
                WSLocationsW.append(SLocationsW[y])
                SLocationsW.remove(SLocationsW[y])                    
                SLocationsH.remove(SLocationsH[y])
            elif x == 1:
                SSLocationsH.append(SLocationsH[y])
                SSLocationsW.append(SLocationsW[y])
                WSLocationsH.append(SLocationsH[y]) 
                WSLocationsW.append(SLocationsW[y])
                SLocationsW.remove(SLocationsW[y])                    
                SLocationsH.remove(SLocationsH[y])
            elif x == 2:
                TSLocationsH.append(SLocationsH[y])
                TSLocationsW.append(SLocationsW[y])
                WSLocationsH.append(SLocationsH[y]) 
                WSLocationsW.append(SLocationsW[y])
                SLocationsW.remove(SLocationsW[y])                    
                SLocationsH.remove(SLocationsH[y])
            elif x == 3:
                RSLocationsH.append(SLocationsH[y])
                RSLocationsW.append(SLocationsW[y])
                WSLocationsH.append(SLocationsH[y]) 
                WSLocationsW.append(SLocationsW[y])
                SLocationsW.remove(SLocationsW[y])                    
                SLocationsH.remove(SLocationsH[y])
                
                
                
    for i in range (len(LPicker)):
        if LUnlocked[i]==True:
            pg.draw.circle(screen, LPicker[i], (WIDTH//13*(5+i), (HEIGHT//10)*9), WIDTH//60)
        else:
            pg.draw.circle(screen, [119, 114, 120], (WIDTH//13*(5+i), (HEIGHT//10)*9), WIDTH//150)
    
    if event.type==pg.MOUSEBUTTONDOWN and event.button == 1 :
        pos1=pg.mouse.get_pos()
        for i in range(len(LPicker)):
            if abs(pos1[0]-WIDTH//13*(5+i))*abs(pos1[0]-WIDTH//13*(5+i))+abs(pos1[1]-(HEIGHT//10)*9)*abs(pos1[1]-(HEIGHT//10)*9)<=WIDTH//60*WIDTH//60:
                line_selected=i
            print(abs(pos1[0]-WIDTH//13*(5+i))*abs(pos1[0]-WIDTH//13*(5+i))+abs(pos1[1]-(HEIGHT//10)*9)*abs(pos1[1]-(HEIGHT//10)*9))
                
                
    if event.type==pg.MOUSEBUTTONDOWN and event.button == 3 :
       line_selected=-1
    
    pg.display.update()
    clock.tick(60)