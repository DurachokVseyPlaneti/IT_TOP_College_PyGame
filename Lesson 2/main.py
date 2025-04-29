import random

import pygame as pg

pg.init()
SIZE = WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode(SIZE)

from src.coin import Coin, Bomb, Heart
from src.patrick import Patrick
from src.utils import load_image

FPS = 60
BACKGROUND = pg.transform.smoothscale(load_image('back.jpg'), SIZE)

clock = pg.time.Clock()
running = True

all_sprites = pg.sprite.Group()
items_group = pg.sprite.Group()
player = Patrick(all_sprites)
player.rect.bottom = HEIGHT
player.rect.centerx = WIDTH / 2

font = pg.font.Font(None, 50)

while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
    screen.blit(BACKGROUND, (0, 0))
    if random.random() < 0.02:
        Coin(all_sprites, items_group)
    if random.random() < 0.005:
        Bomb(all_sprites, items_group)
    if random.random() < 0.002:
        Heart(all_sprites, items_group)
    all_sprites.draw(screen)
    all_sprites.update(events)
    player.collide(items_group)

    screen.blit(font.render(player.coins, True, '#116834'), (10, 10))
    screen.blit(font.render(player.health, True, '#FF16CB'), (10, 60))

    pg.display.flip()
    clock.tick(FPS)
pg.quit()