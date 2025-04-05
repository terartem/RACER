from pygame import *
from random import randint
window = display.set_mode((700,500))
display.set_caption('ГОНКИ')
Racer = transform.scale(image.load("racer.png"),(700,500))


clock = time.Clock()
FPS = 60

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
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x  > 10:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y  > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y  < 455:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update_1(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = -60
            self.rect.x = randint(30,130)
            self.rect.y = 0
    def update_2(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = -60
            self.rect.x = randint(160,260)
            self.rect.y = 0
    def update_3(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = -60
            self.rect.x = randint(290,390)
            self.rect.y = 0
    def update_4(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = -60
            self.rect.x = randint(420,520)
            self.rect.y = 0
    def update_5(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = -60
            self.rect.x = randint(550,650)
            self.rect.y = 0
    
          




car_player = Player('car_player.png',300,430,90,100,6)
car_enemy1 = Enemy('car_e1.png', randint(30,130),-60,95,110,randint(1,5))
car_enemy2 = Enemy('car_e1.png',randint(160,260),-60,95,110,randint(1,5))
car_enemy3 = Enemy('car_e1.png', randint(290,390),-60,95,110,randint(1,5))
car_enemy4 = Enemy('car_e1.png',randint(420,520),-60,95,110,randint(1,5))
car_enemy5 = Enemy('car_e1.png',randint(550,650),-60,95,110,randint(1,5))












finish = False
game = True
while game:
    if finish != True:
        window.blit(Racer,(0,0))

        








        car_player.reset()
        car_player.update()

        car_enemy1.reset()
        car_enemy1.update_1()
        car_enemy2.update_2()
        car_enemy2.reset()
        car_enemy3.update_3()
        car_enemy3.reset()
        car_enemy4.update_4()
        car_enemy4.reset()
        car_enemy5.update_5()
        car_enemy5.reset()




    for e in event.get():
        if e.type == QUIT:
            game =  False
        elif e.type == KEYDOWN:
            if e.key == K_r and finish == True:
                car_enemy1.rect.y = -60
                car_enemy2.rect.y = -60
                car_enemy3.rect.y = -60
                car_enemy4.rect.y = -60
                car_enemy5.rect.y = -60



    clock.tick(FPS)
    display.update()