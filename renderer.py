import pygame
from pygame.locals import DOUBLEBUF, OPENGL, QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN
from OpenGL.GL import *
from OpenGL.GLU import *
from model import building_model, draw_cube, draw_column, draw_wall, draw_roof

def start_render():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, -5.0, -20)
    rotation_x, rotation_y = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    rotation_y -= 5
                elif event.key == K_RIGHT:
                    rotation_y += 5
                elif event.key == K_UP:
                    rotation_x -= 5
                elif event.key == K_DOWN:
                    rotation_x += 5

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        render_model(rotation_x, rotation_y)
        pygame.display.flip()
        pygame.time.wait(10)

def render_model(rotation_x, rotation_y):
    glPushMatrix()
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)

    for fundament in building_model['fundaments']:
        draw_cube(*fundament['position'], fundament['length'], fundament['height'], fundament['width'])
        for element in building_model['elements'][fundament['id']]:
            if element['type'] == "wall":
                draw_wall(*element['position'], *element['size'])
            elif element['type'] == "column":
                draw_column(*element['position'], 0.5, element['size'][1])
            elif element['type'] == "roof":
                draw_roof(*element['position'], *element['size'])
    glPopMatrix()
