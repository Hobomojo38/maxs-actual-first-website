import pygame
import math
import os
pygame.init()

#-------------------------------------------------------------------------------------------------------------------------

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class line: #takes "point" inputs
    def __init__(self, point1, point2, colour = (220, 220, 220)):        
        self.point1 = point1
        self.point2 = point2
        if point1.x == point2.x: #Because fuck vertical lines
            self.isVert = True
            self.m = None
            self.b = 0
        else:        
            m = (point2.y - point1.y)/(point2.x - point1.x)
            self.isVert = False
            self.m = m
            self.b = point1.y - (m*point1.x)
        self.colour = colour

#-------------------------------------------------------------------------------------------------------------------------
def getPOI(wall1, wall2):

    if wall1.isVert == True and wall2.isVert == True: #Both are vertical, so both are parallel
        return None
    elif wall1.isVert == True:
        x = wall1.point1.x
        y = wall2.m * x + wall2.b
    elif wall2.isVert == True:
        x = wall2.point1.x
        y = wall1.m * x + wall1.b
    elif wall1.m == wall2.m: #Both are parallel
        return None
    else:
        m3 = wall1.m - wall2.m
        b3 = wall2.b - wall1.b
        x = b3/m3
        y = wall2.m * x + wall2.b    

    return point(x,y)


def getAndCheckPOI(newPOI, playerWall, wall, thedaPlayerPoint, raycasting = True): #has both the getting and checking function for POI and limits so it can cancel if both lines are vertical
    output = False

    #Test to make sure the POI is infront of the player
    if raycasting == True:
        if distance(newPOI, thedaPlayerPoint) > distance(newPOI, playerPos): return False
    #else:
        #tO.append(str(newPOI.x) + " " + str(newPOI.y))

    #testing for x limits on wall
    if wall.point1.x > wall.point2.x:
        output = True if newPOI.x <= wall.point1.x and newPOI.x >= wall.point2.x else False
        #greater than point2, less than point1
    elif wall.point1.x < wall.point2.x:
        output = True if newPOI.x >= wall.point1.x and newPOI.x <= wall.point2.x else False
        #greater than point1, less than point2
    else:
        output = True if newPOI.x == wall.point1.x else False    

    if output == True:
        #testing for y limits on wall
        if wall.point1.y > wall.point2.y:
            output = True if newPOI.y <= wall.point1.y and newPOI.y >= wall.point2.y else False
            #greater than point2, less than point1
        elif wall.point1.y < wall.point2.y:
            output = True if newPOI.y >= wall.point1.y and newPOI.y <= wall.point2.y else False
            #greater than point1, less than point2
        else:
            output = True if newPOI.y == wall.point1.y else False

    if raycasting == False and output == True:
        #testing for x limits on playerWall
        if playerWall.point1.x > playerWall.point2.x:
            output = True if newPOI.x <= playerWall.point1.x and newPOI.x >= playerWall.point2.x else False
            #greater than point2, less than point1
        elif playerWall.point1.x < playerWall.point2.x:
            output = True if newPOI.x >= playerWall.point1.x and newPOI.x <= playerWall.point2.x else False
            #greater than point1, less than point2
        else:
            output = True if newPOI.x == playerWall.point1.x else False    

        if output == True:
            #testing for y limits on playerWall
            if playerWall.point1.y > playerWall.point2.y:
                output = True if newPOI.y <= playerWall.point1.y and newPOI.y >= playerWall.point2.y else False
                #greater than point2, less than point1
            elif playerWall.point1.y < playerWall.point2.y:
                output = True if newPOI.y >= playerWall.point1.y and newPOI.y <= playerWall.point2.y else False
                #greater than point1, less than point2
            else:
                output = True if newPOI.y == playerWall.point1.y else False


    return output



def distance(testingPoint, orgin):
    a = pow(abs(testingPoint.x - orgin.x), 2)
    b = pow(abs(testingPoint.y - orgin.y), 2)
    d = pow(a + b, 1/2)
    return d

def secondPlayerPoint(theda):
    theda = math.radians(theda)
    x = math.cos(theda) * 0.01
    y = math.sin(theda) * 0.01

    if x == 6.123233995736766e-17: x = 0

    x = x + playerPos.x
    y = y + playerPos.y

    return point(x,y)

def wallsAppend(points, colour, close = False):
    numOfPoints = len(points)

    for i in range(0, numOfPoints - 1):
        walls.append(line(points[i], points[i + 1], colour))

    if close == True:
        walls.append(line(points[numOfPoints - 1], points[0], colour))

def thedaOf(m):
    if m == None: return 90

    theda = math.atan(m)

    return [theda, theda + 180]

def getPerpLine(m, point1 = point(0,0)):
    m = -1 / m if m != None else 0
    b = point1.y - (m * point1.x)

    return line(point1, point(0, b))



#-------------------------------------------------------------------------------------------------------------------------



#Clears the past text on the console


#Sets the size of and activates the display
size = width, height = 840, 500
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('Consolas', 15)

columnWidth = 4 #Can be any number that 840%x == 0
numOfColumns = int(width/columnWidth)
FOV = 120

columnXAdjustment = int(columnWidth/2) if columnWidth%2 == 0 else int((columnWidth/2) + 0.5)
newY = (numOfColumns/2)/ math.tan(math.radians(FOV/2))



#Basic colours for quick access
black = (0,0,0)
white = (220,220,220)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

#position and veiwing-angle of the player
playerPos = point(0,0)
playerTheda = 90 #mesured in degrees

walls = []

#walls.append(line(point(0,-25), point(-25,-25), red)) #Random red wall
wallsAppend([point(30,30), point(0, 30), point(0,60), point(30,60)], black)

walls.append(line(point(-50, -50), point(0, -50), green)) #Big box with alternating-colour walls
walls.append(line(point(-50, -50), point(-50, -100), blue))
walls.append(line(point(0, -100), point(-50, -100), green))
walls.append(line(point(0, -50), point(0, -100), blue))

wallsAppend([point(1,1), point(2,1), point(2,2), point(1,2)], blue, True)

walls.append(line(point(-20,20), point(-100, 100), blue))
walls.append(line(point(10,10), point(20,20), blue))

#-------------------------------------------------------------------------------------------------------------------------

#Game Loop
finished = False
os.system('cls')
while finished == False:
    tO = []    
    
    #Updates display before clearing it black so the previous frames aren't visable
    pygame.display.update()
    screen.fill(black)

    #Draws the sky and the floor, both seperated at the horizLine
    horizLine = height/2
    skyColour = (30,30,30)
    floorColour = (10,10,10)
    pygame.draw.rect(screen, skyColour, pygame.Rect(0, 0, width, int(horizLine)))
    pygame.draw.rect(screen, floorColour, pygame.Rect(0, int(horizLine), width, height))
    
    for column in range(0, numOfColumns + 1)[::-1]:
        newX = (numOfColumns/2) - column #The distance from the central column to the column being cast right now
        #newY = 34.6 #Set to the = (#OfColumns/2)/tan(FOV/2)
        
        angle = math.atan2(newX,newY)
        angle = math.degrees(angle)
        #if column in [0,120]:
            #print(angle)
        angle = playerTheda + angle

        #Gets the equation for the playerLine using the angle the player is facing
        thedaPlayerPoint = secondPlayerPoint(angle)
        playerLine = line(playerPos, thedaPlayerPoint)

        #Checks the playerLine with every wall and find the closest one
        closestDist = 1000
        for wall in walls:
            POI = getPOI(playerLine, wall)
            if POI != None:
                if getAndCheckPOI(POI, playerLine, wall, thedaPlayerPoint) == True:
                    d = distance(POI, playerPos)
                    if d < closestDist:
                        closestDist = d
                        closestWall = wall

        #If there is a closest wall, render it
        if closestDist != 1000:
            #Turns to raw distance into a distance parallel to the central line
            angle = math.radians(playerTheda - angle)
            lineLength = closestDist * math.cos(angle)
            
            #Turns the distance into a length of pixels on the screen using a 1/x function
            lineLength = height / lineLength

            x = (column * columnWidth) - columnXAdjustment #The "x" coord of where to draw the new column
            topPoint = point(x, (height/2 - lineLength/2))
            bottomPoint = point(x, (height/2 + lineLength/2))
            pygame.draw.line(screen, closestWall.colour, (int(topPoint.x), int(topPoint.y)), (int(bottomPoint.x), int(bottomPoint.y)), columnWidth)
            

    #Handles any key inputs during run-time
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]: #Escape key/Quit
        finished = True

    if keys[pygame.K_RIGHT]: #Turn left/right
        playerTheda -= 1
    if keys[pygame.K_LEFT]:
        playerTheda += 1
    radPlayerTheda = math.radians(playerTheda)


    newPlayerPos = point(playerPos.x, playerPos.y)

    if keys[pygame.K_w]: #Lateral movement/strafing
        newPlayerPos.y += math.sin(radPlayerTheda) * 0.1
        newPlayerPos.x += math.cos(radPlayerTheda) * 0.1
    if keys[pygame.K_s]:
        newPlayerPos.y -= math.sin(radPlayerTheda) * 0.1
        newPlayerPos.x -= math.cos(radPlayerTheda) * 0.1
    if keys[pygame.K_a]:
        newPlayerPos.y += math.cos(radPlayerTheda) * 0.1
        newPlayerPos.x -= math.sin(radPlayerTheda) * 0.1
    if keys[pygame.K_d]:
        newPlayerPos.y -= math.cos(radPlayerTheda) * 0.1
        newPlayerPos.x += math.sin(radPlayerTheda) * 0.1

    #run checks for no valid POI's ----------------
    thedaPlayerPoint = secondPlayerPoint(playerTheda)


    newPlayerLine = line(playerPos, newPlayerPos)


    """passed = False
    while not passed:
        passed = True

        newPLayerLine = line(playerPos, newPlayerPos)
        for wall in walls:
            POI = getPOI(wall, newPlayerLine)
            check = getAndCheckPOI(POI, newPlayerLine, wall, thedaPlayerPoint, False) if POI != None else False
            if check == True:
                passed = False
                perpLine = getPerpLine(wall.m, POI)
                pointThedas = thedaOf(perpLine.m)
                newPoint1 = point(POI.x + math.cos(pointThedas[0]) * 0.1, POI.y + math.sin(pointThedas[0] * 0.1))
                newPoint2 = point(POI.x + math.cos(pointThedas[1]) * 0.1, POI.y + math.sin(pointThedas[1] * 0.1))

                if distance(newPoint1, playerPos) < distance(newPoint2, playerPos): #Point1 is closer to player
                    newPlayerPos = newPoint1
                else:
                    newPlayerPos = newPoint2"""
                    


    """passed = False
    while passed == False:
        passed = True
        newPlayerLine = line(playerPos, newPlayerPos) #Testing the x movement
        for wall in walls:
            check = []
            POI = getPOI(newPlayerLine, wall)
            POI1 = getPOI(wall, line(playerPos, point(playerPos.x, newPlayerPos.y)))
            POI2 = getPOI(wall, line(playerPos, point(newPlayerPos.x, playerPos.y)))
            check.append(getAndCheckPOI(POI, newPlayerLine, wall, thedaPlayerPoint, False) if POI != None else False)
            check.append(getAndCheckPOI(POI1, newPlayerLine, wall, thedaPlayerPoint, False) if POI1 != None else False)
            check.append(getAndCheckPOI(POI2, newPlayerLine, wall, thedaPlayerPoint, False) if POI2 != None else False)
            if check[0] == True:                
                if POI1 == None: avgPOI = POI2
                elif POI2 == None: avgPOI = POI1
                else: avgPOI = point((POI1.x + POI2.x) / 2, (POI1.y + POI2.y) / 2)
                tO.append("X + Y test is true")
                print("General POI test triggered")

                if avgPOI.x > playerPos.x:
                    #POI.x - (math.sin(math.radians(thedaOf(wall.m))) * 0.011)
                    newPlayerPos.x = POI.x - 0.01
                elif avgPOI.x < playerPos.x:
                    newPlayerPos.x = POI.x + 0.01
 
                if avgPOI.y > playerPos.y:
                    newPlayerPos.y = POI.y - 0.01
                elif avgPOI.y < playerPos.y:
                    newPlayerPos.y = POI.y + 0.01
                #break
            elif True in [check[1], check[2]]:

                if check[1] == True:
                    print("X-coord POI test triggered")
                    if POI1 == None: avgPOI = POI2
                    elif POI2 == None: avgPOI = POI1
                    else: avgPOI = point((POI1.x + POI2.x) / 2, (POI1.y + POI2.y) / 2)
                    tO.append("X + Y test is true")
                    #print(playerPos.y, avgPOI.y)

                    if avgPOI.x > playerPos.x:
                        #POI.x - (math.sin(math.radians(thedaOf(wall.m))) * 0.011)
                        newPlayerPos.x = POI2.x - 0.01
                    elif avgPOI.x < playerPos.x:
                        newPlayerPos.x = POI2.x + 0.01

                if check[2] == True:
                    print("Y-coord POI test triggered")
                    if POI1 == None: avgPOI = POI2
                    elif POI2 == None: avgPOI = POI1
                    else: avgPOI = point((POI1.x + POI2.x) / 2, (POI1.y + POI2.y) / 2)

                    if avgPOI.y > playerPos.y:
                        newPlayerPos.y = POI1.y - 0.01
                    elif avgPOI.y < playerPos.y:
                        newPlayerPos.y = POI1.y + 0.01"""

    
    playerPos = point(newPlayerPos.x, newPlayerPos.y)

    #Turn this on to only run one frame of the game
    #finished = True

    tO.append("x = " + str(playerPos.x))
    tO.append("y = " + str(playerPos.y))
    tO.append("playerTheda = " + str(playerTheda))

    for i in range(len(tO)):        
        text = font.render(str(tO[i]), False, white)
        screen.blit(text, (0, i*15))

    #necessity to run because... ???
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #If the game is told to exit, it will
            finished = True
            exit() #closes the console window

    
#print(math.cos(math.pi/2))




#wall1 = line(point(3,7), point(-5,-9))


#-------------------------------------------------------------------------------------------------------------------------



    