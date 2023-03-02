#!/usr/bin/python3
import pygame
from math import pi,sin,cos
from time import sleep
from datetime import datetime

class base_object:

    def __init__(self,nodes,x,y,colour):
        self.nodesOrginal = nodes
        self.nodesLen = len(self.nodesOrginal)
        self.nodes=[]
        self.copyNodes()
        self.heading = 0
        self.angle = 0      
        self.x = x
        self.y = y
        self.colour = colour
 
    # this is quite probably bad python but it prevents weirdness, I'm not sure I like python
    def copyNodes(self):
        for i in range(0, self.nodesLen,1):
            self.nodes.append([self.nodesOrginal[i][0],self.nodesOrginal[i][1]])
 
    def rotateNodes(self):
        radians =  (pi/180) * self.angle    
        sinTheta = sin(radians)
        cosTheta = cos(radians)
        for i in range(0, self.nodesLen,1):
            x = self.nodesOrginal[i][0]
            y = self.nodesOrginal[i][1]
            self.nodes[i][0] = x * cosTheta - y * sinTheta
            self.nodes[i][1] = y * cosTheta + x * sinTheta

    def drawObject(self,surface):
        cords = []
        for i in range(0,self.nodesLen,1):
            x=self.x+self.nodes[i][0]
            y=self.y+self.nodes[i][1]
            cords.append((x,y))
        pygame.draw.polygon(
        surface, 
        self.colour, 
        cords
        )
   
class myBigClock:

    def __init__(self):
        self.printFonts()
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
        self.background=(0,0,0)
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
        (255,255,255))
        
        self.minuteHand = base_object([
        [-200,-10],
        [-220,0],
        [-200,10],
        [0,5],
        [0,-5] 
        ],
        self.centreX,
        self.centreY,
        (255,255,255))
        
        self.secondHand = base_object([
        [-200,-10],
        [-250,-0],
        [-200,10],
        [0,5],
        [0,-5] 
        ],
        self.centreX,
        self.centreY,
        (255,255,255))
        self.font = pygame.font.SysFont('dejavuserif', 30, True, False)
        self.numerals=[
        "XII ",
        " I  ",
        " II ",
        " III",
        "IIII",      
        "  V ",
        " VI ",
        "VII ",
        "VIII",
        "  IX",
        "  X ",
        "  XI"
        ]

        
        self.mainLoop()

    def mainLoop(self):
        while not self.done:
            self.getEvents()
            
            now = datetime.now()
            if( now.second != self.prevSec):
                self.clock.tick()            
                self.screen.fill(self.background)
           
                self.drawDial(12,280,10)
                self.drawDial(60,280,5)
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
                #pygame.draw.circle(self.screen, (255,255,255), (self.centreX,self.centreY), 20)
                pygame.display.flip()
                self.hourHand.angle = self.hourHand.angle + 1
                self.prevSec =now.second
        
      def drawNumerals(self,dialRadius):
        for i in range(0, 12,1):
            x = (self.centreX-25) - dialRadius * cos(((i-3)*360/12+2700) * pi/180)    
            y = (self.centreY-25) - dialRadius * sin(((i-3)*360/12+2700) * pi/180) 
            text = self.font.render(self.numerals[i], True, (255,255,255))
            text = pygame.transform.rotate(text, i*-30)
            self.screen.blit(text, [x, y])  
                     
    def drawNumerals(self,dialRadius):
        for i in range(0, 12,1):
            x = self.centreX - dialRadius * cos(((i-3)*360/12+2700) * pi/180)    
            y = self.centreY - dialRadius * sin(((i-3)*360/12+2700) * pi/180) 
            text = self.font.render(self.numerals[i], True, (255,255,255))
            text = pygame.transform.rotate(text, i*-30)
            self.screen.blit(text, [x-25, y-20])      
          
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
