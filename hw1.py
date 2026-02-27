#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 Homework #1
This is the starter code for the first homework assignment.
It should run as is and will serve as the starting point for development.
"""
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def Cube():
    d = 1 / 3 ** 0.5
    verticies = (
        (d, -d, -d),
        (d, d, -d),
        (-d, d, -d),
        (-d, -d, -d),
        (d, -d, d),
        (d, d, d),
        (-d, -d, d),
        (-d, d, d)
        )

    edges = (
        (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
        (6,3), (6,4), (6,7), (5,1), (5,4), (5,7)
        )
    glColor(1,1,1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Octahedron():
    d = 1 / 2 ** 0.5
    verticies = (
        (0, -1, 0),
        (0, 1, 0),
        (-d, 0, -d),
        (-d, 0, d),
        (d, 0, -d),
        (d, 0, d),
        )

    edges = (
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (2, 3),
        (3, 5),
        (5, 4),
        (4, 2)
        )
    glColor(1,1,1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Tetrahedron():
    theta = math.acos(-1/3)
    verticies = (
        (0, 0, 1),
        (math.sin(theta) * math.cos(0),             math.sin(theta) * math.sin(0),             math.cos(theta)),
        (math.sin(theta) * math.cos(2*math.pi/3),   math.sin(theta) * math.sin(2*math.pi/3),   math.cos(theta)),
        (math.sin(theta) * math.cos(4*math.pi/3),   math.sin(theta) * math.sin(4*math.pi/3),   math.cos(theta)),
        )

    edges = (
        (0, 3),
        (1, 3),
        (2, 3),
        (0, 1),
        (1, 2),
        (2, 0)
        )
    glColor(1,1,1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Dodecahedron():
    phi = (1 + math.sqrt(5)) / 2
    d = 1 / math.sqrt(3)
    a = d / phi  #
    b = d * phi  


    # VERTICIES!!! (as given by google AI. i have no clue how geometry works)
    verticies = []
    # 8 cube vertices: (±d, ±d, ±d)
    for sx in (-1, 1):
        for sy in (-1, 1):
            for sz in (-1, 1):
                verticies.append((sx*d, sy*d, sz*d))
    # 12 vertices from (0, ±a, ±b), (±a, ±b, 0), (±b, 0, ±a)
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            verticies.append((0, s1*a, s2*b))
            verticies.append((s1*a, s2*b, 0))
            verticies.append((s1*b, 0, s2*a))

    edges = (
        (0, 8), (0, 9), (0, 10), (1, 9), (1, 11), (1, 13),
        (2, 10), (2, 12), (2, 14), (3, 12), (3, 13), (3, 17),
        (4, 8), (4, 15), (4, 16), (5, 11), (5, 15), (5, 19),
        (6, 14), (6, 16), (6, 18), (7, 17), (7, 18), (7, 19),
        (8, 14), (9, 15), (10, 13), (11, 17), (12, 18), (16, 19),
        )
    glColor(1,1,1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

    #holy crap it worked

def Icosahedron():
    theta1 = math.atan(0.5)
    theta_upper = math.pi/2 - theta1
    theta_lower = math.pi/2 + theta1

    verticies = []
    verticies.append((0, 0, 1))
    for i in range(5):
        a = 2 * math.pi * i / 5
        verticies.append((math.sin(theta_upper) * math.cos(a),
                          math.sin(theta_upper) * math.sin(a),
                          math.cos(theta_upper)))
    for i in range(5):
        a = 2 * math.pi * i / 5 + math.pi / 5
        verticies.append((math.sin(theta_lower) * math.cos(a),
                          math.sin(theta_lower) * math.sin(a),
                          math.cos(theta_lower)))
    verticies.append((0, 0, -1))

    edges = (
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 1),
        (1, 6), (1, 10),
        (2, 6), (2, 7),
        (3, 7), (3, 8),
        (4, 8), (4, 9),
        (5, 9), (5, 10),
        (6, 7), (7, 8), (8, 9), (9, 10), (10, 6),
        (11, 6), (11, 7), (11, 8), (11, 9), (11, 10),
        )
    glColor(1,1,1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def Axes():
    glBegin(GL_LINES)
    glColor(1,0,0) # Red for the x-axis
    glVertex3fv((0,0,0))
    glVertex3fv((1.5,0,0))
    glColor(0,1,0) # Green for the y-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,1.5,0))
    glColor(0,0,1) # Blue for the z-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,0,1.5))
    glEnd()


def Circle():
    glPushMatrix()
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -2, 2)
    glColor(1,0,1) # Purple for the limits
    glBegin(GL_LINE_LOOP)
    for i in range(36):
        angle = 2.0 * math.pi * i / 36
        x = math.cos(angle)
        y = math.sin(angle)
        glVertex3fv((x, y, 0))
    glEnd()
    glPopMatrix()
    

def render_text(text_array: list[tuple[str, int, int]], display):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, display[0], 0, display[1], -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    font = pygame.font.SysFont('Arial', 30)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    for text in text_array:
        controls_text_surface = font.render(text[0], True, (255, 255, 255))
        controls_text_surface = controls_text_surface.convert_alpha()
        controls_text_data = pygame.image.tostring(controls_text_surface, "RGBA", True)
        glRasterPos2d(text[1], text[2])
        glDrawPixels(controls_text_surface.get_width(), controls_text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, controls_text_data)

    glDisable(GL_BLEND)

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def main():
    pygame.init()
    display = (600,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Homework #1')
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)

    manual_controls = False

    last_pressed = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    last_pressed = pygame.K_1
                elif event.key == pygame.K_2:
                    last_pressed = pygame.K_2
                elif event.key == pygame.K_3:
                    last_pressed = pygame.K_3
                elif event.key == pygame.K_4:
                    last_pressed = pygame.K_4
                elif event.key == pygame.K_5:
                    last_pressed = K_5
                elif event.key == pygame.K_6:
                    manual_controls = not manual_controls

        keys = pygame.key.get_pressed()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Axes() # Draw the axes
        if (last_pressed == pygame.K_1):
            Cube()
        elif (last_pressed == pygame.K_2):
            Octahedron()
        elif (last_pressed == pygame.K_3):
            Tetrahedron()
        elif (last_pressed == pygame.K_4):
            Dodecahedron()
        elif (last_pressed == pygame.K_5):
            Icosahedron()
        Circle() # Draw the limit circle
        
        
        if (manual_controls):
            lshift_pressed = keys[K_LSHIFT]
            rotate_vector = [0, 0, 0]
            if (keys[K_a]):
                if (lshift_pressed):
                    rotate_vector[2] -= 1
                else:
                    rotate_vector[1] -= 1
            if (keys[K_d]):
                if (lshift_pressed):
                    rotate_vector[2] += 1
                else:
                    rotate_vector[1] += 1
            if (keys[K_w]):
                rotate_vector[0] += 1;
            if (keys[K_s]):
                rotate_vector[0] -= 1;

            glRotatef(1, rotate_vector[0], rotate_vector[1], rotate_vector[2])
        else:
            glRotatef(1, 1, 1, 1)

        text_to_render = [
            (manual_controls and "Press [6] to disable manual controls" or "Press [6] to enable manual controls", 10, 10)
        ]

        if (manual_controls):
            text_to_render.append(("W/S to rotate around X axis", 10, 40))
            text_to_render.append((keys[K_LSHIFT] and "A/D to rotate around Z axis (LShift to Change)" or "A/D to rotate around Y axis (LShift to Change)", 10, 70))
        render_text(text_to_render, display)


        pygame.display.flip()
        pygame.time.wait(10)


main()