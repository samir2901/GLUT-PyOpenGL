from OpenGL.GL import *

def drawDot(x, y):
    glPointSize(1.5)
    glBegin(GL_POINTS)    
    glVertex2i(x, y)
    glEnd()