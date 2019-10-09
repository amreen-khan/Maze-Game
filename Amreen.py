from pygame import * #importing pygame
import random 
init() 
size = w, h = 800, 600 #screen size is being set
screen = display.set_mode(size)


mx, my = mouse.get_pos()
click = 0 
count = 0



GRAY = (128,128,128)
BLACK = (0, 0, 0) #RGB is being set for the colors
RED = (255, 0, 0)
BLUE = (102,178,255)
GREEN = (102,255,178)

fontHello = font.SysFont("Times New Roman", 30)   # Initialize a font
bg = image.load("blue.jpg")                # Load image from file
              # Load shooting sound

def drawScene(screen, x,y, click, count, gameStarted):
    screen.fill((255,255,255))
    

    
    # Draw image from file (to have a transparent background, you need to create
    # the image as such using Photoshop or something other than MS Paint
    # (save as .png or .gif)
    circuit = Rect (0,0,bg.get_width(), bg.get_height())
    screen.blit(bg, circuit)
    
    if gameStarted:  
        if x >=800:
            x = 0        
        draw.rect(screen, BLACK, (x,y, playerWidth, playerHeight)) #the moving square is being drawn
    else:
        draw.rect(screen, BLUE, (x,y, 50,50))
    
def playGame(screen, x, y, levelData, levelColor):
    isAlive = True
    
    for rect in levelData:
        draw.rect(screen, levelColor, rect)
        if x >= 800:
            x = 0        
        if Rect(x,y, playerWidth, playerHeight).colliderect(rect): #if the players rectangle collides with the wall rectangle we are checking, the user is not longer alive
            isAlive = False
    
    return isAlive



running = True
yClock = time.Clock()
gameStarted = False
isAlive = True

x,y = 0, 275
playerWidth, playerHeight = 30,30

levels = [
    [Rect(0, 0, 20, 250), Rect(0, 350, 20, 250), Rect(780, 0, 20, 250), Rect(780, 350, 20, 250), Rect(20, 0, 760, 20), Rect(20, 580, 760, 20),Rect(110, 60, 20, 480), Rect(190, 20, 20,265) , Rect(190, 335, 20,580), Rect(270,60,20,520), Rect(350,20,20,510), Rect(430,20,20,150), Rect(430,210,20,400), Rect(510,440,20,200), Rect(510,20,20,380), Rect(590, 20, 20,265), Rect(590, 335, 20,580),Rect(670, 60, 20, 480)],
    [Rect(0, 0, 20, 250), Rect(0, 350, 20, 250), Rect(780, 0, 20, 250), Rect(780, 350, 20, 250), Rect(20, 0, 760, 20), Rect(20, 580, 760, 20),]
]

levelColors = [GRAY]

currentLevel = 0


    
while running:
    for evnt in event.get(): #check all the events that are happening
        
        if evnt.type == QUIT:
            running = False      
        if evnt.type == MOUSEBUTTONDOWN: #variable is set for pressing the mousebutton as click
            click = evnt.button
                                                                    
    mousePos = mouse.get_pos()
    if mousePos[0] >= 780:
        x = 0
        currentLevel = 1
        mouse.set_pos(x, y)
  
    drawScene(screen, x, y, click, count, gameStarted)    
    
    if gameStarted:
        mouse.set_visible(False) #hides the mouse 
        if x >=800:
            x = 0        
        isAlive = playGame(screen, x,y, levels[currentLevel], levelColors[0]) #stores the returned value
        x, y = mousePos[0], mousePos[1]
        
    
    elif not gameStarted and (mousePos[0] > x and mousePos[0] < x+50 and mousePos[1] > y and mousePos[1] < y+50):
        gameStarted = True
      
        
    if not isAlive: #do stuff here when the user hits a wall / dies
        gameStarted = False
        isAlive = True

        x,y = 0, 275
        playerWidth, playerHeight = 30,30
        currentLevel = 0
        mouse.set_visible(True)
    
        
    display.flip()
    yClock.tick(60) #waits long enough to have 60fps                    
    
quit()