#!/usr/bin/python3
import pygame
from math import pi,sin,cos
from time import sleep
from datetime import datetime,date
from my_object import base_object
   
class myBigClock:

    def __init__(self,options):
    
        self.options = options
        
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        
        self.centreX = self.width/2
        self.centreY = self.height/2
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption(self.options['title'])
                                   
        self.bgImg = pygame.image.load(self.options['bgImage'])

        self.done=False
        self.prevSec = 0

        self.hourHand = base_object([
        [-110,-10],
        [-130,0],
        [-110,10],
        [0,5],
        [0,-5] 
        ],
        self.centreX,
        self.centreY,
        self.options['handColour'])
        
        self.minuteHand = base_object([
        [-160,-10],
        [-180,0],
        [-160,10],
        [0,5],
        [0,-5] 
        ],
        self.centreX,
        self.centreY,
        self.options['handColour'])
        
        self.secondHand = base_object([
        [-180,-5],
        [-200,-0],
        [-180,5],
        [0,2],
        [0,-2] 
        ],
        self.centreX,
        self.centreY,
        self.options['handColour'])
        
        self.numeralsFont = pygame.font.SysFont(self.options["font"], 25, True, False)
 
        self.mainLoop()

    def mainLoop(self):
        while not self.done:
            self.getEvents()
            now = datetime.now()
            if( now.second != self.prevSec):
                self.updateClock (now)

    def updateClock (self, now):
        self.clock.tick()   
        self.screen.fill(self.options['background'])
        bg_width, bg_height = self.bgImg.get_size()
        bg_x = (self.width - bg_width) // 2
        bg_y = (self.height - bg_height) // 2
        self.screen.blit(self.bgImg, (bg_x, bg_y))
        
        self.drawDial(60,210,5,self.options['quarterColour']) 
        
        self.drawDial(12,210,8,self.options['hourColour'])
               
        self.drawNumerals(240)
        today = date.today()
        self.drawLabel ((self.centreX,self.centreY-300),self.options["motto"],25)
        self.drawLabel ((self.centreX,self.centreY+300),today.strftime(self.options["dateFormat"]),18)
        now = datetime.now()
        if (now.hour>12):
            self.hourHand.setAngle((now.hour-12) * 30 + (now.minute * 0.5) + (now.second * 0.00833333333) + 90)
        else:
            self.hourHand.setAngle((now.hour * 30) + (now.minute * 0.5) + (now.second * 0.00833333333) + 90)
        self.minuteHand.setAngle((now.minute * 6) + (now.second * 0.1) + 90)
        self.secondHand.setAngle((now.second * 6) + 90)
        
        self.hourHand.rotateNodes()
        self.minuteHand.rotateNodes()
        self.secondHand.rotateNodes()
        
        self.hourHand.drawObject(self.screen)
        self.minuteHand.drawObject(self.screen)
        self.secondHand.drawObject(self.screen)
        
        pygame.draw.circle(self.screen,self.options['hourColour'], (self.centreX,self.centreY), 10)
        pygame.display.flip()
        self.hourHand.angle = self.hourHand.angle + 1
        self.prevSec = now.second       
        
    def drawDial(self,numitems,dialRadius,dotRadius,dotColour,icon= False):    
        cords =[]
        for i in range(0, numitems,1):
            x = self.centreX - dialRadius * cos((i*360/numitems) * pi/180)    
            y = self.centreY - dialRadius * sin((i*360/numitems) * pi/180)
            if (icon==False):
                pygame.draw.circle(self.screen, dotColour, (x,y), dotRadius)
            else:
                icon.setX(x)
                icon.setY(y)
                icon.setAngle(i*360/numitems)
                icon.rotateNodes()
                icon.setColour(dotColour)
                icon.drawObject(self.screen)       
                  
    def drawNumerals(self,dialRadius):
        for i in range(0, 12,1):
            x = (self.centreX-20) - dialRadius * cos(((i-3)*360/12+2700) * pi/180)    
            y = (self.centreY-15) - dialRadius * sin(((i-3)*360/12+2700) * pi/180) 
            text = self.numeralsFont.render(self.options["numerals"][i], True, self.options["labelColour"])
            text = pygame.transform.rotate(text, i*-30)
            self.screen.blit(text, [x, y])
                  
    def drawLabel (self,cords,message,fontsize):
        font = pygame.font.SysFont(self.options["font"], fontsize, True, False)
        text = font.render(message, True, self.options['labelColour'])
        self.screen.blit(text,(cords[0]-text.get_width()/2, cords[1]-text.get_height()/2))   
           
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
 
    def printFonts(self):
        fonts = pygame.font.get_fonts()
        print(len(fonts))
        for f in fonts:
            print(f)
    
if __name__ == "__main__":

    clk =  myBigClock({
    "width":800,
    "height":600,
    "title":"My Big Clock",
    "motto":"TEMPUS FUGIT",
    "dateFormat":"%A | %d-%B-%Y",
    "background":(150,150,150),
    "bgImage":"greek.svg",
    "labelColour":(0,0,0),
    "handColour":(0,0,0),
    "hourColour":(0,0,0),
    "quarterColour":(100,100,100),
    "font":"freeserif",
    'numerals':[
    "XII ",
    " I  ",
    "II ",
    "III",
    "IIII",      
    "  V ",
    " VI ",
    " VII",
    "VIII",
    "  IX",
    "  X ",
    " XI "
    ]
    })
