from pygame import *
window = display.set_mode((700,500))
display.set_caption('АРТЁЁЁЁЁМ')
Racer = transform.scale(image.load("racer.png"),(700,500))


clock = time.Clock()
FPS = 60





finish = False
game = True
while game:
    if finish != True:
        window.blit(Racer,(0,0))





    for e in event.get():
        if e.type == QUIT:
            game =  False


    clock.tick(FPS)
    display.update()