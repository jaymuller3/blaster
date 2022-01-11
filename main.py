import math
import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# Text
font = pygame.font.Font('freesansbold.ttf', 120)
vicTextX = 120
vicTextY = 220

lossTextX = 80
lossTextY = 220

contTextX = 30
contTextY = 220

def show_victory(x, y):
    victory = font.render("YOU WIN!", True, (255,255,255))
    screen.blit(victory, (x,y))


def show_loss(lossX, lossY):
    screen.fill((0, 0, 0))
    loss = font.render("YOU LOSE!", True, (255,255,255))
    screen.blit(loss, (lossX, lossY))


def show_continue(contX, contY):
    screen.fill((0, 0, 0))
    cont = font.render("TRY AGAIN?", True, (255,255,255))
    screen.blit(cont, (contX, contY))


# Screen
screen = pygame.display.set_mode((800, 600))

# Background
# background = pygame.image.load('img/background.png')

# Music and Sound
mixer.music.load('sound/background.wav')
mixer.music.play(-1)

collision_sound = mixer.Sound('sound/explosion.wav')
collCount = 1

# Title and Icon
pygame.display.set_caption("Blaster")
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
playerAlive = True


def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))


# Bullet
bulletImg = pygame.image.load('img/bullet.png')
bulletX = 0
bulletY = 0
bulletX_change = 0
bulletY_change = 2
bullet_state = 'ready'


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x, y + 10))


def collision(enemyX, enemyY, bulletX, bulletY):
    dist = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if dist < 27:
        return True
    else:
        return False

# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemyNum = 10
enemyRemain = enemyNum
isAlive = []
tempEnemyImg = []
tempEnemyX = []
tempEnemyY = []
tempEnemyX_Change = []
tempEnemyY_change = []
tempIsAlive = []

for i in range(enemyNum):
    isAlive.append(1)
    enemyImg.append(pygame.image.load('img/alien.png'))
    enemyX.append(100 + i * 55)
    enemyY.append(36)
    enemyX_change.append(0.3)
    enemyY_change.append(60)


def enemy(enemyX, enemyY, i) :
    screen.blit(enemyImg[i], (enemyX, enemyY))


def attack(enemyX, enemyY, playerX, playerY):
    dist = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if dist < 27:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
    # screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.4
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.4
            if event.key == pygame.K_UP:
                playerY_change -= 0.4
            if event.key == pygame.K_DOWN:
                playerY_change += 0.4

            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('sound/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or \
                    event.key == pygame.K_RIGHT:
                playerX_change = 0.0
            if event.key == pygame.K_UP or \
                    event.key == pygame.K_DOWN:
                playerY_change = 0.0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Enemy Movement
    for i in range(enemyNum):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision
        hit = collision(enemyX[i], enemyY[i], bulletX, bulletY)

        if hit:
            collision_sound.play()
            bulletX = playerX
            bulletY = playerY
            bullet_state = 'ready'
            isAlive[i] = 0
            enemyRemain -= 1

        enemy(enemyX[i], enemyY[i], i)

        death = attack(enemyX[i], enemyY[i], playerX, playerY)

        if death:
            playerAlive = False

    # Gameover
    if not playerAlive:
        if collCount == 1:
            collision_sound.play()
            collCount -= 1
        playerX = 900
        playerY = 900

        show_loss(lossTextX, lossTextY)
        pygame.display.update()
        pygame.time.delay(1500)

        inputWait = True
        while inputWait:
            show_continue(contTextX, contTextY)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        break




    # Remove enemies after eliminating them
    enemyNum = enemyRemain

    for i in range(len(isAlive)):
        if isAlive[i] == 1:
            tempEnemyImg.append(enemyImg[i])
            tempEnemyX.append(enemyX[i])
            tempEnemyY.append(enemyY[i])
            tempEnemyX_Change.append(enemyX_change[i])
            tempEnemyY_change.append(enemyY_change[i])
            tempIsAlive.append(isAlive[i])

    enemyImg = tempEnemyImg
    enemyX = tempEnemyX
    enemyY = tempEnemyY
    enemyX_change = tempEnemyX_Change
    enemyY_change = tempEnemyY_change
    isAlive = tempIsAlive

    tempEnemyImg = []
    tempEnemyX = []
    tempEnemyY = []
    tempEnemyX_Change = []
    tempEnemyY_change = []
    tempIsAlive = []

    # Bullet Movement
    if bulletY < 0:
        bulletY = playerY
        bulletX = playerX
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    if enemyRemain == 0:
       show_victory(vicTextX, vicTextY)

    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()


# Attributions
# Game built off of template from FreeCodeCamp:
# Pygame Tutorial for Beginners - Python Game Development Course

# Original Course by buildwithpython on YouTube: "PyGame Tutorial" series

# Icon by Pixel Buddha on flaticon.com
# <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-buddha" title="Pixel Buddha">Pixel Buddha</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# Spaceship by photo3idea_studio on flaticon.com
# <div>Icons made by <a href="https://www.flaticon.com/authors/photo3idea-studio" title="photo3idea_studio">photo3idea_studio</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# Bullet by Smashicons on flaticon.com
# <div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# Alien by Freepik on flaticon.com
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>