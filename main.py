import pygame

# Initialize the pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))

# Background
# background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Blaster")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))


# Enemy
enemyImg = pygame.image.load('alien.png')
enemyX = 370
enemyY = 36
enemyX_change = 0.3
enemyY_change = 25

def enemy(enemyX, enemyY):
    screen.blit(enemyImg, (enemyX,enemyY))

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
                playerX_change -= 0.1
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.1
            if event.key == pygame.K_UP:
                playerY_change -= 0.1
            if event.key == pygame.K_DOWN:
                playerY_change += 0.1
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
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change


    playerY += playerY_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

# Attributions
# Icon by Pixel Buddha on flaticon.com
# <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-buddha" title="Pixel Buddha">Pixel Buddha</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# Spaceship by photo3idea_studio on flaticon.com
# <div>Icons made by <a href="https://www.flaticon.com/authors/photo3idea-studio" title="photo3idea_studio">photo3idea_studio</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# Bullet by Smashicons on flaticon.com
# <div>Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

# Alien by Freepik on flaticon.com
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>