import pygame
from pygame.constants import K_x
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK=(90,90,90)
WHITE=(240,240,240)
BLUE = (90,90,255)

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball1 = Ball(WHITE, 10, 10)
ball1.rect.x = 45
ball1.rect.y = 195

ball2 = Ball(BLUE, 10, 10)
ball2.rect.x = 145
ball2.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball1)
all_sprites_list.add(ball2)

carryOn = True
clock = pygame.time.Clock()

scoreA = 0
scoreB = 0

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('./sounds/bass.wav')
pygame.mixer.music.play(-1)

bounce_sound = pygame.mixer.Sound('./sounds/bounce.wav')
bounce_wall = pygame.mixer.Sound('./sounds/bounce_wall.wav')
cheering = pygame.mixer.Sound('./sounds/cheering.wav')

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False
            elif event.key == pygame.K_SPACE:
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        break

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_p]:
        paddleB.moveUp(5)
    if keys[pygame.K_l]:
        paddleB.moveDown(5)
        
    all_sprites_list.update()
    for ball in [ball1, ball2]:
        if ball.rect.x>=690:
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 660
            if ball==ball1:
                scoreA+=1
                cheering.play()
        if ball.rect.x<=0:
            ball.velocity[0] = -ball.velocity[0]
            ball.rect.x = 40
            if ball==ball1:
                scoreB+=1
                cheering.play()
        if ball.rect.y>490:
            ball.velocity[1] = -ball.velocity[1]
            bounce_wall.play()
        if ball.rect.y<55:
            ball.velocity[1] = -ball.velocity[1]
            bounce_wall.play()
        
        if pygame.sprite.collide_mask(ball, paddleA):
                ball.bounce() 
                bounce_sound.play()
                if ball==ball2:
                    scoreA+=1
        if pygame.sprite.collide_mask(ball, paddleB):
                ball.bounce() 
                bounce_sound.play()
                if ball==ball2:
                    scoreB+=1
                
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349,0], [349,500], 5)
    pygame.draw.line(screen, WHITE, [0,50], [700,50], 5)
    
    all_sprites_list.draw(screen)
    
    font = pygame.font.Font(None,50)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()