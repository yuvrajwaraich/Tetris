import pygame
from sys import exit
from tetris import Tetris

pygame.init()

# 15x20 grid, 30x30 pixel boxes
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (0, 191, 255)
DARK_BLUE = (0, 0, 139)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)


def drawBlocks(tBoard):
    for row in range(len(tBoard)):
        for col in range(len(tBoard[0])):
            if tBoard[row][col].getObject() != None:
                if tBoard[row][col].getObject().getColour() == "P":
                    pygame.draw.rect(
                        screen, BLACK, (row*30, col*30, 30, 30), 2)
                    screen.fill(PURPLE, (row*30 + 1, col*30 + 1, 29, 29))
                elif tBoard[row][col].getObject().getColour() == "R":
                    pygame.draw.rect(
                        screen, BLACK, (row*30, col*30, 30, 30), 2)
                    screen.fill(RED, (row*30 + 1, col*30 + 1, 29, 29))
                elif tBoard[row][col].getObject().getColour() == "G":
                    pygame.draw.rect(
                        screen, BLACK, (row*30, col*30, 30, 30), 2)
                    screen.fill(GREEN, (row*30 + 1, col*30 + 1, 29, 29))
                elif tBoard[row][col].getObject().getColour() == "LB":
                    pygame.draw.rect(
                        screen, BLACK, (row*30, col*30, 30, 30), 2)
                    screen.fill(
                        LIGHT_BLUE, (row*30 + 1, col*30 + 1, 29, 29))
                elif tBoard[row][col].getObject().getColour() == "DB":
                    pygame.draw.rect(
                        screen, BLACK, (row*30, col*30, 30, 30), 2)
                    screen.fill(
                        DARK_BLUE, (row*30 + 1, col*30 + 1, 29, 29))
                elif tBoard[row][col].getObject().getColour() == "Y":
                    pygame.draw.rect(
                        screen, BLACK, (row*30, col*30, 30, 30), 2)
                    screen.fill(YELLOW, (row*30 + 1, col*30 + 1, 29, 29))
                elif tBoard[row][col].getObject().getColour() == "O":
                    pygame.draw.rect(
                        screen, BLACK, (row*30, col*30, 30, 30), 2)
                    screen.fill(ORANGE, (row*30 + 1, col*30 + 1, 29, 29))


def main():
    running = True
    objFalling = False
    currTime = pygame.time.get_ticks()
    tetris = Tetris()
    right = False
    left = False
    prevMoveTime = 0
    while running:
        screen.fill(WHITE)
        tBoard = tetris.board
        drawBlocks(tBoard)

        if not objFalling:
            tetris.newObject()
            objFalling = True

        if pygame.time.get_ticks() - currTime >= 500:
            currTime = pygame.time.get_ticks()
            if not tetris.hitBottom():
                tetris.moveObject()
            else:
                tetris.newObject()

        if right and pygame.time.get_ticks() - prevMoveTime >= 75:
            tetris.moveRight()
            prevMoveTime = pygame.time.get_ticks()
        elif left and pygame.time.get_ticks() - prevMoveTime >= 75:
            tetris.moveLeft()
            prevMoveTime = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    right = True
                    prevMoveTime = pygame.time.get_ticks()
                if event.key == pygame.K_LEFT:
                    left = True
                    prevMoveTime = pygame.time.get_ticks()
                if event.key == pygame.K_UP:
                    tetris.rotate()
                if event.key == pygame.K_DOWN:
                    tetris.slamDown()
            if event.type == pygame.KEYUP:
                right = False
                left = False
            
                    
        tetris.checkRowDone()
        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    main()
