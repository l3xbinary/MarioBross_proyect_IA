import pygame
from pygame.locals import *
import time 

COLOR = {
    'RED': (204,0,0),
    'GREEN': (51,255,51),
    'BLUE': (0,128,255),
    'BLACK': (0,0,0),
    'WHITE': (255,255,255),
    'ORANGE': (255,153,51),
    'DGREY' : (96,96,96),
    'GREY' : (128,128,128),
    'LGREY' : (192,192,192)
    }

class Option:
 
    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        if self.hovered:
        	(xp,yp) = self.pos
        	xp = xp-30
        	opt1 = pygame.image.load("pointer_r.png")
        	opt2 = pygame.image.load("pointer_l.png")
        	if self.text == "Nuevo":
        		screen.blit(opt1, (xp,yp))
        		screen.blit(opt2, (xp+112,yp))
      		elif self.text == "Salir":
          		screen.blit(opt1, (xp,yp))
          		screen.blit(opt2, (xp+96,yp))

        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (0, 0, 0)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos


########################## MARIO BROSS ##########################
"""Secuencia de comandos"""

# MENU #
pygame.init()

'Archivos del menu'
soundtrack = pygame.mixer.Sound("main.ogg")
clic_sound = pygame.mixer.Sound("select.ogg")
menu_brgnd = pygame.image.load("main_bkgnd.png")

'Confuguracion e pantalla'
screen = pygame.display.set_mode((655,455))
menu_font = pygame.font.Font(None, 34)

'Variables'
_menu = [Option("Nuevo", (300, 305)), Option("Salir", (308, 335))]
_opt_selected = 0


## Menu ##
soundtrack.play()
while _opt_selected == 0:
    pygame.event.pump()
    screen.fill((100, 100, 100))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.event.quit()

    if _menu[0].rect.collidepoint(pygame.mouse.get_pos()):
        _menu[0].hovered = True

        if event.type == pygame.MOUSEBUTTONDOWN:
          #Carga los parametros del juego nuevo
          soundtrack.stop()
          _opt_selected = 1
          status_game = 1

    else:
      	_menu[0].hovered = False

    if _menu[1].rect.collidepoint(pygame.mouse.get_pos()):
        _menu[1].hovered = True
        if event.type == pygame.MOUSEBUTTONDOWN:
          pygame.event.quit()
    else:
        _menu[1].hovered = False

    screen.blit(menu_brgnd, (0,0))
    for option in _menu:
      option.draw()

    pygame.display.flip()



if _opt_selected == 1:
################### Dentro del juego ###################
  # Codigo de inicio de juego 
  # Contruccion del ambiente/objetos/personajes
  # Carga de parametros iniciales

  while status_game == 1:
      event = pygame.event.poll()
      if event.type == pygame.QUIT:
          pygame.event.quit()

      screen.fill(COLOR['WHITE'])
      pygame.display.flip()
