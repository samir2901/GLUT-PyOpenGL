from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

def init(width,height):
    glLoadIdentity()
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    gluOrtho2D(0,width,0,height)


def drawLine():
    glBegin(GL_LINES)
    glVertex2i(10, 10)
    glVertex2i(200,200)
    glEnd() 


def display():    
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    pivot = (0, 0)
    drawLine()

    glPushMatrix()    
    glRotatef(30,0,0,1)  
    
    drawLine()

    glPopMatrix()
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)

width = 640
height = 480

glutInitWindowSize(width,height)
wind = glutCreateWindow("OpenGL")
init(width,height)
glutDisplayFunc(display)
glutMainLoop()
