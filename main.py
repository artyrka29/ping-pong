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
font.init()
""""ШРИФТИ"""
f1 = font.SysFont(None, 70, bold =True)
f2 = font.SysFont(None, 50)
""""КЛАСИ"""
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.size_x = size_x
        self.size_y = size_y
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
        if key_presed[K_s] and self.rect.y < h-self.size_y:
            self.rect.y += self.speed

    
    def update_r(self):
        key_presed = key.get_pressed()
        if key_presed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_presed[K_DOWN] and self.rect.y < h-self.size_y:
            self.rect.y += self.speed


rokcket1 = Player('racket.png', 10, w/3, 50, 150, 5)
rokcket2 = Player('racket.png', w - 60, h/3, 50, 150, 5)
ball = GameSprite('tenis_ball.png', w/2, h/2, 50, 50, 7)

speed_x, speed_y = 4, 4

point1, point2 = 0, 0

game = True
finish = False
while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    point1_txt = f1.render(str(point2), True, (255, 255, 255))
    point2_txt = f1.render(str(point2), True, (255, 255, 255))
    window.blit(point1_txt, (50, 20))
    window.blit(point2_txt, (750, 20))
    if not finish:
        time.delay(10)
        rokcket1.reset()
        rokcket1.update_l()
        rokcket2.reset()
        rokcket2.update_r()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y <0 or ball.rect.y > h-50:
            speed_y *= -1

        if sprite.collide_rect(ball, rokcket1) or sprite.collide_rect(ball, rokcket2):
            speed_x *= -1

        if ball.rect.x > w-50:
            point1 += 1
            ball.rect.x = w/2
            ball .rect.y = h/2

        if ball.rect.x > w-50:
            point2 += 1
            ball.rect.x = w/2
            ball .rect.y = h/2


    display.update()