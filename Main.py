from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from DDA import DDA

def init(width,height):
    glClearColor(0.0,0.0,0.0,1.0)
    glColor3f(1.0,1.0,1.0)
    gluOrtho2D(0,width,0,height)

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    DDA((0,0),(640,400))
    DDA((0,400),(640,0))
    

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)

width = 640
height = 400

glutInitWindowSize(width,height)
wind = glutCreateWindow("OpenGL")
init(width,height)
glutDisplayFunc(display)
glutMainLoop()

