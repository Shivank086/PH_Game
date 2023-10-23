import pygame, sys, time, random, colorsys, math, os
from pygame.math import Vector2
from pygame.locals import *
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PH run")

score = 0
pX = WIDTH/8
pY = HEIGHT/2
baseX = 0
lv = 1
ROCKT = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ROCK.png')), (60, 400)).convert_alpha()
ROCKL = pygame.transform.rotate(ROCKT, 180).convert_alpha()
HITBOX = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'HITBOX.png')), (60, 400)).convert_alpha()
NUMBERS = [
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ZERO.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'ONE.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'TWO.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'THREE.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'FOUR.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'FIVE.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'SIX.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'SEVEN.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'EIGHT.png')), (65, 65)),
    pygame.transform.scale(pygame.image.load(os.path.join('assets', 'NINE.png')), (65, 65))
]
PLAYER = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'BIRD.png')), (65, 65))


DIRT = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'DIRT.png')), (WIDTH, WIDTH))
ground1 = DIRT.get_rect()
ground1.topleft = (0, 520)
ground2 = DIRT.get_rect()
ground2.topleft = (WIDTH, 520)
ground3 = DIRT.get_rect()
ground3.topleft = (2*WIDTH, 520)

height = ROCKL.get_height()

def getRandomRock():
    y2 = random.randint(70, 470)
    rockX = WIDTH+10
    y1 = height - y2 + 200
    print(-y2)
    return [
        {'x': rockX, 'y': -y2},
        {'x': rockX, 'y': y1}
    ]

rock1 = getRandomRock()
rock2 = getRandomRock()
rock3 = getRandomRock()
rock4 = getRandomRock()
diff = 1
topRock = [
    {'x': WIDTH+200, 'y': rock1[0]['y']},
    {'x': WIDTH*3/2+200, 'y': rock2[0]['y']},
    {'x': WIDTH*2+200, 'y': rock3[0]['y']},
    {'x': WIDTH*5/2+200, 'y': rock4[0]['y']}
]

bottomRock = [
    {'x': WIDTH+200, 'y': rock1[1]['y']},
    {'x': WIDTH*3/2+200, 'y': rock2[1]['y']},
    {'x': WIDTH*2+200, 'y': rock3[1]['y']},
    {'x': WIDTH*5/2+200, 'y': rock4[1]['y']}
]

speed = -8
pSpeed = -9


def isCollison(pX, pY, topRocks, bottomRocks):
    if pY>450: return True
    
    for rock in topRocks:
        if (pY < height + rock['y']) and (abs(pX - rock['x']) < ROCKT.get_width() - 15): return True
    
    for rock in bottomRocks:
        if (pY > rock['y']) and (abs(pX - rock['x']) < ROCKL.get_width() - 15): return True
    return False



FPS = 8*(lv+3)
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            if pY>20: pSpeed=-10
    
    screen.fill((116, 148, 164))

    run = not isCollison(pX, pY, topRock, bottomRock)

    pMid = pX+PLAYER.get_width()/2
    for rock in topRock:
        rMid = rock['x'] + ROCKL.get_width()/2
        if rMid <= pMid < rMid-speed: score+=1

    if pSpeed<15: pSpeed+=1
    pY += pSpeed

    PLAYER = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join('assets', 'BIRD.png')), (65, 65)), -1.5*pSpeed)


    for tRock, bRock in zip(topRock, bottomRock):
        tRock['x'] += speed
        bRock['x']  += speed
    
    ground1.left+=speed
    ground2.left+=speed
    ground3.left+=speed
    
    if topRock[0]["x"] < -ROCKL.get_width():  
        topRock.pop(0)
        bottomRock.pop(0)
        newRock = getRandomRock()
        topRock.append({'x': topRock[2]["x"]+WIDTH/2, 'y': newRock[0]['y']})
        bottomRock.append({'x': topRock[2]["x"]+WIDTH/2, 'y': newRock[1]['y']})

    
    if(ground1.left<=0): ground3.left = ground2.right
    if(ground2.left<=0): ground1.left = ground3.right
    if(ground3.left<=0): ground2.left = ground1.right
    
    for tRock, bRock in zip(topRock, bottomRock):
        screen.blit(ROCKT, (tRock['x'], tRock['y']))
        screen.blit(ROCKL, (bRock['x'], bRock['y']))
    
    
    screen.blit(DIRT, ground1)
    screen.blit(DIRT, ground2)
    screen.blit(DIRT, ground3)
    
    screen.blit(PLAYER, (pX, pY))

    digits = [int(x) for x in list(str(score))]
    width = 0
    for digit in digits:
        width += NUMBERS[digit].get_width()
    offset = (WIDTH-width)
 
    for digit in digits:
        screen.blit(NUMBERS[digit], (offset, 0))
        offset += NUMBERS[digit].get_width()

    if score == 5+lv*5: run = False
    pygame.display.update()
    clock.tick(FPS)

    
