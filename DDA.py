from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def DDA(start,end):
    x, y = start[0], start[1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    steps = max(dx,dy)
    xinc = dx/steps
    yinc = dy/steps
    glBegin(GL_POINTS)
    glVertex2d(round(x),round(y))
    for i in range(steps):
        x += xinc
        y += yinc
        glVertex2d(round(x),round(y))
    glEnd()
    glFlush()
