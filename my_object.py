from math import pi,sin,cos
import pygame   
class base_object:

    def __init__(self,nodes,x,y,colour):
        self.nodesOrginal = nodes
        self.nodesLen = len(self.nodesOrginal)
        self.nodes=[]
        self.copyNodes() 
        self.setAngle(0)      
        self.setX(x)
        self.setY(y)
        self.setColour(colour)

    def setX(self,x):
        self.x=x
 
    def setY(self,y):
        self.y=y

    def setAngle(self,angle):
        self.angle=angle
        
    def setColour(self,colour):
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
