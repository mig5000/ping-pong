from pygame import *
window = display.set_mode((1000,950))
display.set_caption("a")
clock = time.Clock()
FPS = 120

back = transform.scale(image.load("1.jpg"),(1000,950))


class Player1(sprite.Sprite):
    def __init__(self,speed,imagename,x,y):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(imagename),(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(Player1):
    def __init__(self,speed,imagename,x,y):
        super().__init__(speed,imagename,x,y)

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y += 10

        if keys[K_DOWN]:
            self.rect.y -= 10

class Enemy(Player):
    def __init__(self,speed,imagename,x,y):
        super().__init__(speed,imagename,x,y)




herom = Player(10,'dunlop-blackstorm-Ракетка-для-настольного-тенниса.jpg',500,500)
en = Enemy(10,'dunlop-blackstorm-Ракетка-для-настольного-тенниса.jpg',0,0)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(back,(0,0))
    display.update()
    clock.tick(FPS)
    herom.reset()
    herom.update()
    en.reset()
    en.update()