import pygame
import time
import random
import os
pygame.init()

WIDTH = 1750
HEIGHT = 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Phoenix Escape")
DIRT = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'DIRT.png')), (1750, 1750))
ground1 = DIRT.get_rect()
ground1.topleft = (0, 400)
ground2 = DIRT.get_rect()
ground2.topleft = (1750, 400)

BIRD = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'BIRD.png')), (100, 100))
player = BIRD.get_rect()
player.top = 750

FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_UP]: 
        if player.top>0: player.move_ip(0, -20)
    if key[pygame.K_DOWN]:
        if player.bottom<850: player.move_ip(0, 20)
    if key[pygame.K_RIGHT]: 
        if player.right<1350: player.move_ip(20, 0)
    if key[pygame.K_LEFT]: 
        if player.left>0: player.move_ip(-20, 0)

    ground1.left-=10
    ground2.left-=10

    if(ground2.left<=0): ground1.left = ground2.right
    if(ground1.left<=0): ground2.left = ground1.right

    
    screen.fill((116, 148, 164))
    screen.blit(DIRT, ground1)
    screen.blit(DIRT, ground2)
    screen.blit(BIRD, player)
    pygame.display.update()
    clock.tick(FPS)