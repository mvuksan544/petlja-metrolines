import pygame as pg
from random import randint
pg.init()

clock=pg.time.Clock()
backgroundcolor=((0, 10, 30))

running=True

WIDTH=1280
HEIGHT=720
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
SPassenagers=[]
STimer=[]

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

SPassenagers.append([0])
SPassenagers.append([1])
SPassenagers.append([2])
SPassenagers.append([3])

#R=0
#T=1
#S=2
#C=3



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
Met0w=[]

Met1x=[]
Met1y=[]
Met1s=[]
Met1st=[]
Met1w=[]

Met2x=[]
Met2y=[]
Met2s=[]
Met2st=[]
Met2w=[]

Met3x=[]
Met3y=[]
Met3s=[]
Met3st=[]
Met3w=[]

Met4x=[]
Met4y=[]
Met4s=[]
Met4st=[]
Met4w=[]

timecounter=0
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
                SPassenagers.append([3])
                SLocationsW.remove(SLocationsW[y]) 
                SLocationsH.remove(SLocationsH[y])
            elif x == 1:
                SSLocationsH.append(SLocationsH[y])
                SSLocationsW.append(SLocationsW[y])
                WSLocationsH.append(SLocationsH[y]) 
                WSLocationsW.append(SLocationsW[y])
                SPassenagers.append([2])
                SLocationsW.remove(SLocationsW[y])                    
                SLocationsH.remove(SLocationsH[y])
            elif x == 2:
                TSLocationsH.append(SLocationsH[y])
                TSLocationsW.append(SLocationsW[y])
                WSLocationsH.append(SLocationsH[y]) 
                WSLocationsW.append(SLocationsW[y])
                SPassenagers.append([1])
                SLocationsW.remove(SLocationsW[y])                    
                SLocationsH.remove(SLocationsH[y])
            elif x == 3:
                RSLocationsH.append(SLocationsH[y])
                RSLocationsW.append(SLocationsW[y])
                WSLocationsH.append(SLocationsH[y]) 
                WSLocationsW.append(SLocationsW[y])
                SPassenagers.append([0])
                SLocationsW.remove(SLocationsW[y])                    
                SLocationsH.remove(SLocationsH[y])
                
    #Metro placement
    pg.draw.rect(screen, [150, 150, 150], (400, HEIGHT//10*9-20, 100, 40))    
    if event.type==pg.MOUSEBUTTONDOWN and event.button==1:
        pos3=pg.mouse.get_pos()
        if 400<pos3[0] and pos3[0]<500 and HEIGHT//10*9-20<pos3[1] and pos3[1]<HEIGHT//10*9+20:
            MetroPlace=True
        for i in range(len(LPicker)):
                if LUnlocked[i] and MetroPlace and abs(WIDTH//13*(5+i)-pos3[0])<=WIDTH//60 and abs(HEIGHT//10*9-pos3[1])<=WIDTH//60:
                    line_selected1=i
                    if i == 0:
                        L0T+=1
                        Met0s.append(1)
                        Met0x.append(line0[0][0])
                        Met0y.append(line0[0][1])
                        Met0st.append(0)
                        Met0w.append(True)
                        MetroPlace==False
                        pg.time.delay(100)
                    if i == 1:
                        L0T+=1
                        Met1s.append(1)
                        Met1x.append(line1[0][0])
                        Met1y.append(line1[0][1])
                        Met1st.append(0)
                        Met1w.append(True)
                        pg.time.delay(100)
                    if i == 2:
                        L0T+=1
                        Met2s.append(1)
                        Met2x.append(line2[0][0])
                        Met2y.append(line2[0][1])
                        Met2st.append(0)
                        Met2w.append(True)
                        pg.time.delay(100)
                    if i == 3:
                        L0T+=1
                        Met3s.append(1)
                        Met3x.append(line3[0][0])
                        Met3y.append(line3[0][1])
                        Met3st.append(0)
                        Met3w.append(True)
                        pg.time.delay(100)
                    if i == 4:
                        L0T+=1
                        Met4s.append(1)
                        Met4x.append(line4[0][0])
                        Met4y.append(line4[0][1])
                        Met4st.append(0)
                        Met4w.append(True)
                        pg.time.delay(100)
    if (event.type==pg.MOUSEBUTTONDOWN and event.button==3) and MetroPlace:
        MetroPlace=False
        
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
            if LUnlocked[i] and MetroPlace==False and abs(WIDTH//13*(5+i)-pos1[0])<=WIDTH//60 and abs(HEIGHT//10*9-pos1[1])<=WIDTH//60:
                line_selected=i
        
    #metro movemant
    if len(line0)>0:
        for i in range(len(Met0y)):
            if Met0w[i] == True:
                if Met0y[i]<line0[Met0st[i]][1]:
                    Met0y[i]+=Met0s[i]
                elif Met0y[i]>line0[Met0st[i]][1]:
                    Met0y[i]-=Met0s[i]
                else:
                    if Met0x[i]<line0[Met0st[i]][0]:
                        Met0x[i]+=Met0s[i]
                    elif Met0x[i]>line0[Met0st[i]][0]:
                        Met0x[i]-=Met0s[i]
                    else:
                        if Met0st[i]==len(line0)-1:
                            Met0w[i]=False
                        elif Met0st[i]==0:
                            Met0w[i]=True
                        else:
                            pass
                        if Met0w[i]==True:
                            Met0st[i]=Met0st[i]+1
                        else:
                            Met0st[i]=Met0st[i]-1
            else:
                if Met0x[i]<line0[Met0st[i]][0]:
                    Met0x[i]+=Met0s[i]
                elif Met0x[i]>line0[Met0st[i]][0]:
                    Met0x[i]-=Met0s[i]
                else:
                    if Met0y[i]<line0[Met0st[i]][1]:
                        Met0y[i]+=Met0s[i]
                    elif Met0y[i]>line0[Met0st[i]][1]:
                        Met0y[i]-=Met0s[i]
                    else:
                        if Met0st[i]==len(line0)-1:
                            Met0w[i]=False
                        elif Met0st[i]==0:
                            Met0w[i]=True
                        if Met0w[i]==True:
                            Met0st[i]=Met0st[i]+1
                        else:
                            Met0st[i]=Met0st[i]-1
                
    for i in range (len(Met0x)):
        pg.draw.rect(screen, LPicker[0], (Met0x[i]-10, Met0y[i]-10, 20, 20))
    if len(line1)>0:
        for i in range(len(Met1y)):
            if Met1w[i]:
                if Met1y[i]<line1[Met1st[i]][1]:
                    Met1y[i]+=Met1s[i]
                elif Met1y[i]>line1[Met1st[i]][1]:
                    Met1y[i]-=Met1s[i]
                else:
                    if Met1x[i]<line1[Met1st[i]][0]:
                        Met1x[i]+=Met1s[i]
                    elif Met1x[i]>line1[Met1st[i]][0]:
                        Met1x[i]-=Met1s[i]
                    else:
                        if Met1st[i]==len(line1)-1:
                            Met1w[i]=False
                        elif Met1st[i]==0:
                            Met1w[i]=True
                        if Met1w[i]==True:
                            Met1st[i]=Met1st[i]+1
                        else:
                            Met1st[i]=Met1st[i]-1
            else:
                if Met1x[i]<line1[Met1st[i]][0]:
                    Met1x[i]+=Met1s[i]
                elif Met1x[i]>line1[Met1st[i]][0]:
                    Met1x[i]-=Met1s[i]
                else:
                    if Met1y[i]<line1[Met1st[i]][1]:
                        Met1y[i]+=Met1s[i]
                    elif Met1y[i]>line1[Met1st[i]][1]:
                        Met1y[i]-=Met1s[i]
                    else:
                        if Met1st[i]==len(line1)-1:
                            Met1w[i]=False
                        elif Met1st[i]==0:
                            Met1w[i]=True
                        if Met1w[i]==True:
                            Met1st[i]=Met1st[i]+1
                        else:
                            Met1st[i]=Met1st[i]-1
    for i in range (len(Met1x)):
        pg.draw.rect(screen, LPicker[1], (Met1x[i]-10, Met1y[i]-10, 20, 20))
    if len(line2)>0:
        for i in range(len(Met2y)):
            if Met2w[i]:
                if Met2y[i]<line2[Met2st[i]][1]:
                    Met2y[i]+=Met2s[i]
                elif Met2y[i]>line2[Met2st[i]][1]:
                    Met2y[i]-=Met2s[i]
                else:
                    if Met2x[i]<line2[Met2st[i]][0]:
                        Met2x[i]+=Met2s[i]
                    elif Met2x[i]>line2[Met2st[i]][0]:
                        Met2x[i]-=Met2s[i]
                    else:
                        if Met2st[i]==len(line2)-1:
                            Met2w[i]=False
                        elif Met2st[i]==0:
                            Met2w[i]=True
                        if Met2w[i]==True:
                            Met2st[i]=Met2st[i]+1
                        else:
                            Met2st[i]=Met2st[i]-1
            else:
                if Met2x[i]<line2[Met2st[i]][0]:
                    Met2x[i]+=Met2s[i]
                elif Met2x[i]>line2[Met2st[i]][0]:
                    Met2x[i]-=Met2s[i]
                else:
                    if Met2y[i]<line2[Met2st[i]][1]:
                        Met2y[i]+=Met2s[i]
                    elif Met2y[i]>line2[Met2st[i]][1]:
                        Met2y[i]-=Met2s[i]
                    else:
                        if Met2st[i]==len(line2)-1:
                            Met2w[i]=False
                        elif Met2st[i]==0:
                            Met2w[i]=True
                        if Met2w[i]==True:
                            Met2st[i]=Met2st[i]+1
                        else:
                            Met2st[i]=Met2st[i]-1
    for i in range (len(Met2x)):
        pg.draw.rect(screen, LPicker[2], (Met2x[i]-10, Met2y[i]-10, 20, 20))
    if len(line3)>0:
        for i in range(len(Met3y)):
            if Met3w[i]:
                if Met3y[i]<line3[Met3st[i]][1]:
                    Met3y[i]+=Met3s[i]
                elif Met3y[i]>line3[Met3st[i]][1]:
                    Met3y[i]-=Met3s[i]
                else:
                    if Met3x[i]<line3[Met3st[i]][0]:
                        Met3x[i]+=Met3s[i]
                    elif Met3x[i]>line3[Met3st[i]][0]:
                        Met3x[i]-=Met3s[i]
                    else:
                        if Met3st[i]==len(line3)-1:
                            Met3w[i]=False
                        elif Met3st[i]==0:
                            Met3w[i]=True
                        if Met3w[i]==True:
                            Met3st[i]=Met3st[i]+1
                        else:
                            Met3st[i]=Met3st[i]-1
            else:
                if Met3x[i]<line3[Met3st[i]][0]:
                    Met3x[i]+=Met3s[i]
                elif Met3x[i]>line3[Met3st[i]][0]:
                    Met3x[i]-=Met3s[i]
                else:
                    if Met3y[i]<line3[Met3st[i]][1]:
                        Met3y[i]+=Met3s[i]
                    elif Met3y[i]>line3[Met3st[i]][1]:
                        Met3y[i]-=Met3s[i]
                    else:
                        if Met3st[i]==len(line3)-1:
                            Met3w[i]=False
                        elif Met3st[i]==0:
                            Met3w[i]=True
                        if Met3w[i]==True:
                            Met3st[i]=Met3st[i]+1
                        else:
                            Met3st[i]=Met3st[i]-1
        
    for i in range (len(Met3x)):
        pg.draw.rect(screen, LPicker[3], (Met3x[i]-10, Met3y[i]-10, 20, 20))

    if len(line4)>0:
        for i in range(len(Met4y)):
            if Met4w[i]:
                if Met4y[i]<line4[Met4st[i]][1]:
                    Met4y[i]+=Met4s[i]
                elif Met4y[i]>line4[Met4st[i]][1]:
                    Met4y[i]-=Met4s[i]
                else:
                    if Met4x[i]<line4[Met4st[i]][0]:
                        Met4x[i]+=Met4s[i]
                    elif Met4x[i]>line4[Met4st[i]][0]:
                        Met4x[i]-=Met4s[i]
                    else:
                        if Met4st[i]==len(line4)-1:
                            Met4w[i]=False
                        elif Met4st[i]==0:
                            Met4w[i]=True
                        if Met4w[i]==True:
                            Met4st[i]=Met4st[i]+1
                        else:
                            Met4st[i]=Met4st[i]-1
            else:
                if Met4x[i]<line4[Met4st[i]][0]:
                    Met4x[i]+=Met4s[i]
                elif Met4x[i]>line4[Met4st[i]][0]:
                    Met4x[i]-=Met4s[i]
                else:
                    if Met4y[i]<line4[Met4st[i]][1]:
                        Met4y[i]+=Met4s[i]
                    elif Met4y[i]>line4[Met4st[i]][1]:
                        Met4y[i]-=Met4s[i]
                    else:
                        if Met4st[i]==len(line4)-1:
                            Met4w[i]=False
                        elif Met4st[i]==0:
                            Met4w[i]=True
                        if Met4w[i]==True:
                            Met4st[i]=Met4st[i]+1
                        else:
                            Met4st[i]=Met4st[i]-1
        for i in range (len(Met4x)):
            pg.draw.rect(screen, LPicker[4], (Met4x[i]-10, Met4y[i]-10, 20, 20))
    
    
        
          
                
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



    while len(STimer)<=len(WSLocationsH):
        STimer.append(1)
    for k in range (len(STimer)):
        STimer[k]+=1
        
        
    #passenager spawning

    for i in range(len(WSLocationsH)):
        if STimer[i]>300:
            a=randint(0, 4)
            STimer[i]=0
            
            if SPassenagers[i][0]!=a:
                SPassenagers[i].append(a)
                print(SPassenagers)
                

    #Passenager on station drawing      Milose pls
    for i in range (len(WSLocationsH)):
        if SPassenagers[i][0]==0:
            pass
            #for j in range(1, len(SPassenagers[i])):
                #pg.draw.lines(screen, "White", True, ([WSLocationsW[j-1]+j*20, WSLocationsH[j-1]],[WSLocationsW[j-1]+j*20-5, WSLocationsH[j-1]+5], [WSLocationsW[j-1]+i*20, WSLocationsH[j-1]+7], [WSLocationsW[j-1]+j*20+5, WSLocationsH[j-1]-5]))
        for j in range(1, len(SPassenagers[i])):
            if SPassenagers[j][0]==3:
                pg.draw.circle(screen, "White", [WSLocationsW[j-1]+10+12*j, WSLocationsH[j-1]-5], 5)
    

    

    pg.display.update()
    clock.tick(60)   
