from OpenGL.GL import *

def drawDot(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()