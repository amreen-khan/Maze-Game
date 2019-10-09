#By Amreen Khan

from pygame import * 
import pygame 

init() # initializing pygame
SIZE = 800, 600 # setting screen size
screen = display.set_mode(SIZE) 
BLACK = (0, 0, 0) # setting RGB for colors 
WHITE = (255,255,255)
GRAY = (128,128,128)
BLACK = (0, 0, 0) 
RED = (255, 0, 0)
BLUE = (102,178,255)
GREEN = (102,255,178)


running = True # variable that controls the main loop



click = 0 
count = 0


fontHello = font.SysFont("Times New Roman", 30)   # Initialize a font
bg = image.load("blue.jpg")                # Load image from file
key = image.load("key.png")
virus = image.load("virus.png")
youwin = image.load("youwinn.png")
youlost = image.load("youlost.png")
instructions = image.load("instructions.png")
music = mixer.Sound("music.wav")
music.play()


def drawScene(screen, x,y, click, count, gameStarted, levelData,currentLevel):
    screen.fill((255,255,255))
    
    circuit = Rect (0,0,bg.get_width(), bg.get_height())
    screen.blit(bg, circuit) #displaying the background
    
    if gameStarted:  
        
        draw.rect(screen, WHITE, (x,y, playerWidth, playerHeight)) #the moving square is being drawn
        screen.blit(virus,mousePos)#the picture of the virus will be displayed on top of the moving square
   
    else:
        draw.rect(screen, BLUE, (x,y, 50,50)) #drawing the rectangle that will be scrolled over at the beginning in order to strat the game
    
    for rect in levelData:
        draw.rect(screen, RED, rect) #drawing the walls
        
    if currentLevel == 1:
        screen.blit(key,(750,275,50,50)) #displaying the key on the second level
    display.flip()

def playGame(screen, x, y, levelData, levelColor,currentLevel):
    isAlive = 1
    
    for rect in levelData:
        if Rect(x,y, playerWidth, playerHeight).colliderect(rect): #if the players rectangle collides with the wall rectangle we are checking, the user is no longer alive
            isAlive = 0
            
        if currentLevel == 1:
            keyRect = Rect(700,275,50,50) #if the mouse comes in contact with the key the game is over and you have won
            if Rect(x,y, playerWidth, playerHeight).colliderect(keyRect):
                isAlive = 2
    
    return isAlive


FONT = font.SysFont("Times New Roman",35) # setting font and font size
FONT2 = font.SysFont("Impact",100) # setting font and font size

text3 = FONT2.render("Security Breach", 1, (RED)) #setting this outside def statement so it can be used later on
 
def menu(screen): #setting up the initial screen
   
    circuit = Rect (0,0,800,600)
    screen.blit(bg, circuit)
    
    draw.rect(screen, WHITE,(250, 125, 330, 100)) # drawing the "Start Mission" box with the words inside it
    text = FONT.render("Start Mission" , 1, (BLACK))	
    screen.blit(text, Rect(335,160,400,150))
    
    draw.rect(screen, WHITE,(250, 275, 330, 100)) # drawing the "Instructions" box with the words inside it       
    text1 = FONT.render("Instructions" , 1, (BLACK))	
    screen.blit(text1, Rect(335,310,400,100))
    
    draw.rect(screen, WHITE,(250, 425, 330, 100))        
    text2 = FONT.render("Exit Game" , 1, (BLACK)) # drawing the "Exit Game" box with the words inside it
    screen.blit(text2, Rect(355,460,400,100))
    
    draw.rect(screen, BLACK,(125, 15, 560, 90))
    screen.blit(text3, Rect(135,20,400,100)) #displaying the name of the game on top of the page within a black box
    display.flip()


def instruction(screen): #setting up the instruction screen
    
    screen.blit(instructions, Rect(0,0,800,600))
    display.flip()
    

page = 0


running = True
myClock = time.Clock()
gameStarted = False
isAlive = True

x,y = 0, 275 #setting the beginning x and y positions to 0,275
playerWidth, playerHeight = 30,30 #dimensions of the cursor are being set

levels = [
    [Rect(0, 0, 20, 250), Rect(0, 350, 20, 250), Rect(780, 0, 20, 250), Rect(780, 350, 20, 250), Rect(20, 0, 760, 20), Rect(20, 580, 760, 20), Rect(110, 60, 20, 480), Rect(190, 20, 20,265) , Rect(190, 335, 20,580), Rect(270,60,20,520), Rect(350,20,20,510), Rect(430,20,20,150), Rect(430,210,20,400), Rect(510,440,20,200), Rect(510,20,20,380), Rect(590, 20, 20,265), Rect(590, 335, 20,580),Rect(670, 60, 20, 480)],
    
    [Rect(0, 0, 20, 250), Rect(0, 350, 20, 250), Rect(780, 0, 20, 250), Rect(780, 350, 20, 250), Rect(20, 0, 760, 20), Rect(20, 580, 760, 20), Rect(110,20,20,510), Rect(190,60,20,520), Rect(270,20,20,510), Rect(350,60,20,520), Rect(430,20,20,510), Rect(510,60,20,520), Rect(590,20,20,510),Rect(670,60,20,520)]
]#all walls are being displayed within its level in this list

levelColors = [RED]

currentLevel = 0

# Main Loop
while running:
    button = 0
    

    for evnt in event.get():             # checks all events that happen

        if evnt.type == QUIT:
            running = False
       
        elif evnt.type == MOUSEBUTTONDOWN: # when the button is clicked the following coul happen
            mx, my = evnt.pos          
            button = evnt.button
            if page == 0:
                if mx > 250 and mx < 580 and my > 125 and my < 225:
                    page = 1 # if you click within the "Start Program" box you will go to the start program page
                elif mx > 250 and mx < 580 and my > 275 and my < 375:
                    page = 2 # if you click within the "Instructions" box you will go to the instructions page       
                elif mx > 250 and mx < 580 and my > 425 and my < 525:
                    page = 3 # if you click within the "Exit Game" box you will exit the program
                else:
                    page = 0 # if anyhwere else is clicked nothing will happen and you will stay on the same page
            
            elif page == 2:
                if button == 3: #if you right click on the instructions page you will return to the main menu page
                    page = 0         
   
    if page == 1: # if you are on the start program page and you left click it will return you to the initial page
        mousePos = mouse.get_pos()
        
        if mousePos[0] >= 780: #you will pass into the next level when you go through the opening on the first level, the mouse position will be returned to 0,275
            x = 0
            currentLevel = 1
            mouse.set_pos(x, y)
      
        drawScene(screen, x, y, click, count, gameStarted,levels[currentLevel],currentLevel)    
        
        if gameStarted:
            mouse.set_visible(False) #hides the mouse 
            if x >=800:
                x = 0  
            
           
            isAlive = playGame(screen, x,y, levels[currentLevel], levelColors[0], currentLevel) #stores the returned value
            x, y = mousePos[0], mousePos[1]
            display.flip()
          

        
        elif not gameStarted and (mousePos[0] > x and mousePos[0] < x+50 and mousePos[1] > y and mousePos[1] < y+50): #when you scroll over the blue box the game will begin
            gameStarted = True
            
          
            
        if isAlive == 0: #when the user hits a wall and dies they will be returned to the main menu screen
            screen.blit(youlost, Rect(0,0,800,600))
            display.flip()           
            
            page = 0
            gameStarted = False
            isAlive = 1
            
            x,y = 0, 275
            playerWidth, playerHeight = 30,30
            currentLevel = 0
            mouse.set_visible(True)
             
            display.flip()
            time.wait(4000)
    
            x,y = 0, 275
            playerWidth, playerHeight = 30,30
            currentLevel = 0
            mouse.set_visible(True)
            
        elif isAlive == 2: #when a user collects the key and wins they will be returned to the main menu screen
            screen.blit(youwin, Rect(0,0,800,600))
            display.flip()
           
            page = 0
            gameStarted = False
            isAlive = 1
            
            x,y = 0, 275
            playerWidth, playerHeight = 30,30 #makes sure the mouse is still visible after the game ends
            currentLevel = 0
            mouse.set_visible(True)
             
            display.flip()
            time.wait(4000)

   
    elif page == 0: # when page is equal to 0 you will be on the initial screen
        menu(screen)
    
    elif page == 2: # when page is equal to 2 you will be on the change level screen
        instruction(screen)
        
    elif page == 3: # when page is equal to 3 you will exit the program
        running == False
        quit()


quit() 