#!/usr/bin/python3
import pygame
from math import pi,sin,cos
from time import sleep
from datetime import datetime
from my_object import base_object
   
class myBigClock:

    def __init__(self):
        #self.printFonts()
        pygame.init()
        self.width=800
        self.height=600
        size = [self.width, self.height]
        self.screen = pygame.display.set_mode(size)
        self.centreX = self.width/2
        self.centreY = self.height/2
        self.clock = pygame.time.Clock()
        self.done=False
        pygame.display.set_caption("My Big Clock")
        self.background=(255,255,255)
        self.labelColour=(255,255,255)

        self.prevSec = 0
        self.hourHand = base_object([
        [-140,-10],
        [-150,0],
        [-140,10],
        [0,5],
        [0,-5] 
        ],
        self.centreX,
        self.centreY,
        (0,0,0))
        
        self.minuteHand = base_object([
        [-200,-10],
        [-220,0],
        [-200,10],
        [0,5],
        [0,-5] 
        ],
        self.centreX,
        self.centreY,
        (0,0,0))
        
        self.secondHand = base_object([
        [-200,-5],
        [-240,-0],
        [-200,5],
        [0,2],
        [0,-2] 
        ],
        self.centreX,
        self.centreY,
        (0,0,0))
        self.font = pygame.font.SysFont('dejavuserif', 30, True, False)
        self.numerals=[
        "XII ",
        " I  ",
        " II ",
        " III",
        "IIII",      
        "  V ",
        "  VI",
        " VII",
        "VIII",
        "  IX",
        "  X ",
        " XI "
        ]
        
        self.bgImg = pygame.image.load('greek.svg')
        self.mainLoop()

    def mainLoop(self):
        while not self.done:
            self.getEvents()
            
            now = datetime.now()
            if( now.second != self.prevSec):
                self.updateClock (now)

    def updateClock (self, now):
        self.clock.tick()
                    
        self.screen.fill(self.background)
        self.screen.blit(self.bgImg, (0,0))
        self.drawDial(60,280,5,(100,100,100))
        self.drawDial(12,280,10,(0,0,0))
        
        self.drawNumerals(240)
        now = datetime.now()
        if (now.hour>12):
            self.hourHand.angle = (now.hour-12) * 30 + (now.minute * 0.5) + (now.second * 0.00833333333) + 90
        else:
            self.hourHand.angle =(now.hour * 30) + (now.minute * 0.5) + (now.second * 0.00833333333) + 90
        
        self.minuteHand.angle = (now.minute * 6) + (now.second * 0.1) + 90
        self.secondHand.angle = (now.second * 6) + 90
        self.hourHand.rotateNodes()
        self.minuteHand.rotateNodes()
        self.secondHand.rotateNodes()

        self.hourHand.drawObject(self.screen)
        self.minuteHand.drawObject(self.screen)
        self.secondHand.drawObject(self.screen)
        pygame.draw.circle(self.screen, (0,0,0), (self.centreX,self.centreY), 10)
        pygame.display.flip()
        self.hourHand.angle = self.hourHand.angle + 1
        self.prevSec = now.second       

    def drawDial(self,numitems,dialRadius,dotRadius,dotColour):
    
        cords =[]

        for i in range(0, numitems,1):
            x = self.centreX - dialRadius * cos((i*360/numitems) * pi/180)    
            y = self.centreY - dialRadius * sin((i*360/numitems) * pi/180)
            pygame.draw.circle(self.screen, dotColour, (x,y), dotRadius)
                     
    def drawNumerals(self,dialRadius):
        for i in range(0, 12,1):
            x = (self.centreX-20) - dialRadius * cos(((i-3)*360/12+2700) * pi/180)    
            y = (self.centreY-25) - dialRadius * sin(((i-3)*360/12+2700) * pi/180) 
            text = self.font.render(self.numerals[i], True, (0,0,0))
            text = pygame.transform.rotate(text, i*-30)
            self.screen.blit(text, [x, y])      
          
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                self.done=True 
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_q):
                    self.done=True
                elif (event.key == pygame.K_UP):
                    self.K_UP=True
                elif (event.key == pygame.K_DOWN):
                    self.K_DOWN=True
                elif (event.key == pygame.K_LEFT):
                    self.K_LEFT=True
                elif (event.key == pygame.K_RIGHT):
                    self.K_RIGHT=True
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_UP):
                    self.K_UP=True
                elif (event.key == pygame.K_DOWN):
                    self.K_DOWN=True
                elif (event.key == pygame.K_LEFT):
                    self.K_LEFT=True
                elif (event.key == pygame.K_RIGHT):
                    self.K_RIGHT=True
                    
    def sinwv(self,t,frequency,offset,amp):
        return sin(frequency*t+offset)*(amp-1)+amp;                
 
    def printFonts(self):
        fonts = pygame.font.get_fonts()
        print(len(fonts))
        for f in fonts:
            print(f)
    
if __name__ == "__main__":
    tmp =  myBigClock()
