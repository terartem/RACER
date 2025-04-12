from pygame import *
from random import randint
window = display.set_mode((900,600))
display.set_caption('ГОНКИ')
Racer = transform.scale(image.load("racer.png"),(900,600))


clock = time.Clock()
FPS = 60
normx = [20, 320, 600]




class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_width,player_height,player_speed):
        super().__init__()
        self.image =transform.scale(image.load(player_image),(player_width,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    def colliderect(self,sprite):
        return self.rect.colliderect(sprite.rect)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x  > 100:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y  > 5:
            self.rect.y -= self.speed
        
     

class Enemy(GameSprite):
    def update_1(self):
        global normx
        num = randint(0, 2)
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = -215
            self.rect.x = normx[num]
    def update_2(self):
        global normx
        num = randint(0, 2)
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = -215
            self.rect.x = normx[num]

   

          




car_player = Player('car_player.png',300,300,120,220,200)
car_enemy1 = Enemy('car_e1.png', randint(30,200),-220,150,215,randint(2,5))
car_enemy2 = Enemy('car_e1.png',randint(230,400),-220,150,215,randint(2,5))






font.init()
font1 = font.SysFont('Arial',30)
ticks = 0


finish = False
game = True
while game:
    if finish != True:
        window.blit(Racer,(0,0))

        








        car_player.reset()
        if ticks > 15:
            car_player.update()
            ticks=0
        else:
            ticks +=1


        car_enemy1.reset()
        car_enemy1.update_1()
        car_enemy2.update_2()
        car_enemy2.reset()
       
        if car_player.colliderect(car_enemy1) or (car_enemy2):
            lose = font1.render('ТЫ ПРОИГРАЛ!!!!!!!!!!!!!!!!!!!!!!!!!!!!',60,(230,0,0))
            window.blit(lose,(300,200))




    for e in event.get():
        if e.type == QUIT:
            game =  False
        elif e.type == KEYDOWN:
            if e.key == K_r and finish == True:
                car_enemy1.rect.y = -220
                car_enemy2.rect.y = -220
              



    clock.tick(FPS)
    display.update()