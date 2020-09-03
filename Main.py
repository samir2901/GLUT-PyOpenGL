from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from DDA import *
from BresenhamLine import *
from MidPointCircle import *
from RegressionPlot import *
from Dot import *

def init(width,height):
    glClearColor(1.0,1.0,1.0,1.0)
    glColor3f(1.0,1.0,1.0)
    gluOrtho2D(0,width,0,height)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #midPointCircle((100,100),50)
    #midPointCircle((200,200),100)
    #midPointCircle((300,300),150)
    draw()
    #drawDot(100,80)
    #glFlush()




glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)

width = 640
height = 480

glutInitWindowSize(width,height)
wind = glutCreateWindow("OpenGL")
init(width,height)
glutDisplayFunc(display)
glutMainLoop()
