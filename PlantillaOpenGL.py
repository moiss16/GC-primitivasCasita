from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *


def dibujarSol():
    glColor3f(0.9,0.9,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.2 - 0.9 ,sin (angulo) * 0.2 + .9 ,0.0)
    glEnd()



def dibujarCesped():
    glColor3f(0,0.6,0)
    glBegin(GL_QUADS)
    glVertex3f(-1,-0.7,0)
    glVertex3f(1,-0.7,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glEnd()

#------------------------------------------------------------------------casa----------------------------------------------------#
def dibujarCasita():
    glColor3f(1,0.9,0.9)
    glBegin(GL_QUADS)
    glVertex3f(-0.1,-0.1,0)
    glVertex3f(0.6,-0.1,0)
    glVertex3f(0.6,-0.8,0)
    glVertex3f(-0.1,-0.8,0)
    glEnd()

def dibujarTriangulito():
    glColor3f(.7,.7,.7)
    glBegin(GL_TRIANGLES)
    glVertex3f(.25,.3,0)
    glVertex3f(-.2,-.1,0)
    glVertex3f(0.7,-0.1,0)
    glEnd()

def dibujarVentana():
    glColor3f(0,0.8,0.9)
    glBegin(GL_QUADS)
    glVertex3f(-.05,-0.3,0)
    glVertex3f(0.15,-.3,0)
    glVertex3f(0.15,-0.5,0)
    glVertex3f(-.05,-.5,0)
    glEnd()

def dibujarPuerta():
    glColor3f(0.4,0.2,0)
    glBegin(GL_QUADS)
    glVertex3f(.3,-0.4,0)
    glVertex3f(0.5,-.4,0)
    glVertex3f(0.5,-0.8,0)
    glVertex3f(.3,-.8,0)
    glEnd()

def dibujarPerilla():
    glColor3f(.6,.6,.6)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.02 + 0.45 ,sin (angulo) * 0.02 - .6 , 0.0)
    glEnd()

#-------------------------------------------------------------arbol---------------------------------------------------------#
def dibujarTronco():
    glColor3f(0.6,0.4,0.2)
    glBegin(GL_QUADS)
    glVertex3f(-.8,-0.3,0)
    glVertex3f(-0.5,-.3,0)
    glVertex3f(-0.5,-0.85,0)
    glVertex3f(-.8,-.85,0)
    glEnd()

def dibujarhojas1():
    glColor3f(0.3,0.6,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.15 - 0.45 ,sin (angulo) * 0.15 - .2 , 0.0)
    glEnd()
def dibujarhojas2():
    glColor3f(0.3,0.6,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.25 - 0.75 ,sin (angulo) * 0.25 - .2 , 0.0)
    glEnd()
def dibujarhojas3():
    glColor3f(0.3,0.6,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.2 - 0.55 ,sin (angulo) * 0.2 - .1 , 0.0)
    glEnd()
def dibujarhojas4():
    glColor3f(0.3,0.6,0.1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.17 - 0.75 ,sin (angulo) * 0.17 - .05 , 0.0)
    glEnd()

    #----------------------------------------------------------Nubes------------------------------------------------------------#
def dibujarNubes11():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 - 0.15 ,sin (angulo) * 0.1 + .85 , 0.0)
    glEnd()
def dibujarNubes12():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 - 0.27 ,sin (angulo) * 0.1 + .85 , 0.0)
    glEnd()
def dibujarNubes13():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 - 0.38 ,sin (angulo) * 0.1 + .85 , 0.0)
    glEnd()
def dibujarNubes21():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 + 0.12 ,sin (angulo) * 0.1 + .65 , 0.0)
    glEnd()
def dibujarNubes22():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 + 0.23 ,sin (angulo) * 0.1 + .65 , 0.0)
    glEnd()
def dibujarNubes23():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 + 0.34 ,sin (angulo) * 0.1 + .65 , 0.0)
    glEnd()
def dibujarNubes31():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 + 0.62 ,sin (angulo) * 0.1 + .8 , 0.0)
    glEnd()
def dibujarNubes32():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 + 0.73 ,sin (angulo) * 0.1 + .8 , 0.0)
    glEnd()
def dibujarNubes33():
    glColor3f(0.7,0.9,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.1 + 0.84 ,sin (angulo) * 0.1 + .8 , 0.0)
    glEnd()

def lineasSol1():
    glColor3f(0.9,0.9,0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(-.9,.8)
    glVertex2f(-.85,.6)
    glEnd()

def lineasSol2():
    glColor3f(0.9,0.9,0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(-.8,.8)
    glVertex2f(-.65,.65)
    glEnd()

def lineasSol3():
    glColor3f(0.9,0.9,0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(-1,1)
    glVertex2f(-.55,.9)
    glEnd()

def lineaspasto1():
    glColor3f(0.2,0.3,0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(-.4,-.9)
    glVertex2f(-.3,-.8)
    glEnd()

def lineaspasto2():
    glColor3f(0.2,0.3,0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(-.3,-.8)
    glVertex2f(-.2,-.9)
    glEnd()
def lineaspasto3():
    glColor3f(0.2,0.3,0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(.4,-.97)
    glVertex2f(.3,-.88)
    glEnd()

def lineaspasto4():
    glColor3f(0.2,0.3,0.1)
    glLineWidth(6.0)
    glBegin(GL_LINES)
    glVertex2f(.3,-.88)
    glVertex2f(.2,-.97)
    glEnd()

def dibujar():
    #rutinas de dibujo
    dibujarSol()
    dibujarCesped()
    dibujarCasita()
    dibujarTriangulito()
    dibujarVentana()
    dibujarPuerta()
    dibujarPerilla()
    dibujarTronco()
    dibujarhojas1()
    dibujarhojas2()
    dibujarhojas3()
    dibujarhojas4()
    dibujarNubes11()
    dibujarNubes12()
    dibujarNubes13()
    dibujarNubes21()
    dibujarNubes22()
    dibujarNubes23()
    dibujarNubes31()
    dibujarNubes32()
    dibujarNubes33()
    lineasSol1()
    lineasSol2()
    lineasSol3()
    lineaspasto1()
    lineaspasto2()
    lineaspasto3()
    lineaspasto4()

    #glBegin(GL_TRIANGLES)
    
    #glEnd()

#------------------------------------------------------------------------------------------------#

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Casita", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0,0.5,0.9,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()