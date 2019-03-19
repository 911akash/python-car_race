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


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    #game_loop()


def crash():
    message_display('You Crashed')



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    crashed = False
    score = 0


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
        for block in blocks:
            if block.thing_starty == 595:
                blocks.remove(block)
                block.thing_starty = 0
                block.thing_startx = random.randrange(0, display_width - block.thing_width)
                newblock = Block()
                blocks.append(newblock)
                score += 1

            block.things(block.thing_startx, block.thing_starty)
            block.thing_starty += block.thing_speed

        car(x, y)

        x += x_change

        if x > (display_width - car_width) or x < 0:
            crash()
        else:
            car(x, y)

        scoreText = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = text_objects("SCORE:" + str(score), scoreText)
        gameDisplay.blit(TextSurf, (0, 0))

        pygame.display.update()
        clock.tick(120)

game_loop()
pygame.quit()
quit()