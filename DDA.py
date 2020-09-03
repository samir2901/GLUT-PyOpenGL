from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from Dot import *

def DDA(start,end):
    x, y = start[0], start[1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    steps = max(dx,dy)
    xinc = dx/steps
    yinc = dy/steps    
    drawDot(int(x+0.5),int(y+0.5))   
    for i in range(steps):
        x += xinc
        y += yinc
        drawDot(int(x+0.5),int(y+0.5))   
