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

    global x
    global y
    
    plotRegressionLine(x,y)
    
    glFlush()
    

def mouseClicked(button, button_state, cursor_x, cursor_y):
    global x
    global y
    if(button == GLUT_LEFT_BUTTON and button_state == GLUT_DOWN):
        global clicked
        if not clicked:
            glColor3f(0,0,1)   
            glPointSize(1.5)
            glBegin(GL_POINTS)                         
            for point in zip(x,y):
                print(clicked)                
                #print(point)
                glVertex2i(*point)
                #drawDot(*point)
            glEnd()
            glFlush()           


clicked = False
x = np.array(sample(range(100,400),10))
y = np.array(sample(range(50,400),10))

glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA)

width = 640
height = 480

glutInitWindowSize(width,height)
wind = glutCreateWindow("OpenGL")
init(width,height)
glutMouseFunc(mouseClicked)
glutDisplayFunc(display)
glutMainLoop()
