from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from DDA import *
from BresenhamLine import *
from MidPointCircle import *

def init(width,height):
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    gluOrtho2D(0,width,0,height)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    DDA((0,480),(640,0))
    BresenhamLine((0,0),(640,480))
    midPointCircle((320,240),200)
    
    
    

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)

width = 640
height = 480

glutInitWindowSize(width,height)
wind = glutCreateWindow("OpenGL")
init(width,height)
glutDisplayFunc(display)
glutMainLoop()

