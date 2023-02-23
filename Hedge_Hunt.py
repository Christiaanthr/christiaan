#Snake Game
import pygame
from pygame.locals import *
import random 
import time

pygame.init()




font = pygame.font.SysFont(None, 30)
fnt = pygame.font.SysFont( 'Times New Roman', 60)

SCREEN_WIDTH = 800
SCREEN_HIGHT = 800

SPEED = 5
SPACE_SIZE = 50.0

SNAKE_COLOR = "#cd853f"
FOOD_COLOR ="#fa8072"
BACKGROUND_COLOR = "#ffdab9"

green = SNAKE_COLOR  #(0,180,0)
red = FOOD_COLOR
white = '#f4a460'

SCREEN_WIDTH = (round(700/SPACE_SIZE)*SPACE_SIZE)
SCREEN_HIGHT = (round(700/SPACE_SIZE)*SPACE_SIZE)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HIGHT+100))
pygame.display.set_caption('Hedge Hunt')


food_size = (SPACE_SIZE,SPACE_SIZE)
snake_img =pygame.image.load('E:/vsCode/snake_plant.png')
snake_img = pygame.transform.scale( snake_img,food_size)
snake_head = pygame.image.load('E:/vsCode/snake_head.png')
snake_head = pygame.transform.scale( snake_head,food_size)
food_img = snake_img

screen.fill(FOOD_COLOR ,rect=[200,200,SPACE_SIZE,SPACE_SIZE])

clock = pygame.time.Clock()

def snake(SPACE_SIZE, snake_list, snsize):
    turn = 0
    for xny in snake_list:
        turn += 1
        if turn == snsize:
            snake_pos = (xny[0],xny[1],SPACE_SIZE,SPACE_SIZE)
            screen.blit(snake_head,snake_pos)
        else:
            snake_pos = (xny[0],xny[1],SPACE_SIZE,SPACE_SIZE)
            screen.blit(snake_img,snake_pos)                

def message_screen(msg,color):
    screen_text = font.render(msg,True, color)
    screen.blit(screen_text, [0 ,  SCREEN_HIGHT/2])

def line_draw(score):
    pygame.draw.rect(screen,white,[0,SCREEN_HIGHT,SCREEN_WIDTH,100])
    text = fnt.render('Score: ' + str(score),True, (0,0,0))
    screen.blit(text, [260, SCREEN_HIGHT+15])    

def gameloop():
    run = True
    game_over = False 

    lead_x = SPACE_SIZE
    lead_y = SPACE_SIZE

    lead_x_change = 0
    lead_y_change = 0
    score = 0

    randApplex = round(random.randint(0,SCREEN_WIDTH-SPACE_SIZE)/SPACE_SIZE)*SPACE_SIZE
    randAppley = round(random.randint(0,SCREEN_HIGHT-SPACE_SIZE)/SPACE_SIZE)*SPACE_SIZE 

    snakelength = 1
    snakelist = []

    game_speed = SPEED

    while run:
        while game_over == True:
            
            screen.fill(BACKGROUND_COLOR)
            message_screen('      Game over press SPACE to play again and esc to exit. SCORE:  ' + str(score),red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        game_over = False                                                
                    if event.key == pygame.K_SPACE:
                        gameloop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not lead_x_change == SPACE_SIZE:
                    lead_x_change = -SPACE_SIZE
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT and not lead_x_change == -SPACE_SIZE:
                    lead_x_change = SPACE_SIZE 
                    lead_y_change = 0    
                elif event.key == pygame.K_UP and not lead_y_change == SPACE_SIZE:
                    lead_y_change = -SPACE_SIZE 
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN and not lead_y_change == -SPACE_SIZE:
                    lead_y_change = SPACE_SIZE
                    lead_x_change = 0

        lead_x += lead_x_change
        lead_y += lead_y_change
        if lead_x > SCREEN_WIDTH-SPACE_SIZE or lead_x < 0 or lead_y < 0 or lead_y > SCREEN_HIGHT-SPACE_SIZE:
            game_over = True

        screen.fill(BACKGROUND_COLOR)    
        
        img_pos =(randApplex,randAppley)
        screen.blit(food_img,img_pos)
        #pygame.draw.rect(screen, red,[randApplex,randAppley,SPACE_SIZE,SPACE_SIZE])  

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)

        if len(snakelist) > snakelength:
            del snakelist[0]

        for eachSeg in snakelist[:-1]:
            if eachSeg == snakehead:
                game_over = True

        snake(SPACE_SIZE, snakelist,snakelength) 
        line_draw(score)
        pygame.display.update()
        
        clock.tick(game_speed)
        
        if lead_x == randApplex and lead_y == randAppley:

            randApplex = round(random.randint(0,SCREEN_WIDTH-SPACE_SIZE)/SPACE_SIZE)*SPACE_SIZE
            randAppley = round(random.randint(0,SCREEN_HIGHT-SPACE_SIZE)/SPACE_SIZE)*SPACE_SIZE
            snakelength += 1 
            score += 1
            game_speed += 0.1
            line_draw(score)
            pygame.display.update()            
                  
gameloop()
pygame.quit()            
quit()    