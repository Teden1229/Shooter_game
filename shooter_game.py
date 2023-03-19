from pygame import *
from random import randint

wight = 1380
height = 720

font.init()
#font2 = font.Font('Callibri','Italic')

w = display.set_mode((wight,height))
display.set_caption('Шутир')
background = transform.scale(image.load('galaxy.jpg'),(wight,height))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

class Game7up(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        w.blit(self.image, (self.rect.x, self.rect.y))

lost = 0 

class Enemy(Game7up):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>height:
            self.rect.y = 0
            self.rect.x = randint(100,wight-100)
            lost = lost + 1

#text.lose = font2.render("Пропущенно:"  + str(lost), 1, (255, 255, 255))

class Player(Game7up):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < wight - 80:
            self.rect.x += self.speed
        

        def fire(self):
            pass

run = True
player = Player('rocket.png', 5, height-100, 10)
enemy = Enemy('ufo.png',randint(100,wight-100),0,randint(1,5))



Clock = time.Clock()
FPS = 144


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    w.blit(background,(0,0))
    player.update()
    player.reset()
    enemy.update()
    enemy.reset()
    display.update()
    time.delay(50)
    праовавпваипоповпдтавориовтпдватопрвлтлатпо

