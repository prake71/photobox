#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""photobox - a photobox application
  
photobox is a application mainly written for use in combination with 
a Raspberry Pi Single Board Computer and a camera. 

"""

import pygame
import pygame.camera

# initialize pygame engine
pygame.init()
# to be on the save side, init camera in addition
pygame.camera.init()

# define some color constants, just for the case
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0 ,0)

size = (640, 480)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Photobox")

# game done?
done = False

# timer to regulate frame rate
clock = pygame.time.Clock()

# initialize camera
clist = pygame.camera.list_cameras()
print(clist)
if not clist:
    raise ValueError("Sorry, no cameras detected.")
cam = pygame.camera.Camera(clist[0], size)
cam.start()

# reserve some surface for the snapshots later on
snapshot = pygame.surface.Surface(size, 0, screen)


# -------------- Game Loop ----------------
while not done:
   # --- Event Loop
   for event in pygame.event.get():
    # if window closed set done to true
       if event.type == pygame.QUIT:
           done = True

   # --- Game Logic
   if cam.query_image():
       snapshot = cam.get_image(snapshot)

   # --- erase screen
   #screen.fill(WHITE)

   # --- blit snapshot to screen
   screen.blit(snapshot, (0,0))

   # --- flip virtual screen to real screen
   pygame.display.flip()

   # --- limit loop to 60 frames per second
   clock.tick(60)

   # --- display frame rate in window border
   pygame.display.set_caption("Photobox (fps: %.2f)" % (clock.get_fps()))

# close window and quit 
pygame.quit()

