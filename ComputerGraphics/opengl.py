"""

_|          _|  _|      _|  _|      _|  @Time : 2020.12.22 0:10
_|          _|    _|  _|      _|  _|    @Auth : Wang Xiangyu
_|    _|    _|      _|          _|      @File : opengl
  _|  _|  _|      _|  _|        _|      @IDE : PyCharm
    _|  _|      _|      _|      _|      @CODING : utf-8

"""
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

IS_PERSPECTIVE = True  # 透视投影
globalx, globaly = 320, 240
WIN_W, WIN_H = 640, 480


def draw():
    global globalx, globaly
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor4f(1.0, 0.0, 0.0, 1.0)  # 设置当前颜色为红色不透明
    glVertex2f((globalx - 320) / 320, (240 - globaly) / 240)
    glEnd()

    glFlush()
    # glutSwapBuffers()


def mouseclick(button, state, x, y):
    global globalx, globaly
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print(x, y)
        globalx, globaly = x, y
        ################################
        # 标记重新绘制
        glutPostRedisplay()
        ################################


if __name__ == "__main__":
    glutInit()

    glutInitWindowSize(WIN_W, WIN_H)
    glutCreateWindow('OpenGL')

    glutDisplayFunc(draw)
    glutMouseFunc(mouseclick)

    glutMainLoop()
