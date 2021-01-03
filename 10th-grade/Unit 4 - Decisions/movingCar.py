
# Kesar Sampat 
#
# Original car shapes code from Joey Woodrow
# HCP
#Assignment - Unit 4 extension of Vehicles on the move
#purpose - moves vehicles along a road- demonstrates animation and mouse collision detection

import pygame, sys

#initialize game engine
pygame.init()

# open and set a window size 
w = 640
h = 480
surface = pygame.display.set_mode((w,h))

#set title bar 
pygame.display.set_caption("Rolling on the Highway!")

#colors here
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 175, 0)
BLUE = (0, 0, 255)
LTGREEN = (67, 189, 56)
CYAN = (89, 212, 234)
YELLOW = (255, 255, 0)
GREY = (40,40,40)
RED = (255,0,0)
DKGREEN = (0, 70, 0)

clock = pygame.time.Clock()
clock.tick(40)



##################   FUNCTIONS   ####################################



def drawRoad():
    pygame.draw.rect(surface, BLACK, (0, h/3, w, h/3),0)
    x=0
    while(x<w):
        pygame.draw.line(surface,YELLOW,(x,h/3+h/6),( x+40, h/3+h/6),5)
        x+=50

def drawCar(x,y,scale,color):
    carh = h/6*scale
    carw = 2*carh
    #draw rectangle body
    pygame.draw.rect(surface, color, (x, y+carh/3, carw, carh/3), 0)
    #draw wheels
    pygame.draw.ellipse(surface,GREY, (x+carw/6, y+5*carh/9, carw/6, carw/6), 0)
    pygame.draw.ellipse(surface,GREY, (x+4*carw/6, y+5*carh/9, carw/6, carw/6), 0)
    #drawtoppartthing
    pointlist = ((x+carw/3,y),(x+2*carw/3, y),(x+5*carw/6, y+carh/3),(x+carw/6,y+carh/3))
    pygame.draw.polygon(surface, color, pointlist, round(carh//11))
    pygame.draw.line(surface, color, [x+carw/2,y], [x+carw/2,y+carh/3], round(carh//11))
    #taillight
    pygame.draw.rect(surface, RED, (x, y+carh*4/10, carw/20,carw/12),0)
    #headlight
    pygame.draw.rect(surface, YELLOW, (x+carw*11/12, y+carh*2/5, carw/12,carw/12),0)
    
def drawTruck(x,y,scale,color):
    th = h/5*scale
    tw = 2*th
    #drawrectangle body
    pygame.draw.rect(surface, color,(x, y, 7*tw/8, 3*th/4),0)
    pygame.draw.rect(surface, color,(x+7*tw/8, y+th/4, tw/8, th/2),0)
    #drawwheels
    pygame.draw.ellipse(surface, GREY, (x+tw/8, y+11*th/16, th/3,th/3),0)
    pygame.draw.ellipse(surface, GREY, (x+3*tw/4, y+11*th/16, th/3,th/3),0)
    #drawwindows
    pygame.draw.rect(surface, BLACK, (x+3*tw/4, y+th/4, tw/8,th/4),0)
    pointLiist = [(x+3*tw/4,y+th/4),(x+3*tw/4,y+th*97/200),(x+5*tw/8,y+th*97/200)]
    pygame.draw.polygon(surface,BLACK, pointLiist, 0)
    #pygame.draw.line(surface,BLACK, [x+3*tw/4,y+th/2],[x+7*tw/8,y+th/2])
    pygame.draw.line(surface, color, [x+3*tw/4,y+th/4],[x+3*tw/4, y+th/2],1)
    #drawimageontruck
    pygame.draw.rect(surface, GREY, (x, y, tw/2,th/2),0)
    pygame.draw.rect(surface, color, (x, y, tw/2,th/2),round(tw/th))
    pygame.draw.rect(surface, color, (x+tw/16,y+3*th/16, 5*tw/16, th/6),0)
    pointliist=[(x+3*tw/8,y+th/8),(x+3*tw/8,y+3*th/8),(x+15*tw/32,y+th/4)]
    pygame.draw.polygon(surface,color, pointliist, 0)
    
def drawBus(x,y,scale, color):
    bh=h/5*scale
    bw=3*bh
    #body
    pygame.draw.rect(surface, color, (x,y,bw,4*bh/5),0)
                     
    #windows
    pygame.draw.rect(surface, BLACK, (x+bw/15, y+bh/5, bw/15,bw/15),0)
    pygame.draw.rect(surface, BLACK, (x+3*bw/15, y+bh/5, bw/15,bw/15),0)
    pygame.draw.rect(surface, BLACK, (x+5*bw/15, y+bh/5, bw/15,bw/15),0)
    pygame.draw.rect(surface, BLACK, (x+7*bw/15, y+bh/5, bw/15,bw/15),0)
    pygame.draw.rect(surface, BLACK, (x+9*bw/15, y+bh/5, bw/15,bw/15),0)
    pygame.draw.rect(surface, BLACK, (x+11*bw/15, y+bh/5, bw/15,bw/15),0)
    #door
    pygame.draw.rect(surface, GREY,(x+13*bw/15, y+bh/5, bw/15,bw*6/33),0)
    #frontwindow
    pygame.draw.rect(surface, BLACK, (x+14.5*bw/15, y+bh/5, bw/30, bw*2/15),0)
    #wheels
    pygame.draw.ellipse(surface, GREY, (x+bw/5, y+bh*2/3,bw/10,bw/10),0)
    pygame.draw.ellipse(surface, GREY, (x+bw*11/15, y+bh*2/3, bw/10, bw/10),0)
    
def showMessage(words, size, x, y, color, bg=None):
    font = pygame.font.SysFont("Calibri", 25, True, False,)
    text = font.render(words, True, color, bg)
    textBounds = text.get_rect()
    textBounds.center=(x,y)
    return text, textBounds

def drawScene(busX,truckX,carX, btnMessage, mouseOverStatus):
    drawRoad()
    drawCar(carX,9*h/16, .65, BLUE)
    drawTruck(truckX,6*h/16, .55, LTGREEN)
    drawBus(busX,5/14*h,.6,YELLOW)
    
    #create button with correct colors based on the button message and mouseOver Status
    if mouseOverStatus == True:
        if btnMessage ==" STOP ":
            buttonText, buttonBounds = showMessage(btnMessage, 24, w/2, h/4, WHITE, RED)
        else:
            buttonText, buttonBounds = showMessage(btnMessage, 24, w/2, h/4, WHITE, DKGREEN)
            
    else: #mouse is not over the button
        if btnMessage ==" STOP ":
            buttonText, buttonBounds = showMessage(btnMessage, 24, w/2, h/4, RED, WHITE)  
        else:
            buttonText, buttonBounds = showMessage(btnMessage, 24, w/2, h/4, DKGREEN, WHITE)        
            
    surface.blit(buttonText, buttonBounds)
            
            
            
   
    
def moveVehicles(c, t, b):
    c+= 8
    b+= 5
    t+= 3

    
    #check for moving off screen
    if c>w:
        c=-25
    if t>w:
        t=-25
    if b>w:
        b=-25
    
                   
        
    return c, t, b
    
def toggleMessage(buttonMessage):
    if buttonMessage == " STOP ":
        return "  GO  "
    else:
        return " STOP "
        



   
    
#-------------------MAIN PROGRAM loop 

def main():
    
    #initialize car x-values
    carX= w*3/5
    truckX=3*w/4
    busX=3/10*w    
    
    #need bounds for button click collision detection 
    buttonText,buttonBounds = showMessage(" STOP" , 24, w/2, h/4, RED, WHITE)
    
    btnMessage = " STOP "
    mouseOver = False #assume mouse not over button, then check it 

    
    while(True):
        for event in pygame.event.get():
            if (event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)):
                pygame.quit()
                sys.exit()
                
            mouseOver = False #assume mouse not over button, then check it 
            
                
            if buttonBounds.collidepoint(pygame.mouse.get_pos()):
                mouseOver = True
                if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                    btnMessage = toggleMessage(btnMessage) #change text on the button
                    
            
        if btnMessage == " STOP ":
            carX, truckX, busX = moveVehicles(carX, truckX, busX)
            
            
        
              

                
        #drawing code here
            
       
        surface.fill(GREEN)
        drawScene(busX,truckX,carX, btnMessage, mouseOver)
        
        
        pygame.display.update()
                            
      
        
        
main()