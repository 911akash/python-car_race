import pygame
import time
import random

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Formula 1')

black = (0, 0, 0)
white = (255, 255, 255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')
car_width = 73

thing_starty = 0


class Block:
    def __init__(self):
        self.thing_starty = 0
        self.color = black
        self.thing_speed = 7
        self.thing_width = 300
        self.thing_height = 100
        self.thing_startx = random.randrange(0, display_width - self.thing_width)

    def progress(self):
        pass

    def things(self, x, y):
        pygame.draw.rect(gameDisplay, self.color, [x, y, self.thing_width, self.thing_height])



def car(x,y):
    gameDisplay.blit(carImg, (x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def quitgame():
    pygame.quit()
    quit()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    #time.sleep(2)
    #game_loop()


def start_page():
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))

    gameDisplay.blit(TextSurf, TextRect)
    button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)
    button("Quit", 550, 450, 100, 50, red, bright_red, quitgame)
    pygame.display.update()
    clock.tick(20)
    #time.sleep(2)


def showScore(score):
    scoreText = pygame.font.Font('freesansbold.ttf', 25)
    TextSurf, TextRect = text_objects("SCORE:" + str(score), scoreText)
    gameDisplay.blit(TextSurf, (0, 0))


def crash():
    #message_display('You Crashed')
    start_page()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    crashed = False
    score = 0
    is_crash = False

    blocks = []
    numberofBlocks = 1
    for num in range(numberofBlocks):
        block = Block()
        blocks.append(block)
        num += 1

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        if not is_crash:
            for block in blocks:
                if block.thing_starty >= display_height:
                    blocks.remove(block)
                    block.thing_starty = 0
                    block.thing_startx = random.randrange(0, display_width - block.thing_width)
                    newblock = Block()
                    blocks.append(newblock)
                    score += 1
                if block.thing_starty + block.thing_height >=y:
                    #print('y crossover')
                    if (block.thing_startx + block.thing_width >= x) and (block.thing_startx <= x + car_width):
                        is_crash = True
                        crash()
                        #crashed = True
                        #continue

            block.things(block.thing_startx, block.thing_starty)
            block.thing_starty += block.thing_speed

        car(x, y)

        if not is_crash:
            x += x_change

            if x > (display_width - car_width) or x < 0:
                crash()
            else:
                car(x, y)

        showScore(score)

        pygame.display.update()
        clock.tick(120)

        if is_crash:
            crash()
            showScore(score)
            pygame.display.update()
            clock.tick(120)
            #time.sleep(5)


game_loop()
pygame.quit()
quit()