from random import sample
from OpenGL.GL import *
from DDA import *
from Dot import *
from sklearn.linear_model import LinearRegression
import numpy as np


def plotRegressionLine(x,y,lineColor=(1,0,0),pointColor=(0,0,1),axesColor=(0,1,0)):
    
    #draw x-axis and y-axis
    glColor3f(*axesColor)
    DDA((0,0),(0,500))
    DDA((0,0),(500,0))
 
    lr = LinearRegression().fit(x.reshape(-1,1),y)

    glColor3f(*pointColor)    
    for point in zip(x,y):
        #print(point)
        drawDot(*point)

    slope = lr.coef_[0]
    intercept = lr.intercept_

    initY = int(intercept)
    finalY = int(slope * x[len(x)-1] + intercept)
    glColor3f(*lineColor)
    DDA((0,initY),(x[len(x)-1],finalY))   

def draw():
    x = np.array(sample(range(100,400),10))
    y = np.array(sample(range(50,400),10))
    plotRegressionLine(x,y)
    glFlush()


