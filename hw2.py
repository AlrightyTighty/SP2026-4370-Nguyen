"""
COSC 4370 Homework #2
Rotate camera via arrow keys (up and down), you cannot rotate past 90 degrees in either direction

Press s to toggle shading
"""
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from collections import namedtuple

Vector3 = namedtuple("Vector3", ["x", "y", "z"])
Material = namedtuple("Material", ["ambient", "diffuse", "specular", "specular_exponent", "emissive"], defaults=[None])

class Color:
    def __init__(self, red, green, blue, alpha):
        self.red = red / 255
        self.green = green / 255
        self.blue = blue / 255
        self.alpha = alpha / 255
    
    def __iter__(self):
        return iter((self.red, self.green, self.blue))

UNITS_PER_AU = 10
EARTH_SIZE = 1
DAYS_PER_SECOND = 30
FRAME_RATE = 30

SUN_COLOR = Color(255, 255, 0, 255)
SUN_AMBIENT = Color(255, 255, 0, 255)
SUN_DIFFUSE = Color(255, 255, 0, 255)
SUN_SPECULAR = Color(255, 255, 0, 255)
SUN_EMISSIVE = Color(255, 255, 0, 255)
SUN_SPECULAR_EXPONENT = 0
SUN_MATERIAL = Material(SUN_AMBIENT, SUN_DIFFUSE, SUN_SPECULAR, SUN_SPECULAR_EXPONENT, SUN_EMISSIVE)

MERCURY_COLOR = Color(255, 0, 0, 255)
MERCURY_AMBIENT = Color(100, 0, 0, 255)
MERCURY_DIFFUSE = Color(220, 0, 0, 255)
MERCURY_SPECULAR = Color(255, 0, 0, 255)
MERCURY_SPECULAR_EXPONENT = 3
MERCURY_MATERIAL = Material(MERCURY_AMBIENT, MERCURY_DIFFUSE, MERCURY_SPECULAR, MERCURY_SPECULAR_EXPONENT)

VENUS_COLOR = Color(0, 255, 0, 255)
VENUS_AMBIENT = Color(0, 100, 0, 255)
VENUS_DIFFUSE = Color(0, 220, 0, 255)
VENUS_SPECULAR = Color(0, 255, 0, 255)
VENUS_SPECULAR_EXPONENT = 3
VENUS_MATERIAL = Material(VENUS_AMBIENT, VENUS_DIFFUSE, VENUS_SPECULAR, VENUS_SPECULAR_EXPONENT)

EARTH_COLOR = Color(0, 0, 255, 255)
EARTH_AMBIENT = Color(0, 0, 100, 255)
EARTH_DIFFUSE = Color(0, 0, 220, 255)
EARTH_SPECULAR = Color(0, 0, 255, 255)
EARTH_SPECULAR_EXPONENT = 3
EARTH_MATERIAL = Material(EARTH_AMBIENT, EARTH_DIFFUSE, EARTH_SPECULAR, EARTH_SPECULAR_EXPONENT)

MOON_COLOR = Color(200, 200, 200, 255)
MOON_AMBIENT = Color(80, 80, 80, 255)
MOON_DIFFUSE = Color(170, 170, 170, 255)
MOON_SPECULAR = Color(200, 200, 200, 255)
MOON_SPECULAR_EXPONENT = 0.3
MOON_MATERIAL = Material(MOON_AMBIENT, MOON_DIFFUSE, MOON_SPECULAR, MOON_SPECULAR_EXPONENT)

MARS_COLOR = Color(255, 0, 0, 255)
MARS_AMBIENT = Color(100, 0, 0, 255)
MARS_DIFFUSE = Color(220, 0, 0, 255)
MARS_SPECULAR = Color(255, 0, 0, 255)
MARS_SPECULAR_EXPONENT = 3
MARS_MATERIAL = Material(MARS_AMBIENT, MARS_DIFFUSE, MARS_SPECULAR, MARS_SPECULAR_EXPONENT)

ORBIT_COLOR = Color(80, 80, 80, 255)

enable_shading = False

class Planet:
    def __init__(self, au_from_sun, frequency, relative_size, color, material, anchor = None):
        self.orbital_radius = au_from_sun * UNITS_PER_AU
        self.frequency = frequency
        self.size = relative_size * EARTH_SIZE
        self.theta = 0
        self.position = Vector3(0, 0, 0)
        self.color = color
        self.anchor = anchor
        self.material = material
        self.update_position(0)

    def update_position(self, time_passed):
        theta_difference = time_passed / self.frequency * 2 * math.pi
        self.theta += theta_difference
        self.position = Vector3(math.cos(self.theta) * self.orbital_radius, 0, math.sin(self.theta) * self.orbital_radius)
        if self.anchor is not None:
            self.position = tuple(a + b for a, b in zip(self.position, self.anchor.position))

    def render_orbit(self):
        glPushMatrix()
        glDisable(GL_LIGHTING)
        glColor(*ORBIT_COLOR)
        glBegin(GL_LINE_LOOP)
        for i in range(360):
            angle = math.radians(i)
            if self.anchor is None:
                glVertex3f(math.cos(angle) * self.orbital_radius, 0, math.sin(angle) * self.orbital_radius)
            else:
                glVertex3f(math.cos(angle) * self.orbital_radius + self.anchor.position.x, 0, math.sin(angle) * self.orbital_radius + self.anchor.position.z)
        glEnd()
        glEnable(GL_LIGHTING)
        glPopMatrix()

    def render_self(self):
        global enable_shading
        if (enable_shading):
            glEnable(GL_LIGHTING)
        else:
            glDisable(GL_LIGHTING)
        glPushMatrix()
        glTranslatef(*self.position)
        glColor(*self.color)
        glMaterialfv(GL_FRONT, GL_AMBIENT, list(self.material.ambient))
        glMaterialfv(GL_FRONT, GL_DIFFUSE, list(self.material.diffuse))
        glMaterialfv(GL_FRONT, GL_SPECULAR, list(self.material.specular))
        glMaterialf(GL_FRONT, GL_SHININESS, self.material.specular_exponent)
        if self.material.emissive is not None:
            glMaterialfv(GL_FRONT, GL_EMISSION, list(self.material.emissive))
        glutSolidSphere(self.size, 50, 50)
        glMaterialfv(GL_FRONT, GL_EMISSION, (0, 0, 0, 1))
        glPopMatrix()

        

def main():
    global enable_shading
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Homework #2')
    glutInit()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-20, 20, -20, 20, -20, 20)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1))
    glEnable(GL_NORMALIZE)

    bodies = [
        Planet(0, 1, 2, SUN_COLOR, SUN_MATERIAL),
        Planet(1, 365.26, 1, EARTH_COLOR, EARTH_MATERIAL),
        Planet(0.39, 87.97, 0.38, MERCURY_COLOR, MERCURY_MATERIAL),
        Planet(0.72, 224.70, 0.72, VENUS_COLOR, VENUS_MATERIAL),
        Planet(1.5, 686.98, 0.53, MARS_COLOR, MARS_MATERIAL),
    ]

    bodies.append(Planet(1.5 * EARTH_SIZE / UNITS_PER_AU, 27.3, 0.27, MOON_COLOR, MOON_MATERIAL, bodies[1]))

    current_rotation = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    enable_shading = not enable_shading

        active_keys = pygame.key.get_pressed()

        if active_keys[pygame.K_UP]:
            current_rotation += 1
        if active_keys[pygame.K_DOWN]:
            current_rotation -= 1

        current_rotation = max(-90, min(current_rotation, 90))

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(current_rotation, 1, 0, 0)

        for body in bodies:
            body.update_position(DAYS_PER_SECOND / FRAME_RATE)
            body.render_orbit()
            body.render_self()

        pygame.display.flip()
        pygame.time.wait(1000 // FRAME_RATE)


main()
