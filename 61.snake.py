import pygame, sys, time, random
from pygame.locals import*

pygame.init()
dis_width=600
dis_height=400
DISPLAYSURF=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake Game')

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)

clock=pygame.time.Clock()
snake_block=10
snake_speed=15

lose_style=pygame.font.SysFont("couriernew",17)
def loseMessage(msg):
    message=lose_style.render(msg,True,black)
    DISPLAYSURF.blit(message,[dis_width/6,dis_height/3])

score_style=pygame.font.SysFont("robotobold",23)
def show_score(score):
    value=score_style.render("Score: "+str(score),True,black)
    DISPLAYSURF.blit(value,[0,0])

def draw_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(DISPLAYSURF, green, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0
    
    snake_list=[]
    snake_length=1

    foodx=round(random.randrange(0,dis_width-snake_block)/10)*10
    foody=round(random.randrange(0,dis_height-snake_block)/10)*10

    game_over=False
    while True:
        while game_over==True:
            loseMessage("You Lose!\nQ - Quit     Space - Play Again")
            show_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.type()==pygame.K_q():
                        pygame.quit()
                        sys.exit()
                    if event.type()==pygame.K_SPACE():
                        gameLoop()

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x1_change=-snake_block
                    y1_change=0
                if event.key==pygame.K_RIGHT:
                    x1_change=snake_block
                    y1_change=0
                if event.key==pygame.K_UP:
                    x1_change=0
                    y1_change=-snake_block
                if event.key==pygame.K_DOWN:
                    x1_change=0
                    y1_change=snake_block

        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_over=True
        x1+=x1_change
        y1+=y1_change

        DISPLAYSURF.fill(white)
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if(len(snake_list)>snake_length):
            del snake_list[0]

        for x in snake_list[:-1]:
            if x==snake_Head:
                game_over=True
        
        pygame.draw.rect(DISPLAYSURF,red,[foodx,foody,snake_block,snake_block])
        
        draw_snake(snake_block,snake_list)
        show_score(snake_length-1)
        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,dis_width-snake_block)/10)*10
            foody=round(random.randrange(0,dis_height-snake_block)/10)*10
            snake_length+=1

        pygame.display.update()    
        clock.tick(snake_speed)

gameLoop()