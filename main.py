import pygame
import json
pygame.init()
win=pygame.display.set_mode((1400,700))
blocknum=0#should be factor of 90
eqcheckindex=0
done=False
try :
    with open('levels.json','r') as lvldata:
        lvl=json.loads(lvldata.read())
except:
    print('Error in opening level file or converting into level')

try :
    with open('setting.json','r') as setdata:
        setting=json.loads(setdata.read())
except :
    
    print('Error in opening setting file ')

def bgmplayer(stat):
    if setting['sound']:
        if stat:
            pygame.mixer.music.load('musics/bgm.mp3')
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
            return
        else :
            pygame.mixer.music.stop()
            return
    return
def text(txt,col,siz):
    font= pygame.font.SysFont("Script", siz)
    mtxt = font.render(txt, False,col)
    return mtxt

def psound(name):
    if setting['sound']:
        if name=='die':
            die.play()
        elif name=='gate':
            gate.play()
        elif name=='key':
            key.play()
        elif name=='btn':
            btn.play()
    return
    
def lvlcheck(dirtlst,x):
    for grassb in dirtlst:
        if grassb.collidepoint(x):
            return True,dirtlst.index(grassb)
    else:
        return False,0
def selectlevel():
    global setting,lvl
    back= pygame.Rect(40,40,90,90) 
    soundrect = pygame.Rect(1280,30,150,100)
    shi=pygame.Rect(670,30,50,50)
    slo=pygame.Rect(675,100,50,50)
    jhi=pygame.Rect(1200,30,50,50)
    jlo=pygame.Rect(1205,100,50,50)
    changesound=False
    
    rects=[]
    while 1:
        win.blit(levelimg,(0,0))
        win.blit(text("Player Speed",(2,0,255),90),(170,50))
        win.blit(text("Jump Limit",(2,0,255),90),(760,50))
        win.blit(imgloder('num'+str((setting['speed'])),(60,60)),(580,40))
        win.blit(imgloder('up',(50,50)),(670,30))
        win.blit(imgloder('up',(50,50),rot=180),(675,100))
        
        win.blit(imgloder('num'+str((setting['jump'])),(60,60)),(1100,40))
        win.blit(imgloder('up',(50,50)),(1200,30))
        win.blit(imgloder('up',(50,50),rot=180),(1205,100))
        
        i=1
        for x in range(200,700,145):
            for y in range(110,1400,150):
                if i!=setting['level']:
                    win.blit(numbg,(y-40,x-40))
                else :
                    win.blit(clbg,(y-40,x-40))
                win.blit(text(str(i),(255,255,255),90),(y,x))
                rects.append(pygame.Rect(y-40,x-40,130,130))
                i+=1
        
        if not setting['sound']:
            win.blit(text("/",(255,0,0),180),(1340,10))
        
        if changesound :
            changesound=False
            if setting['sound']:
                setting['sound']=0
            else :
                setting['sound']=1
            with open('setting.json','w') as setdata:
                setdata.write(json.dumps(setting,indent=4))
            with open('setting.json','r') as setdata:
                setting=json.loads(setdata.read())
                
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if lvlcheck(rects,pos)[0]:
                    psound('btn')
                    beflvl=setting['level']
                    try :
                        setting['level']=lvlcheck(rects,pos)[1]+1
                        with open('setting.json','w') as setdata:
                            setdata.write(json.dumps(setting,indent=4))
                        with open('setting.json','r') as setdata:
                            setting=json.loads(setdata.read())
                        with open('levels.json','r') as lvldata:
                            lvl=json.loads(lvldata.read())
                        clvl=lvl[setting['level']-1]
                        print(clvl)
                    except :
                        setting['level']=beflvl
                        with open('setting.json','w') as setdata:
                            setdata.write(json.dumps(setting,indent=4))
                        with open('setting.json','r') as setdata:
                            setting=json.loads(setdata.read())
                        with open('levels.json','r') as lvldata:
                            lvl=json.loads(lvldata.read())
                    
                if back.collidepoint(pos):
                    psound('btn')
                    return
                elif soundrect.collidepoint(pos):
                    psound('btn')
                    changesound=True
                elif shi.collidepoint(pos) and setting['speed']!=7:
                    psound('btn')
                    setting['speed']+=1
                    with open('setting.json','w') as setdata:
                        setdata.write(json.dumps(setting,indent=4))
                    with open('setting.json','r') as setdata:
                        setting=json.loads(setdata.read())
                elif slo.collidepoint(pos) and setting['speed']!=0:
                    psound('btn')
                    setting['speed']-=1
                    with open('setting.json','w') as setdata:
                        setdata.write(json.dumps(setting,indent=4))
                    with open('setting.json','r') as setdata:
                        setting=json.loads(setdata.read())
                elif jhi.collidepoint(pos) and setting['jump']!=9:
                    psound('btn')
                    setting['jump']+=1
                    with open('setting.json','w') as setdata:
                        setdata.write(json.dumps(setting,indent=4))
                    with open('setting.json','r') as setdata:
                        setting=json.loads(setdata.read())
                elif jlo.collidepoint(pos) and setting['jump']!=2:
                    psound('btn')
                    setting['jump']-=1
                    with open('setting.json','w') as setdata:
                        setdata.write(json.dumps(setting,indent=4))
                    with open('setting.json','r') as setdata:
                        setting=json.loads(setdata.read())

def createlevel():
    back= pygame.Rect(60,40,90,90) 
    while 1:
        win.blit(bgimg,(0,0))
        win.blit(text("This feature is Currently not avilabel !",(255,0,25),100),(100,200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if back.collidepoint(pos):
                    psound('btn')
                    return

def credits():
    back= pygame.Rect(60,40,90,90) 
    txtlist=['Created By : Prashant Rawat','Age when this game created : 14 y','Date of Complete : 15/02/2023','Made in : 7 Days','Wish : A Laptop','Emails : learnehking@gmail.com ,','prashantrawat.coder@gmail.com','GitHub : PrashantRawatCoder']
    while 1:
        i=0
        win.blit(bgimg,(0,0))
        for x in range(40,640,80):
            win.blit(text(txtlist[i],(255-(x//3),0,205),100),(200,x))
            i+=1
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if back.collidepoint(pos):
                    psound('btn')
                    return 








def out(res):
    btnlist=[]
    btnlist.append(pygame.Rect(500,290,380,100))     
    btnlist.append(pygame.Rect(330,390,380,85))     
    btnlist.append(pygame.Rect(730,390,380,85))
    btnlist.append(pygame.Rect(330,480,380,85))
    btnlist.append(pygame.Rect(730,480,380,85)) 
    while 1:
        win.blit(outimg,(0,0))
        if res:
            win.blit(text('Yoooo... ! You Won !',(5,0,205),180),(150,140))
        else :
            win.blit(text('Oh No ! You Lost !',(5,0,205),200),(200,140))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if btnlist[0].collidepoint(pos):
                    psound('btn')
                    return True
                elif btnlist[1].collidepoint(pos):
                    psound('btn')
                    selectlevel()
                elif btnlist[2].collidepoint(pos):
                    psound('btn')
                    createlevel()
                elif btnlist[3].collidepoint(pos):
                    psound('btn')
                    credits()
                elif btnlist[4].collidepoint(pos):
                    psound('btn')
                    return False
        
        pygame.display.update()


def start():
    btnlist=[]
    btnlist.append(pygame.Rect(500,290,380,100))     
    btnlist.append(pygame.Rect(330,390,380,85))     
    btnlist.append(pygame.Rect(730,390,380,85))
    btnlist.append(pygame.Rect(330,480,380,85))
    btnlist.append(pygame.Rect(730,480,380,85)) 
    while 1:
        win.blit(startimg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if btnlist[0].collidepoint(pos):
                    psound('btn')
                    return True
                elif btnlist[1].collidepoint(pos):
                    psound('btn')
                    selectlevel()
                elif btnlist[2].collidepoint(pos):
                    psound('btn')
                    createlevel()
                elif btnlist[3].collidepoint(pos):
                    psound('btn')
                    credits()
                elif btnlist[4].collidepoint(pos):
                    psound('btn')
                    return False
        
        pygame.display.update()





def buttondraw(interf):
    btnlist=[]
    if interf==0:
        win.blit(iup,(1060,605))
        win.blit(ilef,(90,610))
        win.blit(irigt,(1280,580))
        btnlist.append(pygame.Rect(1020,560,200,150))     
        btnlist.append(pygame.Rect(50,560,200,150))     
        btnlist.append(pygame.Rect(1240,560,200,150))     
        #pygame.draw.rect(win,(25,20,255),btnlist[0])
        #pygame.draw.rect(win,(25,20,255),btnlist[1])
        #pygame.draw.rect(win,(25,20,255),btnlist[2])  
        
    return btnlist
def level(num):
    global blocknum,lvl
    blocklist=['sky','grass','dirt']
    img = blocklist[lvl[num-1]['block'][blocknum]]
    blocknum+=1
    return img

def objlevel(num):
    global blocknum,lvl
    blocklist=['','spike','door','odoor','','','','','','','10','11','12','13','14','15','16','17','18','19']
    img = blocklist[lvl[num-1]['objs'][blocknum]]
    blocknum+=1
    return img

def eqlevel(num):
    global blocknum,lvl
    blocklist=['20','21','22','23','24','25','26','27','28','29','skysmall','plus','minus','mul','div','equal','ques']
    img = blocklist[lvl[num-1]['equation'][blocknum]]
    blocknum+=1
    return img

def playerpos(num):
    global lvl
    img = lvl[num-1]['duckpos']
    keypos = lvl[num-1]['keypos']
    print(((keypos[0]*30),(keypos[1]*30)+45))
    return img[0]*30,(img[1]*30)+45,((keypos[0]*30),(keypos[1]*30)+45)

    
def drawgame(levl):
    blockSize = 90 #Set the size of the grid block
    global k                                                
    k=0
    drtlst=[pygame.Rect(0,0,1460,120),pygame.Rect(0,0,45,720),pygame.Rect(1460,0,100,720),pygame.Rect(0,715,1450,100)]
    for x in range(45, 1445, blockSize):
        for y in range(90, 700, blockSize):
            k+=1
            img=level(levl)
            if not done:
                if img=='dirt':
                    drtlst.append(pygame.Rect(x,y,90,90))
                elif img=='grass':
                    drtlst.append(pygame.Rect(x,y,90,90))
            win.blit(blockimg[img],(x,y))
            #rect = pygame.Rect(x, y, blockSize, blockSize)
            #pygame.draw.rect(win, (0,0,0), rect,1)
    return drtlst

def imgloder(path,size=[90,90],rot=0,flipx=False,flipy=False):
    return pygame.transform.flip(pygame.transform.rotate(pygame.transform.scale(pygame.image.load('img/'+path+'.png').convert_alpha(),size),rot),flipy,flipx)
 
def duckmov(dirtlst,x,y):
    for grassb in dirtlst:
        if grassb.collidepoint(x,y):
            return True
    else:
        return False
        
def duckmovrect(dirtlst,crect):
    for grassb in dirtlst:
        if pygame.Rect.colliderect(grassb,crect):
            return True,dirtlst.index(grassb)
    else:
        return False

#def numrectdet(dirtlst,crect):
#    for grassb in dirtlst:
#        if grassb!=0:
#            if pygame.Rect.colliderect(grassb,crect):
#                return dirtlst.index(grassb)

def objdraw(levl,blockslist):
    blockSize = 90 #Set the size of the grid block
    global blocknum,k,done
    blocknum=0
    k=0
    drtlst=[]
    doorcor=None
    numlst=[]
    numposlist=[]
    for x in range(45, 1445, blockSize):
        for y in range(90, 700, blockSize):
            k+=1
            img=objlevel(levl)
            if not done and pygame.Rect(x,y,90,90) not in blockslist and img!='':
                if img=='spike':
                    drtlst.append(pygame.Rect(x+10,y+50,40,40))
                    win.blit(blockimg[img],(x+10,y+50))
                elif img=='door' or img=='odoor' :
                    win.blit(blockimg[img],(x,y))
                    doorcor=pygame.Rect(x,y,90,90)
                else :
                    win.blit(blockimg[img],(x+20,y+20))
                    numlst.append(int(img))
                    numposlist.append(pygame.Rect(x+20,y+20,50,50))
                    
    done=False
    return drtlst,doorcor,numlst,numposlist

def numpos(level):
    blockSize = 90 #Set the size of the grid block
    global blocknum,k,done
    blocknum=0
    drtlst=[]
    for x in range(45, 1445, blockSize):
        for y in range(90, 700, blockSize):
            img=objlevel(level)
            if img in ('10','11','12','13','14','15','16','17','18','19'):
                drtlst.append(pygame.Rect(x+20,y+20,50,50))
            else :
                drtlst.append(pygame.Rect(0,0,0,0))    
    return drtlst

def equationdraw(levl):
    blockSize = 45 #Set the size of the grid block
    global blocknum,k
    blocknum=0
    k=0
    for y in range(0, 90, blockSize):
        for x in range(45, 1400, blockSize):
            k+=1
            img=eqlevel(levl)
            win.blit(blockimg[img],(x,y))
        
    return 

  
def eqnumget(level):
    global lvl
    result=[]
    eqs=list(filter((10).__ne__,lvl[level-1]['equation'][:]))
    for i in range(0,(len(eqs)//5)):
        result.append(None)
    return result

def equationcheck(numgot,level):
    global lvl
    if None in numgot:
        checkno=numgot.index(None)-1
    else :
        checkno = len(numgot)-1
        
    cheacking=list(filter((10).__ne__,lvl[level-1]['equation'][:]))[checkno*5:(checkno+1)*5]
    print(numgot)
    if None in numgot :
        if cheacking[1]==11:
             if cheacking[0]+cheacking[2]==cheacking[4]:
                 return False,False
             else :
                 return True,False
        if cheacking[1]==12:
             if cheacking[0]-cheacking[2]==cheacking[4]:
                 return False,False
             else :
                 return True,False
        if cheacking[1]==13:
             if cheacking[0]*cheacking[2]==cheacking[4]:
                 return False,False
             else :
                 return True,False
        if cheacking[1]==14:
             if cheacking[0]/cheacking[2]==cheacking[4]:
                 return False,False
             else :
                 return True,False
    else :
        if cheacking[1]==11:
             if cheacking[0]+cheacking[2]==cheacking[4]:
                 return False,True
             else :
                 return True,False
        if cheacking[1]==12:
             if cheacking[0]-cheacking[2]==cheacking[4]:
                 return False,True
             else :
                 return True,False
        if cheacking[1]==13:
             if cheacking[0]*cheacking[2]==cheacking[4]:
                 return False,True
             else :
                 return True,False
        if cheacking[1]==14:
             if cheacking[0]/cheacking[2]==cheacking[4]:
                 return False,True
             else :
                 return True,False


def main():
    global win,lvl,blocknum,duckani,eqcheckindex,done,setting
    with open('levels.json','r') as lvldata:
        lvl=json.loads(lvldata.read())
    a=setting['speed']
    jumplimit=setting['jump']
    if a==0:
        change=3
    elif a==1 :
        change=9
    elif a==2:
        change=10
    elif a==3 :
        change=15
    elif a== 4:
        change=18
    elif a==5 :
        change=30
    elif a== 6:
        change=45
    elif a==7 :
        change=90
    playerspeed=change
    blocknum=0
    eqcheckindex=0
    done=False
    duckani=0
    levelno=setting['level']
    duckposx,duckposy,keypos=playerpos(levelno)
    numgot=eqnumget(levelno)
    numposcheck=numpos(levelno)
    keyrect=pygame.Rect(0,0,0,0)
    out=False
    victory=False
    dooropen=False
    game='Some Error occured'
    countdown=0
    left=False
    right=False
    flipy=False
    duckfell=True
    jump=False
    jumpno=0
    blocknum=0
    cancelrect=pygame.Rect(1400,100,60,60)
    
    bgmplayer(1)
    while 1:
        #if win.get_size()==(720,1469):
            #win=pygae.transform.rotate(win,90)
        
        
        
        win.fill((0,0,0))
        dirtlst=drawgame(levelno)
        spikes,door,numlist,numposlist=objdraw(levelno,dirtlst)
        duckfell=not duckmovrect(dirtlst,(duckposy+42,duckposx+180,15,15))
        duckrect=pygame.Rect((duckposy)+5,(duckposx+90),80,90)
        equationdraw(levelno)
        
        
        if duckmovrect([keyrect],duckrect) and not dooropen:
            psound('key')
            lvl[levelno-1]['objs'][lvl[levelno-1]['objs'].index(2)]=3
            dooropen=True
            psound('gate')
        if victory and not dooropen:
            win.blit(blockimg['key'],keypos)
            keyrect=pygame.Rect(keypos[0],keypos[1],50,50)                                                                             
        if not out and not (dooropen and duckmovrect([door],duckrect)):
            win.blit(imgloder('duck',flipy=flipy),(duckposy,(duckposx)+90))
            out=duckmovrect(spikes,duckrect)       
        if dooropen and duckmovrect([door],duckrect) :
             if countdown<10:
                 win.blit(imgloder('duck',(90-countdown*4,90-countdown*4),flipy=flipy,rot=(countdown+1)*36),(door[0]+15,door[1]+15))
                 duckfell=False
                 jump=False
                 left=False
                 right=False
                 if countdown==1:
                     duckposx-=30
                 #
                 
                 countdown+=1
             else:
                 bgmplayer(0)
                 return True
        elif out:
            if countdown<10:
                win.blit(imgloder('duck',(90-countdown*4,90-countdown*4),flipy=flipy,rot=(countdown+1)*36),(duckposy,(duckposx)+90))
                duckfell=False
                jump=False
                left=False
                right=False
                if countdown==1:
                    duckposx-=30 
                countdown+=1
            else:
                psound('die')
                bgmplayer(0)
                return False
        #pygame.draw.rect(win,(10,200,255),(duckposy+30,(duckposx)+90,20,90))
        if duckmovrect(numposlist,pygame.Rect(duckposy+30,(duckposx)+90,20,90)) and None in numgot:
            lvl[levelno-1]['objs'][duckmovrect(numposcheck,pygame.Rect(duckposy+30,(duckposx)+90,20,90))[1]]=0
            #lvl[levelno-1]['objs'].index(numlist[duckmovrect(numposlist,duckrect)[1]])
            numgot[numgot.index(None)] =numlist[duckmovrect(numposlist,duckrect)[1]]-10
            psound('key')
            if None in numgot:
                changenum=numgot[numgot.index(None)-1]
            else :
                changenum = numgot[::-1][0]
            lvl[levelno-1]['equation'][lvl[levelno-1]['equation'].index(16)]=changenum
            
            out,victory=equationcheck(numgot,levelno)
        
        win.blit(cancel,(1400,100))
        if left and not duckmov(dirtlst,(duckposy)-5,(duckposx+150)):
             duckposy-=playerspeed
            #pygame.draw.rect(win,(9,98,234),(duckposy-5,duckposx+150,5,5))
        elif right and not duckmov(dirtlst,(duckposy)+100,(duckposx+150)):
            duckposy+=playerspeed
            #pygame.draw.rect(win,(9,98,234),(duckposy+100,duckposx+150,5,5))
        if duckmov(dirtlst,(duckposy)+40,(duckposx)+90):
            jump=False
        if jump :
            jumpno+=1
            duckposx-=playerspeed
            if jumpno>=jumplimit:
                jump=False
                jumpno=0
        if duckfell and not jump:
            duckposx+=playerspeed;
        
        buttons=buttondraw(0)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                
                if buttons[0].collidepoint(pos):
                    psound('btn')
                    jump=True
                if buttons[1].collidepoint(pos):
                    psound('btn')
                    left=True
                    flipy=False
                elif buttons[2].collidepoint(pos):
                    psound('btn')
                    right=True
                    flipy=True
                elif cancelrect.collidepoint(pos):
                    psound('btn')
                    bgmplayer(0)
                    return False
            elif event.type == pygame.MOUSEBUTTONUP:
                left=False
                right=False
                
        pygame.display.update()
        duckfell=True
        blocknum=0


if __name__=='__main__':
    
    die=pygame.mixer.Sound('musics/pdie.mp3')
    gate=pygame.mixer.Sound('musics/gate.wav')
    key=pygame.mixer.Sound('musics/key.wav')
    btn=pygame.mixer.Sound('musics/btn.wav')
    
    
    iup=imgloder('up',(100,80))
    ilef=imgloder('up',(100,80),90)
    irigt=imgloder('up',(100,80),270)
    startimg=imgloder('start',(1469,720))
    outimg=imgloder('out',(1469,720))
    bgimg=imgloder('bg',(1469,720))
    levelimg=imgloder('levelbg',(1469,720))
    cancel=imgloder('cancel',(60,60))
    numbg=imgloder('numbg',(130,130))
    clbg=imgloder('clbg',(130,130))
    blockimg={'grass':imgloder('grass'),'dirt':imgloder("dirt"),"sky":imgloder('sky'),'spike':imgloder('sharp',(40,40)),"door":imgloder('lockeddoor',(90,90)),"odoor":imgloder('door',(90,90)), '10':imgloder('num0',(50,50)),'11':imgloder('num1',(50,50)),'12':imgloder('num2',(50,50)),'13':imgloder('num3',(50,50)),'14':imgloder('num4',(50,50)),'15':imgloder('num5',(50,50)),'16':imgloder('num6',(50,50)),'17':imgloder('num7',(50,50)),'18':imgloder('num8',(50,50)),'19':imgloder('num9',(50,50)),'plus':imgloder('plus',(45,45)),'minus':imgloder('minus',(45,45)),'mul':imgloder('mul',(45,45)),'div':imgloder('div',(45,45)),'equal':imgloder('equal',(45,45)),'ques':imgloder('ques',(45,45)),'20':imgloder('num0',(45,45)),'21':imgloder('num1',(45,45)),'22':imgloder('num2',(45,45)),'23':imgloder('num3',(45,45)),'24':imgloder('num4',(45,45)),'25':imgloder('num5',(45,45)),'26':imgloder('num6',(45,45)),'27':imgloder('num7',(45,45)),'28':imgloder('num8',(45,45)),'29':imgloder('num9',(45,45)),'key':imgloder('key'),"skysmall":imgloder('sky',(45,45))}
    
    if start():
        while 1:
            if out(main()):
                continue
            break
    pygame.quit()