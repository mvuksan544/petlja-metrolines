import pygame as pg
import os
from pathlib import Path
import sys
from tkinter import *
from tkinter import messagebox
import time
import fileinput
source_path = Path(__file__).resolve()
source_dir = source_path.parent
os.chdir(source_dir)
dirstr = str(source_dir)
asspth = dirstr+'\Assets'
lftpth = asspth+'\left_arrow.jpg'
extpth = asspth+'\exit_arrow.jpg'
dwnpth = asspth+'\down_arrow.jpg'
savedtf = dirstr+'\Data\savedatacreated.txt'

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

with open(savedtf) as f:
    lines = f.readlines()
cgc = ('Gray')
if lines[0]=='True':
    cgc = ('White')
pg.init()
moption = 0
ooption = 0
poption = 0
backgroundcolor=((0, 10, 30))
bgcm = ((54, 49, 55))
whitec = "White"
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
#menu text Play
fontply = pg.font.Font('freesansbold.ttf',70)
textply = fontply.render('Play', True, whitec, bgcm)
textRectply = textply.get_rect()
textRectply.center = (tx-175,492)

#menu text Options
fontopt = pg.font.Font('freesansbold.ttf',70)
textopt = fontopt.render('Options', True, whitec, bgcm)
textRectopt = textopt.get_rect()
textRectopt.center = (tx-115,662)

#menu text Exit
fontext = pg.font.Font('freesansbold.ttf',70)
textext = fontext.render('Exit', True, whitec, bgcm)
textRectext = textext.get_rect()
textRectext.center = (tx-177,832)

#menu text main
font1 = pg.font.Font('freesansbold.ttf',70)
text1 = font1.render('Petlja Metrolines', True, "White", bgcm)
textRect1 = text1.get_rect()
textRect1.center = (tx-100,350)
#options text main
font2 = pg.font.Font('freesansbold.ttf',70)
text2 = font2.render('Options', True, "White", bgcm)
textRect2 = text2.get_rect()
textRect2.center = (tx-262,350)
#options text Belgrade Metro
fontbmt = pg.font.Font('freesansbold.ttf',70)
textbmt = fontbmt.render('Belgrade Metro', True, whitec, bgcm)
textRectbmt = textbmt.get_rect()
textRectbmt.center = (tx+20,492)
#options text Petlja Servers
fontpsrv = pg.font.Font('freesansbold.ttf',70)
textpsrv = fontpsrv.render('Connect to Petlja servers', True, whitec, bgcm)
textRectpsrv = textpsrv.get_rect()
textRectpsrv.center = (tx+185,662)

#options text Airport
fontarp = pg.font.Font('freesansbold.ttf',70)
textarp = fontarp.render('Airport', True, whitec, bgcm)
textRectarp = textarp.get_rect()
textRectarp.center = (tx-127,832)

#option text back
fontbck = pg.font.Font('freesansbold.ttf',70)
textbck = fontbck.render('Back', True, whitec, bgcm)
textRectbck = textbck.get_rect()
textRectbck.center = (tx-157,832)

#play text main
font3 = pg.font.Font('freesansbold.ttf',70)
text3 = font3.render('Play', True, "White", bgcm)
textRect3 = text3.get_rect()
textRect3.center = (tx-312,350)

#play text New Game
fontng = pg.font.Font('freesansbold.ttf',70)
textng = fontng.render('New Game', True, whitec, bgcm)
textRectng = textng.get_rect()
textRectng.center = (tx-64,492)

#play text Continue Game
fontcg = pg.font.Font('freesansbold.ttf',70)
textcg = fontcg.render('Continue Game', True, cgc, bgcm)
textRectcg = textcg.get_rect()
textRectcg.center = (tx+26,662)
tyu = False
tyu1 = False
tyu2 = False
tyu3 = False
tyu4 = False
tyu5 = False
tyu6 = False
tyu7 = False
tyu8 = False
mtp = False
poption = 0
def menu():    
    global moption
    global tyu
    global tyu1
    global tyu2
    global mtp
    global poption
    global tyu6
    global tyu7
    global tyu8
    global textbck
    global textRectbck
    global text3
    global textRect3
    global whitec
    global bgcm
    global ooption
    global textng
    global textcg
    global keys
    if mtp==False:
        if moption>2:
            moption=0
        if moption<=-1:
            moption=2
        mx,my = pg.mouse.get_pos()
        if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_DOWN]:
                    moption+=1
                if keys[pg.K_UP]:
                    moption-=1
        if pg.Rect.collidepoint(textRectext,(mx,my)) or moption==2:
            textext = fontext.render('Exit', True, bgcm, whitec)
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    tyu = True
            
            if pg.mouse.get_pressed()[0]==True or tyu==True:
                tyu = False
                running=False
                pg.quit()
                sys.exit()
        else:
            textext = fontext.render('Exit', True, whitec, bgcm)
        
        if pg.Rect.collidepoint(textRectply,(mx,my)) or moption==0:
            textply = fontply.render('Play', True, bgcm, whitec)
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    tyu1 = True
            if pg.mouse.get_pressed()[0]==True or tyu1==True:
                mtp=True
                tyu1 = False
        else:
            textply = fontply.render('Play', True, whitec, bgcm)
        
        if pg.Rect.collidepoint(textRectopt,(mx,my)) or moption==1:
            textopt = fontopt.render('Options', True, bgcm, whitec)
        else:
            textopt = fontopt.render('Options', True, whitec, bgcm)
        screen.blit(text1,textRect1)
        screen.blit(lftimg, (tx-380,430))
        screen.blit(dwnimg,(tx-380,600))
        screen.blit(extimg,(tx-380,770))
        screen.blit(textply,textRectply)
        screen.blit(textopt,textRectopt)
        screen.blit(textext,textRectext)
       
    if mtp==True:    
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_DOWN]:
                poption=poption+1
            if keys[pg.K_UP]:
                poption=poption-1
        
        if poption>3:
            poption=1
        if poption<0:
            poption=3

        screen.fill(bgcm)
        screen.blit(lftimg, (tx-380,430))
        screen.blit(lftimg, (tx-380,600))
        screen.blit(textbck,textRectbck)
        screen.blit(text3,textRect3)
        screen.blit(extimg,(tx-380,770))
        screen.blit(textng,textRectng)
        screen.blit(textcg,textRectcg)
        mx,my = pg.mouse.get_pos()
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_ESCAPE]:
                mtp=False
        
        if pg.Rect.collidepoint(textRectng,(mx,my)) or poption==1:
            textng = fontng.render('New Game', True, bgcm, whitec)   
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    tyu6 = True
            if pg.mouse.get_pressed()[0]==True or tyu6==True:
                if lines[0]=='True':
                    questionsave = messagebox.askokcancel("Save data already exists","Are you sure you want to delete your save data?")
                
                if questionsave==False:
                    tyu6 = False
                
                if questionsave==True:
                    replaceAll(savedtf,"True","False")
                    lines[0]='False'
                    cgc = 'Gray'
                    textcg = fontcg.render('Continue Game', True, cgc, bgcm)
                
                
                if lines[0]=='False' or questionsave==True:
                    
                    tyu6 = False
                    mtp=False
                    poption = 0
                #ubaciti Dekijev gejm function ovde
        else:
            textng = fontng.render('New Game', True, whitec, bgcm)
        
        if (pg.Rect.collidepoint(textRectcg,(mx,my)) or poption==2) and lines[0]=='True':
            textcg = fontcg.render('Continue Game', True, bgcm, whitec)   
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    tyu7 = True
            if pg.mouse.get_pressed()[0]==True or tyu7==True:
                tyu7 = False
                mtp=False
                poption = 0
                #ubciti funkciju da ucita game iz save-a
        elif lines[0]=='True':
            textcg = fontcg.render('Continue Game', True, whitec, bgcm)  
        
        if pg.Rect.collidepoint(textRectbck,(mx,my)) or poption==3:
            textbck = fontbck.render('Back', True, bgcm, whitec)   
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    tyu8 = True
            if pg.mouse.get_pressed()[0]==True or tyu8==True:
                tyu8 = False
                mtp=False
                poption = 0
        else:
            textbck = fontbck.render('Back', True, whitec, bgcm) 
    
    
    
    


screen=pg.display.set_mode((WIDTH, HEIGHT))
lftimg = pg.image.load(lftpth).convert()
extimg = pg.image.load(extpth).convert()
dwnimg = pg.image.load(dwnpth).convert()
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
optwhile = False
pfun = False
while running:
    screen.fill(bgcm)
    for event in pg.event.get():
        if event.type ==pg.QUIT:
            running=False   
    pg.time.wait(200)
    if optwhile==False and pfun==False:
        menu()
        
    
    mx,my=pg.mouse.get_pos()
    if pg.Rect.collidepoint(textRectopt,(mx,my)) or moption==1:
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_RETURN]:
                tyu2 = True
        if pg.mouse.get_pressed()[0]==True or tyu2==True:
            optwhile=True
            tyu2=False
    if optwhile==True:
        screen.blit(lftimg, (tx-380,430))
        screen.blit(lftimg, (tx-380,600))
        screen.blit(extimg, (tx-380,770))
        screen.blit(text2,textRect2)
        screen.blit(textbmt,textRectbmt)
        screen.blit(textpsrv,textRectpsrv)
        screen.blit(textbck,textRectbck)
        if ooption>3:
            ooption=0
        if moption<0:
            ooption=2
        mx,my = pg.mouse.get_pos()
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_DOWN]:
                ooption+=1
            if keys[pg.K_UP]:
                ooption-=1
        
        if event.type == pg.KEYDOWN:
            keys = pg.key.get_pressed()
            if keys[pg.K_ESCAPE]:
                optwhile=False
        if pg.Rect.collidepoint(textRectbmt,(mx,my)) or ooption==1:
            textbmt = fontbmt.render('Belgrade Metro', True, bgcm, whitec)
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()    
                if keys[pg.K_RETURN]:
                    tyu3 = True
            if pg.mouse.get_pressed()[0]==True or tyu3==True:
                tyu3 = False
                messagebox.showerror('Srpski Napredni Error','napredni_beogradski_metro not found')
        else:
            textbmt = fontbmt.render('Belgrade metro', True, whitec, bgcm)

        if pg.Rect.collidepoint(textRectpsrv,(mx,my)) or ooption==2:
            textpsrv = fontpsrv.render('Connect to Petlja servers', True, bgcm, whitec)
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    tyu4 = True
            if pg.mouse.get_pressed()[0]==True or tyu4==True:
                tyu4 = False
                messagebox.showerror('500 Internal Server Error','The server has encountered a situation it does not know how to handle.')
        else:
            textpsrv = fontpsrv.render('Connect to Petlja servers', True, whitec, bgcm)
        
        if pg.Rect.collidepoint(textRectbck,(mx,my)) or ooption==3:
            textbck = fontbck.render('Back', True, bgcm, whitec)   
            if event.type == pg.KEYDOWN:
                keys = pg.key.get_pressed()
                if keys[pg.K_RETURN]:
                    tyu5 = True
            if pg.mouse.get_pressed()[0]==True or tyu5==True:
                tyu5 = False
                optwhile=False
                ooption = 0
        else:
            textbck = fontbck.render('Back', True, whitec, bgcm)   

            
     
    pg.display.update()
    clock.tick(60)
    