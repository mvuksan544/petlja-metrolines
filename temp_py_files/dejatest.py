import pygame as pg
from random import randint
pg.init()

clock=pg.time.Clock()
backgroundcolor=((0, 10, 30))

running=True

WIDTH=1440
HEIGHT=900
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

MetroPlace=False

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
WSLocationsW.append(WIDTH//3*2)
WSLocationsW.append(WIDTH//3)
WSLocationsW.append(WIDTH//2)


LPicker=[[77, 247, 222],[240, 98, 98] , [125, 247, 77], [255, 252, 84], [239, 87, 250]]
LUnlocked=[True, True, True, True, True]

L0T=0
L1T=0
L2T=0
L3T=0
L4T=0

line0=[]
line1=[]
line2=[]
line3=[]
line4=[]

Met0x=[]
Met0y=[]
Met0s=[]
Met0st=[]

Met1x=[]
Met1y=[]
Met1s=[]
Met1st=[]

Met2x=[]
Met2y=[]
Met2s=[]
Met2st=[]

Met3x=[]
Met3y=[]
Met3s=[]
Met3st=[]

Met4x=[]
Met4y=[]
Met4s=[]
Met4st=[]



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
                
    #Metro placement
    pg.draw.rect(screen, [150, 150, 150], (400, HEIGHT//10*9-20, 100, 40))    
    if event.type==pg.MOUSEBUTTONDOWN:
        pos3=pg.mouse.get_pos()
        if 400<pos3[0] and pos3[0]<500 and 40<pos3[1] and pos3[1]<HEIGHT//10*9+20:
            MetroPlace=True
            for i in range(len(LPicker)):
                if LUnlocked[i] and MetroPlace and abs(WIDTH//13*(5+i)-pos3[0])<=WIDTH//60 and abs(HEIGHT//10*9-pos3[1])<=WIDTH//60:
                    line_selected1=i
                    print(line_selected1)
                    if i == 0:
                        L0T+=1
                        Met0s.append(1)
                        Met0x.append(line0[0][0])
                        Met0y.append(line0[0][1])
                        Met0st.append(0)
                        MetroPlace==False
    if MetroPlace:
        pos4=pg.mouse.get_pos()
        pg.draw.rect(screen, (150, 150, 150,), (pos4[0]-40, pos4[1]-17, 80, 34))
          
                
                
                
                
                
                
    #line drawing            
                
    for i in range(1, len(line0)):
        pg.draw.lines(screen, LPicker[0], False, (line0[i-1],[line0[i-1][0], line0[i][1]], line0[i] ), 5)
    for i in range(1, len(line1)):
        pg.draw.lines(screen, LPicker[1], False, (line1[i-1],[line1[i-1][0], line1[i][1]], line1[i] ), 5) 
    for i in range(1, len(line2)):
        pg.draw.lines(screen, LPicker[2], False, (line2[i-1],[line2[i-1][0], line2[i][1]], line2[i] ), 5) 
    for i in range(1, len(line3)):
        pg.draw.lines(screen, LPicker[3], False, (line3[i-1],[line3[i-1][0], line3[i][1]], line3[i] ), 5)
    for i in range(1, len(line4)):
        pg.draw.lines(screen, LPicker[4], False, (line4[i-1],[line4[i-1][0], line4[i][1]], line4[i] ), 5)  
                
    #Line selection         

    for i in range (len(LPicker)):
        if LUnlocked[i]==True:
            pg.draw.circle(screen, LPicker[i], (WIDTH//13*(5+i), (HEIGHT//10)*9), WIDTH//60)
        else:
            pg.draw.circle(screen, [119, 114, 120], (WIDTH//13*(5+i), (HEIGHT//10)*9), WIDTH//150)
    
    if event.type==pg.MOUSEBUTTONDOWN and event.button == 1 :
        pos1=pg.mouse.get_pos()
        for i in range(len(LPicker)):
            if LUnlocked[i] and abs(WIDTH//13*(5+i)-pos1[0])<=WIDTH//60 and abs(HEIGHT//10*9-pos1[1])<=WIDTH//60:
                line_selected=i
        
    #metro movemant
    if len(line0)>0:
        for i in range(len(Met0y)):
            if Met0x[i]<line0[Met0st[i]][0]:
                Met0x[i]+=Met0s[i]
            elif Met0x[i]>line0[Met0st[i]][0]:
                Met0x[i]+=Met0s[i]
            else:
                if Met0y[i]<line0[Met0st[i]][1]:
                    Met0y[i]+=Met0s[i]
                elif Met0y[i]>line0[Met0st[i]][1]:
                    Met0y[i]+=Met0s[i]
                else:
                    Met0st[i]=Met0st[i]+1
    for i in range (len(Met0x)):
        pg.draw.rect(screen, LPicker[0], (Met0x[i], Met0y[i], 10, 10))
        
          
                
    if event.type==pg.MOUSEBUTTONDOWN and event.button == 3:
        if line_selected==0 and len(line0)>0:
           line0.pop(len(line0)-1)
           pg.time.delay(100)
        if line_selected==1 and len(line1)>0:
           line1.pop(len(line1)-1)
           pg.time.delay(100)
        if line_selected==2 and len(line2)>0:
           line2.pop(len(line2)-1)
           pg.time.delay(100)
        if line_selected==3 and len(line3)>0:
           line3.pop(len(line3)-1)
           pg.time.delay(100)
        if line_selected==4 and len(line4)>0:
           line4.pop(len(line4)-1)
           pg.time.delay(100)
    if event.type==pg.KEYDOWN and pg.K_ESCAPE:
        line_selected=-1
       
       
    #line drawing
    if event.type==pg.MOUSEBUTTONDOWN and event.button == 1 and line_selected>=0:
        pos2=pg.mouse.get_pos()
        for i in range(len(WSLocationsH)):
            if abs(WSLocationsW[i]-pos2[0])<WIDTH//70 and abs(WSLocationsH[i]-pos2[1])<WIDTH//70:
                if line_selected==0 and (len(line0)==0 or line0[len(line0)-1]!=[WSLocationsW[i], WSLocationsH[i]]):
                    line0.append([WSLocationsW[i], WSLocationsH[i]])
                elif line_selected==1 and (len(line1)==0 or line1[len(line1)-1]!=[WSLocationsW[i], WSLocationsH[i]]):
                    line1.append([WSLocationsW[i], WSLocationsH[i]]) 
                elif line_selected==2 and (len(line2)==0 or line2[len(line2)-1]!=[WSLocationsW[i], WSLocationsH[i]]):
                    line2.append([WSLocationsW[i], WSLocationsH[i]])
                elif line_selected==3 and (len(line3)==0 or line3[len(line3)-1]!=[WSLocationsW[i], WSLocationsH[i]]):
                    line3.append([WSLocationsW[i], WSLocationsH[i]])
                elif line_selected==4 and (len(line4)==0 or line4[len(line4)-1]!=[WSLocationsW[i], WSLocationsH[i]]):
                    line4.append([WSLocationsW[i], WSLocationsH[i]])
                    
    
           

    if line_selected==4 and len(line4)>0:
        pos2=pg.mouse.get_pos()
        pg.draw.lines(screen, LPicker[4], False, (line4[len(line4)-1],[line4[len(line4)-1][0], pos2[1]], pos2 ), 5)    
    elif line_selected==3 and len(line3)>0:
        pos2=pg.mouse.get_pos()
        pg.draw.lines(screen, LPicker[3], False, (line3[len(line3)-1],[line3[len(line3)-1][0], pos2[1]], pos2 ), 5)
    elif line_selected==2 and len(line2)>0:
        pos2=pg.mouse.get_pos()
        pg.draw.lines(screen, LPicker[2], False, (line2[len(line2)-1],[line2[len(line2)-1][0], pos2[1]], pos2 ), 5) 
    elif line_selected==1 and len(line1)>0:
        pos2=pg.mouse.get_pos()
        pg.draw.lines(screen, LPicker[1], False, (line1[len(line1)-1],[line1[len(line1)-1][0], pos2[1]], pos2 ), 5) 
    elif line_selected==0 and len(line0)>0:
        pos2=pg.mouse.get_pos()
        pg.draw.lines(screen, LPicker[0], False, (line0[len(line0)-1],[line0[len(line0)-1][0], pos2[1]], pos2 ), 5)

    pg.display.update()
    clock.tick(60)   
