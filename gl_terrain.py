import sys
from math import pi, tan
from OpenGL.GL import *
from OpenGL.GLUT import *
from noise import RandomNoise

noise = RandomNoise(32, 32, 255, 0)
noise.randomize()
p = 3
lines_grid = noise.smoothNoise2d(smoothing_passes=p)

ROT_SPEED = 1.0
X = 0.0
Y = 0.0
Z = 0.0
rotX = 0.0
rotY = 0.0
rotZ = 0.0

def Draw():
    global lines_grid

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glRotatef(rotX, 1.0, 0.0, 0.0)
    glRotatef(rotY, 0.0, 1.0, 0.0)
    glRotatef(rotZ, 0.0, 0.0, 1.0)
    glTranslatef(X, Y, Z)
    #---
    mod = 6
    z = -1.0
    for lines in lines_grid:
        glBegin(GL_LINE_STRIP)
        x = 0.0
        z += 1.0
        for y in lines:
            y *= mod
            glVertex3f(x, y, z)
            x += 1.0
        glEnd()
    #---
    glutSwapBuffers()

def Key(k, x, y):
    global X, Y, Z

    if k == b'w':
        Z += ROT_SPEED
    elif k == b's':
        Z -= ROT_SPEED
    elif k == b'a':
        X += ROT_SPEED
    elif k == b'd':
        X -= ROT_SPEED
    elif k == b'q':
        Y += ROT_SPEED
    elif k == b'e':
        Y -= ROT_SPEED
    else:
        return
    glutPostRedisplay()

def KeyUp(k, x, y):
    global X, Y, Z

    if k == b'w':
        Z = 0
    elif k == b's':
        Z = 0 
    elif k == b'a':
        X = 0
    elif k == b'd':
        X = 0
    elif k == b'q':
        Y = 0
    elif k == b'e':
        Y = 0
    else:
        return
    glutPostRedisplay()

def Special(k, x, y):
    global rotX, rotY, rotZ

    if k == GLUT_KEY_UP:
        rotX += ROT_SPEED
    elif k == GLUT_KEY_DOWN:
        rotX -= ROT_SPEED
    elif k == GLUT_KEY_LEFT:
        rotY += ROT_SPEED
    elif k == GLUT_KEY_RIGHT:
        rotY -= ROT_SPEED
    else:
        return
    glutPostRedisplay()

def SpecialUp(k, x, y):
    global rotX, rotY, rotZ

    if k == GLUT_KEY_UP:
        rotX = 0
    elif k == GLUT_KEY_DOWN:
        rotX = 0
    elif k == GLUT_KEY_LEFT:
        rotY = 0
    elif k == GLUT_KEY_RIGHT:
        rotY = 0
    else:
        return
    glutPostRedisplay()
        

def glPerspective(fovY, aspect, zNear, zFar):
    fH = tan(fovY/360*pi) * zNear
    fW = fH * aspect
    glFrustum(-fW, fW, -fH, fH, zNear, zFar)

def Reshape(width, height):
    h = float(height) / float(width);
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glPerspective(45.0, h, 5.0, 60.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.0, -6.0, -45.0)

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glPerspective(45.0, float(Width)/float(Height), 0.1, 50.0)
    glTranslatef(0.0, -6.0, -45.0)
    glRotatef(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_MODELVIEW)


def InitGLUT(Width, Height, WindowName):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(Width, Height)
    glutCreateWindow(WindowName)
    glutDisplayFunc(Draw)
    glutIdleFunc(Draw)
    glutReshapeFunc(Reshape)
    glutKeyboardFunc(Key)
    glutKeyboardUpFunc(KeyUp)
    glutSpecialFunc(Special)
    glutSpecialUpFunc(SpecialUp)


def main():
    InitGLUT(1200, 1024, 'TEST')
    InitGL(1200, 1024)

    if "-info" in sys.argv:
        print("GL_RENDERER   = ", glGetString(GL_RENDERER))
        print("GL_VERSION    = ", glGetString(GL_VERSION))
        print("GL_VENDOR     = ", glGetString(GL_VENDOR))

    glutMainLoop()

if __name__ == "__main__":
    main()
