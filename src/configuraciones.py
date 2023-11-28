import pygame,sys
from random import randint



#datos generales 
SIZE = (700,648)

#PERSONAJE PRINCIPAL 
cord_x = 400
cord_y = 300
speed_x = 0 
speed_y = 0

#imagenes 
imagen_personaje = pygame.image.load("./src/imagenes/donna.png")
imagen_malos = pygame.image.load("./src/imagenes/gatozombie.png")
coins_imagen = pygame.image.load("./src/imagenes/coins.png")

#DATOS PRINCIPALES 
UR = 9
DR = 3
DL = 1
UL = 7

origin = (0, 0)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

width = 700
height = 648
centro_pantalla = (width//2,height//2)

FPS = 60

#palomas y gatos 
SPEED=3
menos_longitud = 50
menos_altura = 50

#especificaciones de la moneda 
block_width = 50
block_height = 50
velocidad_x = 5
velocidad_y = 5
size_coins = 23
color = red
contador_moneda = 0

#LASER 
size_laser=(5,10)
speed_laser=6

    #gatos
      
UR = 9
DR = 3
DL = 1
UL = 7

SPEED = 4
menos_longitud = 50
menos_altura = 50
cant_enemigos = 6


button_width=200
button_height=50


#contadores de max puntos 
contador = 0
max_contador = 0

