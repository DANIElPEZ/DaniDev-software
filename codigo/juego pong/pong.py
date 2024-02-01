import pygame as pg
pg.init()
pg.display.set_caption("PONG V9999999999999.999999999999999XXXXXXXXXXXDDDDDDDDDDDD")
ventana=pg.display.set_mode((900,500))
y1=205
y2=205
sy1=0
sy2=0
px=450
py=240
spx=3
spy=2
reloj=pg.time.Clock()
fuente=pg.font.SysFont("Arial",20)
win=pg.font.SysFont("Arial",30)
winjp2=win.render("",True,(230,45,137))
winjp1=win.render("",True,(230,45,137))
c=True
begin=0
reset=0
jp1,jp2=0,0
while c:
    for evt in pg.event.get():
        if evt.type==pg.QUIT:
            c=False
        if evt.type==pg.KEYDOWN:
            if evt.key==pg.K_o:
                sy2=-7
                begin=1
            if evt.key==pg.K_l:
                sy2=7
                begin=1
            if evt.key==pg.K_w:
                sy1=-7
                begin=1
            if evt.key==pg.K_s:
                sy1=7
                begin=1
            if evt.key==pg.K_b:
                reset=1
        if evt.type==pg.KEYUP:
            if evt.key==pg.K_o:
                sy2=0
                begin=1
            if evt.key==pg.K_l:
                sy2=0
                begin=1
            if evt.key==pg.K_b:
                begin=1
            if evt.key==pg.K_s:
                sy1=0
                begin=1
            if evt.key==pg.K_b:
                reset=1
        y1+=sy1
        y2+=sy2
    if py<0 or py>500:
        spy*=-1
    if px<0 or px>900:
        px,py=450,240
        begin=0
    if px<1:
        jp2+=1
    if px>899:
        jp1+=1
    if jp2==5:
        winjp2=win.render("Gano el jugador 2---------->",True,(230,45,137))
    if jp1==5:
        winjp1=win.render("<----------Gano el jugador 1",True,(230,45,137))
    if reset==1:
        winjp2=win.render("",True,(230,45,137))
        winjp1=win.render("",True,(230,45,137))
        jp1,jp2=0,0
        reset=0
    jp1t=str(jp1)
    jp2t=str(jp2)
    texto1=fuente.render(jp1t,True,(0,255,0))
    texto2=fuente.render(jp2t,True,(0,255,0))
    if begin==1:
        px+=spx
        py+=spy
    ventana.fill((0,0,0))
    #dibujo
    rect1=pg.draw.rect(ventana,(255,255,255),(25,y1,20,100))
    rect2=pg.draw.rect(ventana,(255,255,255),(855,y2,20,100))
    pelota=pg.draw.circle(ventana,(255,255,255),[px,py],10)
    #colisiones
    if pelota.colliderect(rect1) or pelota.colliderect(rect2):
        spx*=-1
    ventana.blit(texto1,(430,20))
    ventana.blit(texto2,(470,20))
    ventana.blit(winjp2,(550,240))
    ventana.blit(winjp1,(60,240))
    pg.display.flip()
    reloj.tick(60)
pg.quit()