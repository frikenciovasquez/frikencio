#actualizacion del proyecto con implementacion de generacion de neemigos y deciones aleatoriamente

import pygame
from random import randint
#Dibuja triangulo y lo escala con el teclado
ANCHO=1200
ALTO=600
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
focus=randint(1,2)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, accion=0):
        pygame.sprite.Sprite.__init__(self)
        self.accion=accion
        self.i=0
        self.image=pygame.Surface([40,100])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.rect.x=50
        self.rect.y=470
        self.focus=1

    def update(self):
        self.rect.y+=self.vel_y
        if self.rect.y>=(ALTO-self.rect.height):
            self.rect.y=ALTO-self.rect.height
            self.vel_y=0
        self.rect.x+=self.vel_x

class Jugador2(pygame.sprite.Sprite):
    def __init__(self, accion=0):
        pygame.sprite.Sprite.__init__(self)
        self.accion=accion
        self.i=0
        self.image=pygame.Surface([40,100])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.vel_y=0
        self.rect.x=145
        self.rect.y=320
        self.focus=2

    def update(self):
        self.rect.y+=self.vel_y
        if self.rect.y>=(ALTO-self.rect.height):
            self.rect.y=ALTO-self.rect.height
            self.vel_y=0
        self.rect.x+=self.vel_x

class Enemigo1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.i=0
        self.image=pygame.Surface([40,100])
        self.image.fill(NEGRO)
        self.rect=self.image.get_rect()
        self.vel_x=3
        self.vel_y=0
        self.rect.x=605
        self.rect.y=385
        self.salud=100
        self.vivo=1
        self.espera=500

    def update (self):
        if self.vivo==1:
            self.espera-=2
            #print self.espera
            #print focus
            if self.espera<=0:
            #self.rect.x +=5
                self.rect.x += self.vel_x
                self.rect.y+= self.vel_y
                #self.vel_x=0
                if focus==1:
                    if self.rect.x > j.rect.x:
                        self.vel_x=-1.5
                    if self.rect.x < j.rect.x:
                        self.vel_x=1.5
                    if self.rect.y < j.rect.y:
                        self.vel_y=1.5
                    if self.rect.y > j.rect.y:
                        self.vel_y=-1.5
                    if self.rect.y == j.rect.y:
                        self.vel_y=0
                    if self.rect.x == j.rect.x:
                        self.vel_x=0
                if focus==2:
                    if self.rect.x > j2.rect.x:
                        self.vel_x=-1.5
                    if self.rect.x < j2.rect.x:
                        self.vel_x=1.5
                    if self.rect.y < j2.rect.y:
                        self.vel_y=1.5
                    if self.rect.y > j2.rect.y:
                        self.vel_y=-1.5
                    if self.rect.y == j2.rect.y:
                        self.vel_y=0
                    if self.rect.x == j2.rect.x:
                        self.vel_x=0


class Enemigo2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.i=0
        self.image=pygame.Surface([100,40])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.vel_x=3
        self.vel_y=0
        self.rect.x=-1250
        self.rect.y=385
        self.espera=0
        self.vivo=1

    #def uptade(self):
    def update (self):
        if self.vivo==1:
            #print self.rect.x
            self.espera-=2
            #print self.espera

            if self.espera<=0:
                self.rect.x -=5

if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fondo=pygame.image.load('fondo.png')
    fondo2=pygame.image.load('fondo2.png')
    pygame.display.flip()
    pantalla.blit(fondo,[0,-500])
    pantalla.blit(fondo2,[0,-500])
    reloj=pygame.time.Clock()
    todos=pygame.sprite.Group()

    #juador1
    jugador=pygame.sprite.Group()
    j=Jugador()
    todos.add(j)
    #jugador2
    jugador2=pygame.sprite.Group()
    j2=Jugador2()
    todos.add(j2)
    #enemigos
    enemigos=pygame.sprite.Group()
    e1=Enemigo1()
    e1.vel_x=5
    todos.add(e1)
    enemigos.add(e1)
    cantidad_enemigos=randint(5,100)
    for i in range(cantidad_enemigos):
        e2=Enemigo2()
        e2.rect.x=1250*i
        e2.rect.y=randint(ALTO-300,ALTO-100)
        todos.add(e2)
        enemigos.add(e2)

    print e2.rect.y
    fin=False
    info=fondo.get_rect()
    #print info
    pos_x=0
    pos_y=-500
    varx=-2
    vary=-2
    pista=pygame.mixer.Sound('musica.ogg')
    pista.play()
    x=0
    i=0
    while not fin:
        pos=pygame.mouse.get_pos()
        print pos
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_RIGHT:
                    j.vel_x=10

                if event.key==pygame.K_LEFT:
                    j.vel_x=-10
                if event.key==pygame.K_UP:
                    j.vel_y-=10
                if event.key==pygame.K_DOWN:
                    j.vel_y=10

                if event.key==pygame.K_d:
                    j2.vel_x=10

                if event.key==pygame.K_a:
                    j2.vel_x=-10
                if event.key==pygame.K_w:

                    j2.vel_y=-10
                if event.key==pygame.K_s:
                    j2.vel_y=10


                if event.key==pygame.K_p:
                    j.accion=1
                    j.i=0

                elif j2.rect.y<=10 and pos_y<0:
                    print pos_y


            if event.type== pygame.KEYUP:
                j.vel_x=0
                j.vel_y=0
                j2.vel_y=0
                j2.vel_x=0
                j.accion=0

        if j.rect.x>=(ANCHO-300)and pos_x>=-1000:
            pos_x-=10
            j.vel_x-=1
            if j.rect.x>=ANCHO-160:
                j.vel_x-=1

        if j.rect.x<=250 and pos_x<0:
            pos_x+=10
            if j.rect.x<15:
                j.vel_x=+1

        if j.rect.bottom <= 365 and j.rect.bottom<= ALTO:
            #pos_y=-2
            #j.vel_y=0
            pass
        if j.rect.y<=10 and pos_y<0:
            print pos_y

#------------------------------------------------------------------
        if j2.rect.x>=(ANCHO-300)and pos_x>=-1000:
            pos_x-=10
            j2.vel_x-=1
            if j2.rect.x>=ANCHO-160:
                j2.vel_x-=1

        if j2.rect.x<=250 and pos_x<0:
            pos_x+=10
            if j2.rect.x<15:
                j2.vel_x=+1

        if j2.rect.bottom <= 365 and j2.rect.bottom<= ALTO:
            #pos_y=-2
            #j.vel_y=0
            pass
        if j2.rect.y<=10 and pos_y<0:
            print pos_y



        if j.accion==1:
            #print '111111'
            ls_col=pygame.sprite.spritecollide(j,enemigos,False)
            for e in ls_col:
                if e.rect.center>=(j.rect.bottom-25):
                    e.salud-=10
                    print e.salud
                    if e.salud<=0:
                        enemigos.remove(e1)
                        todos.remove(e1)

                    e.rect.x+=10

                    #print '22222222', e.rect.x
                #if e1.rect.bottom>=(j1.rect.bottom-25):
                    #e1.rect.x+=20




        enemigos.update()
        todos.update()
        #print e1.rect.x
        pantalla.fill(NEGRO)
        pantalla.blit(fondo2,[0,-500])
        pantalla.blit(fondo,[pos_x,pos_y])
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
