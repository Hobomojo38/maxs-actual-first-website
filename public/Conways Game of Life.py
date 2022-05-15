import pygame
from pygame import *
import time, sys
import random

pygame.init()

x, y, xBorder, yBorder, pixelMult = 0, 0, 0, 0, 0
chaos = True
lenGrid = 0

class Timer:
    def __init__(self) -> None:
        self.startTime = 0
        pass

    def start(self):
        """Starts/Resets the timer"""
        self.startTime = time.time()

    def currentTime(self):
        """Gives the time, in seconds, since the timer started."""
        return time.time() - self.startTime


def Create_Grid(xLimit, yLimit):
    """(int, int) -> list[][]"""

    grid = []

    for i in range(xLimit):
        grid.append([])
        for j in range(yLimit):
            grid[i].append(False)

    return grid

def Randomize_Grid(grid, chance):

    newGrid = Create_Grid(x, y)

    for X in range(x):
        for Y in range(y):
            num = random.random()
            # print(num <= chance/100)
            newGrid[X][Y] = True if num <= chance/100 else False

    return newGrid

def Print_Grid(grid):
    """(list[][]) -> None
    Prints the inputed grid on the console, with (0,0) being top left"""

    for i in range(x):
        out = ""
        for j in range(y):
            out += "1" if grid[i][j] == True else "0"
        print(out)

def Get_Neighbors(grid, X, Y):
    count = 0

    # dx = -1
    # while dx < 2:
    #     dy = -1
    #     while dy < 2:
    #         count += grid[(x + dx + X)%x][(y + dy + Y)%y]
    #         dy += 1
    #     dx += 1
    
    # return count - grid[X][Y]

    xUp = X + 1 if X!= x - 1 else 0
    xDown = X - 1 if X != 0 else x - 1
    yUp = Y + 1 if Y != y - 1 else 0
    yDown = Y - 1 if Y != 0 else y - 1
    

    count += grid[X][yUp] # Up
    count += grid[X][yDown]# Down
    count += grid[xUp][Y] # Right
    count += grid[xDown][Y] # Left
    count += grid[xUp][yUp] # Upper-Right
    count += grid[xDown][yUp] # Upper-Left
    count += grid[xUp][yDown] # Down-Right
    count += grid[xDown][yDown] # Down-Left

    return count

def Calc_Next_Gen(grid):
    """(List, int, int) -> List
    Gives the next generation of the provided grid"""

    newGrid = Create_Grid(x, y)

    for X in range(x):
        for Y in range(y):
            count = Get_Neighbors(grid, X, Y)

            if count == 2: newGrid[X][Y] = grid[X][Y]
            elif count == 3: newGrid[X][Y] = True
            else: newGrid[X][Y] = False
            # if grid[X][Y] == True and (count == 2 or count == 3): newGrid[X][Y] = True
            # elif grid[X][Y] == False and count == 3: newGrid[X][Y] = True
            # else: newGrid[X][Y] = False

    return newGrid

def Draw_Board(grid, oldGrid = Create_Grid(x,y)):
    for X in range(x):
            for Y in range(y):
                if grid[X][Y] != oldGrid[X][Y]:
                    colour = ((random.randint(0,255), random.randint(0,255), random.randint(0,255)) if chaos else white) if grid[X][Y] else black
                    pygame.draw.rect(screen, colour, pygame.Rect(xBorder+X*pixelMult, yBorder+Y*pixelMult, pixelMult, pixelMult))

def Draw_Blank_Board(grid, oldGrid = Create_Grid(x,y)):
    for X in range(x):
            for Y in range(y):
                    pygame.draw.rect(screen, black, pygame.Rect(xBorder+X*pixelMult, yBorder+Y*pixelMult, pixelMult, pixelMult))

def Draw_Text(text, x, y, border = False, borderColour = (255,255,255)):
    Rend = font.render(text, True, black)
    if border == True: pygame.draw.rect(screen, borderColour, pygame.Rect(x, y, font.size(text)[0], font.size(text)[1]))
    
    
    screen.blit(Rend, (x,y))
    pass

def Get_Mouse_Pos():
    return pygame.mouse.get_pos()

def Test_Pos_Grid():
    """Returns the grid square the pos is over, or (-1,-1) if it does not."""
    xLimit, yLimit = x*pixelMult , y*pixelMult

    pos = Get_Mouse_Pos()

    xPos = pos[0] - xBorder
    yPos = pos[1] - yBorder

    if xPos < 0 or yPos < 0: return (-1,-1)

    return (xPos//pixelMult, yPos//pixelMult) if xPos < xLimit and yPos < yLimit else (-1,-1)
    

# Main ---------------------------------------------------------------------------------------------



x,y = 300, 180
pixelMult = 4
xBorder, yBorder = 20, 40



# Imagine a "Do not press" button on top of this... 
chaos = False





genCount = 0
xLength, yLength = x*pixelMult+xBorder*2, y*pixelMult+yBorder*2
mouseDown = False
waitTimeBetweenGens = 0

displaySize = xLength, yLength 
black = 0,0,0
white = 255,255,255
grey = 100,100,100


screen = pygame.display.set_mode(displaySize)
pygame.display.set_caption("Conway\'s Game of Life")
font = pygame.font.SysFont('Consolas', 15)

screen.fill(grey)
grid = Create_Grid(x,y)
Draw_Blank_Board(grid)

grid = Randomize_Grid(grid, 30)


# grid[10][10] = True
# grid[11][10] = True
# grid[12][10] = True
# grid[12][11] = True
# grid[11][12] = True

timer = Timer()
timer2 = Timer()
timer.start()





while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False

    if mouseDown and Test_Pos_Grid() != (-1,-1):
        index = Test_Pos_Grid()

        grid[index[0]][index[1]] = True
        #Draw_Board(grid)
        
    pygame.display.update()
    # print(timer.currentTime())

    if timer.currentTime() >= waitTimeBetweenGens: #Update board
        timer.start()

        timer2.start()
        grid2 = Calc_Next_Gen(grid)
        calcTime = timer2.currentTime()

        genCount += 1
        # screen.fill((150,150,150))

        Draw_Text("Generation: " + str(genCount), 2, 2, True, grey)
        
        
        timer2.start()
        Draw_Board(grid2, grid)
        drawTime = timer2.currentTime()

        Draw_Text("Total time (ms): " + str((drawTime + calcTime) * 1000), 2, 18, True, grey)
        Draw_Text("Time to render (ms): " + str(drawTime*1000), 2, yBorder + y*pixelMult + 2 , True, grey)
        Draw_Text("Time to calc next gen (ms): " + str(calcTime*1000), 2, yBorder + y*pixelMult + 18, True, grey)

        grid = grid2
        

    
# Enable this code and disable the above main to print the grid to console. For debugging

# genCount = 40

# print("\nGen 1\n")
# Print_Grid(grid)

# for i in range(genCount):
#     print("\nGen {}\n".format(i + 2))
#     grid = Calc_Next_Gen(grid)
#     Print_Grid(grid)
