import pygame,sys
from configuraciones import *
from random import randint




def iniciar_juego():
    pygame.init()

def configurar_pantalla():
    pantalla = pygame.display.set_mode(SIZE) 
    pygame.display.set_caption("Pet.Guns")
    
def escribir_fuente():
      # ESCRIBO FUENTE 
      fuente = pygame.font.SysFont(None ,48)
      texto = fuente.render(f"PUNTOS: {contador}",True,white,black)
      rect_texto = texto.get_rect()
      rect_texto = (0,0) 

def controlar_fps():
      #CONTROLAR FPS 
      clock = pygame.time.Clock()

def terminar():
    pygame.quit()
    exit() 

def mostar_texto(superficie,texto,fuente,cordenadas,color_fuente,color_fondo=black):
     sup_texto=fuente.render(texto,True,color_fuente,color_fondo)
     rect_texto=sup_texto.get_rect()
     rect_texto.center =cordenadas
     superficie.blit(sup_texto,rect_texto)
    
def crear_enemigo(imagen=None,left =  0, top = 0 , ancho = 100, alto = 100, color = (255,255,255), dir = dir, velocidad = 5):
    rec=pygame.Rect(left,top,ancho,alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
        
    return{"rect": rec, "color":color, "dir":dir, "velocidad" : velocidad, "imagen":imagen}

def cargar_enemigos(malos, cantidad,imagen = None):
      for i in range(cantidad):
            malos.append(crear_enemigo(imagen,left = randint(0, 700), top =randint(0, 100), ancho = 100, alto = 100, color = 0, dir = UR))

def dibujar_enemigos(pantalla,malos):
    
    for malo in malos:
        if malo["imagen"]:
            pantalla.blit(malo["imagen"], malo["rect"])
        else:
            pygame.draw.rect(pantalla, malo["color"], malo["rect"])


def wait_user():
     while True:
          for e in pygame.event.get():
               if e.type == pygame.QUIT:
                    terminar()
               if e.type == pygame.KEYDOWN:
                  if e.key == pygame.K_ESCAPE:
                        terminar()
                  return
               

#crear cuadrado 
def crear_bloque(imagen = None, left=0,top=0,ancho=80,alto=100,color=(255,255,255),dir=0,borde=0,radio=1,velocidad_x=5,velocidad_y=5):
    rec=pygame.Rect(left,top,ancho,alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
    return{"rect": rec, "color":color, "dir":dir,"borde":borde, "radio":radio,"velocidad_x":velocidad_x,"velocidad_y":velocidad_y, "imagen" : imagen}


    #creamos lista de moneda 
def cargar_nuevos_coins(coins, cantidad, imagen = None):
    for i in range(cantidad):
        coins.append(crear_bloque(imagen, randint(0,width-block_width),randint(0,height-size_coins), size_coins,size_coins))


def dibujar_coins(pantalla, coins):
    for coin in coins:
        if coin["imagen"]:
            pantalla.blit(coin["imagen"], coin["rect"])
        else:
            pygame.draw.rect(pantalla, coin["color"], coin["rect"], coin["borde"], coin["radio"])




#para detectar colisiones 
def detectar_colision(rect_1,rect_2):
    colision=False
    if punto_en_rectangulo(rect_1.topleft,rect_2) or punto_en_rectangulo(rect_1.topright,rect_2)or punto_en_rectangulo(rect_1.bottomright,rect_2) or punto_en_rectangulo(rect_1.bottomleft,rect_2) or punto_en_rectangulo(rect_2.topleft,rect_1) or punto_en_rectangulo(rect_2.topright,rect_1)or punto_en_rectangulo(rect_2.bottomright,rect_1) or punto_en_rectangulo(rect_2.bottomleft,rect_1):
       colision=True
       return colision              

def punto_en_rectangulo(punto,rect):
    x,y=punto
    return x > rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom 



def crear_boton (screen, rect, texto, color_normal, color_hover):
    posicion_mouse = pygame.mouse.get_pos()

    if rect.collidepoint(posicion_mouse) :
        pygame.draw.rect(screen, color_hover, rect, border_radius = 0)
    else:
        pygame.draw.rect(screen, color_normal, rect, border_radius = 0)
    mostrar_texto_2(screen, texto, rect.centerx, rect.centery)


def mostrar_texto_2(superficie, texto, x, y, font_size = 36, color = (0, 0, 0)):
    fuente = pygame.font.SysFont("Minecraft", font_size)
    render = fuente.render(texto, True, color)
    rect_texto = render.get_rect(center = (x, y))
    superficie.blit(render, rect_texto)



def wait_user_click(screen, button_comenzar, button_salir, button_musica_on, button_musica_off):
    while True:
        crear_boton(screen, button_comenzar, "Comenzar", white, red)

        crear_boton(screen, button_musica_on, "Musica On", white, red)

        crear_boton(screen, button_musica_off, "Musica Off", white, red)

        crear_boton(screen, button_salir, "Salir", white, red)
        
        pygame.display.flip()

        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                terminar()

            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_ESCAPE:
                    terminar()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                if eventos.button == 1:
                    if button_comenzar.collidepoint(eventos.pos):
                        return None
                    elif button_salir.collidepoint(eventos.pos):
                        terminar()
                    elif button_musica_off.collidepoint(eventos.pos):
                        if pygame.mixer.music.get_busy():
                              pygame.mixer.music.pause()
                    elif button_musica_on.collidepoint(eventos.pos):
                        if not pygame.mixer.music.get_busy():
                              pygame.mixer.music.unpause()
