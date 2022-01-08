import pygame 
from field import Field

pygame.init()

DARKBLUE=(36,90,190)
WHITE=(255,255,255)
ORANGE=(255,120,0)
RED=(255,0,0)

size = (1000,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Maze")
field = Field(1000,800)
field.add_monsters(35)

score = 0
x_pos = 50
y_pos = 50

size_x = 100
size_y = 80
dx = size[0]/size_x
dy = size[1]/size_y
wbrick = 0.9*dx
hbrick = 0.9*dy
    
carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
            or event.type == pygame.KEYDOWN and event.key == pygame.K_x:
                carryOn = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not field.brick_at(x_pos-1, y_pos):
        x_pos-=1
    if keys[pygame.K_RIGHT] and not field.brick_at(x_pos+1, y_pos):
        x_pos +=1
    if keys[pygame.K_UP] and not field.brick_at(x_pos, y_pos-1):
        y_pos-=1
    if keys[pygame.K_DOWN] and not field.brick_at(x_pos, y_pos+1):
        y_pos +=1
    
    screen.fill(DARKBLUE)
    
    subfield = field.window(x_pos, y_pos, size_x, size_y)
    for idx, vector in enumerate(subfield):
        for idy, val in enumerate(vector):
            if val>0:
                x=idx*dx
                y=idy*dy
                if val<99:
                    color = (250-val*20,200-val*10,val*30)
                else:
                    color = RED
                pygame.draw.rect(screen, color, [x, y, wbrick, hbrick])

    pygame.draw.rect(screen, ORANGE, [size_x/2*dx,size_y/2*dy , hbrick, wbrick])

    field.update_monsters(x_pos, y_pos)
    
    font = pygame.font.Font(None, 50)
    text = font.render(f"{score}",1, WHITE)
    screen.blit(text, (20,30))
    score+=1

    if field.monster_at(x_pos, y_pos):
        font = pygame.font.Font(None, 74)
        text = font.render("GAME OVER",1, RED)
        screen.blit(text, (250,300))
        pygame.display.flip()
        pygame.time.wait(3000)
        carryOn = False

    
    pygame.display.flip()
    
    clock.tick(80)
    
pygame.quit()            