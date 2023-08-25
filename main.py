from typing import Any
from pygame import*
init()

w = 800
h = 500
back = (0, 0, 0)

window = display.set_mode((w, h))
display.set_icon(image.load('tenis_ball.png'))
display.set_caption("ping pong 1vs1")
window.fill(back)
game = True
finish = False

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.size_x = player_x
        self.size_y = player_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update_l(self):
        key_presed = key.get_pressed()
        if key_presed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        key_presed = key.get_pressed()
        if key_presed[K_s] and self.rect.y < h-self.size_y:
            self.rect.y += self.speed
            

    def update_r(self):
        pass

rokcket1 = Player('racket.png', 10, w/3, 50, 150, 5)



class Ball():
    pass

while game:
    time.delay(5)
    window.fill(back)
    rokcket1.reset()
    rokcket1.update_l()
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()