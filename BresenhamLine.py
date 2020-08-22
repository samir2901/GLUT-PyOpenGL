from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def drawLineLow(start,dest):
    x, y=start[0], start[1]
    dx = dest[0] - start[0]
    dy = dest[1] - start[1]
    p = 2 * dy - dx
    glBegin(GL_POINTS)
    while x<=dest[0]:
        glVertex2i(x,y)
        x += 1
        if p < 0:
            p += 2 * dy
        else:
            p += 2*(dy - dx)
            y += 1
    glEnd()
    glFlush()

def drawLineEqual(start, dest):
    x, y=start[0], start[1]    
    glBegin(GL_POINTS)
    while x<=dest[0]:
        glVertex2i(x,y)
        x += 1        
        y += 1
    glEnd()
    glFlush()

def drawLineHigh(start,dest):
    x, y=start[0], start[1]
    dx = dest[0] - start[0]
    dy = dest[1] - start[1]
    if dx < 0:
        x = -1
        dx = -dx
    p = 2 * dx - dy
    glBegin(GL_POINTS)
    while y<=dest[1]:
        glVertex2i(x,y)
        y += 1
        if p < 0:
            p += 2*dx
        else:
            p -= 2*dy
            x += 1
    glEnd()
    glFlush()

def BresenhamLine(start, dest):
    if(abs(dest[1]-start[1]) < abs(dest[0]-start[0])):
        drawLineLow(start,dest)
    elif(abs(dest[1]-start[1]) == abs(dest[0]-start[0])): 
        drawLineEqual(start,dest)
    else:
        drawLineHigh(start,dest)

