import pygame,sys
from configuraciones import *
from random import randint
from funciones import *
import json

pygame.init()


# CONFIGURACIONES PANTALLA 
pantalla = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pet.Guns")

button_comenzar=pygame.Rect(400,200,button_width,button_height)
button_musica_on=pygame.Rect(400,300,button_width,button_height)
button_musica_off=pygame.Rect(400,400,button_width,button_height)
button_salir=pygame.Rect(400,500,button_width,button_height)

contador = 0
max_contador = 0

# ESCRIBO FUENTE 
fuente = pygame.font.SysFont(None ,48)
texto = fuente.render(f"PUNTOS: {contador}",True,white,black)
rect_texto = texto.get_rect()
rect_texto = (0,0) 

#CONTROLAR FPS 
clock = pygame.time.Clock()
fondo = pygame.image.load("./src/imagenes/paisaje.png").convert()
inicio = pygame.image.load("./src/imagenes/inicio.jpg").convert()
pausa = pygame.image.load("./src/imagenes/pause.jpg").convert()
game_over = pygame.image.load("./src/imagenes/game.over.jpg").convert()

donna = crear_bloque(imagen_personaje,cord_x,cord_y,50,50,speed_x,speed_y)
laser = None
move_up = False
move_down = False
move_right = False
move_left = False

#MONEDAS DEL JUEGO 
coins = []
cargar_nuevos_coins(coins, 25, coins_imagen)
    
#------------------------------------------------
#SONIDOS
musica_colision = pygame.mixer.Sound("./src/SONIDOS/ladra.mp3")
musica_coins = pygame.mixer.Sound("./src/SONIDOS/sonidocoin.mp3")
pygame.mixer.music.load("./src/SONIDOS/musica.ambiente.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
playing_music=True
game_over_sonido=pygame.mixer.Sound("./src/SONIDOS/game.over.mp3")
sonido_colision_laser=pygame.mixer.Sound("./src/SONIDOS/colision.mp3")
#TRUCOS
trick_reverse = False
high_score_file = "high_score.json"



while True:
      #pantalla inicio
      pantalla.fill(black) 
      pantalla.blit(inicio, origin)
      wait_user_click(pantalla,button_comenzar,button_salir,button_musica_on,button_musica_off)
      pygame.display.flip()
      contador = 0
      vidas = 3
      is_running = True
      texto_lives = fuente.render(f"Vidas: {vidas}", True,white,black)
      rect_texto_live = texto_lives.get_rect(topright = (width, 0))
      malos=[]
      cargar_enemigos(malos, cant_enemigos,imagen_malos)


      #actualizar eventos 
      while is_running:
            clock.tick(FPS)

            for eventos in pygame.event.get():
                  if eventos.type == pygame.QUIT:
                     sys.exit()
                        #movimientos de personaje principal 
                  if eventos.type == pygame.KEYDOWN:
                        if eventos.key == pygame.K_LEFT:
                              move_left = True
                              move_right = False
                        if eventos.key == pygame.K_RIGHT:
                              move_right = True
                              move_left = False
                        if eventos.key == pygame.K_DOWN:
                              move_down = True
                              move_up = False
                        if eventos.key == pygame.K_UP:
                              move_up = True
                              move_down = False
                  
                        # disparo de laser 
                        if eventos.key == pygame.K_w:
                             if not laser:
                              size_laser = (5,10)
                              speed_laser = 6
                              laser_width , laser_heigh = size_laser
                              midtop = donna["rect"].midtop
                              laser = crear_bloque(None,midtop[0]-laser_width /2 ,midtop[1] - laser_heigh, laser_width, laser_heigh, red,velocidad_y == speed_laser)

                        if eventos.key ==pygame.K_t:
                              trick_reverse=True
                        #movimientos personaje principal 
                  if eventos.type == pygame.KEYUP:
                        if eventos.key == pygame.K_LEFT:
                              move_left = False
                        if eventos.key == pygame.K_RIGHT:
                              move_right = False
                        if eventos.key == pygame.K_DOWN:
                              move_down = False
                        if eventos.key == pygame.K_UP:
                              move_up = False
                        if eventos.key == pygame.K_x:
                        #pausar musica de fondo 
                              if playing_music:
                                    pygame.mixer_music.pause()
                              else:
                                    pygame.mixer_music.unpause()
                              playing_music=not playing_music
                        #pausa juego 
                        if eventos.key == pygame.K_p:
                              if playing_music:
                                    pygame.mixer_music.pause()
                              pantalla.blit(pausa, origin)
                              pygame.display.flip()
                              wait_user()
                              if playing_music:
                                    pygame.mixer_music.unpause()
                              #trucos 
                        if eventos.key == pygame.K_t:
                              trick_reverse=False
            
                  #rebote derecha pantalla 
            
            if move_right and donna["rect"].right <= (width - SPEED):
                  # Derecha
                  donna["rect"].left += SPEED
            if move_left and donna["rect"].left >= (0 + SPEED):
                  # Izquierda
                  donna["rect"].left -= SPEED
            if move_up and donna["rect"].top >= SPEED:
                  # Arriba
                  donna["rect"].top -= SPEED
            if move_down and donna["rect"].bottom < height - SPEED:
                  # Abajo
                  donna["rect"].top += SPEED


            for malo in malos:
                  if malo["rect"].right >= width:
                        if malo["dir"] == DR:
                              malo["dir"] = DL
                        elif malo["dir"] == UR:
                              malo["dir"] = UL
                  #rebote izquierda pantalla 
                  elif malo["rect"].left <= 1:
                        if malo["dir"] == DL:
                              malo["dir"] = DR
                        elif malo["dir"] == UL:
                              malo["dir"] = UR
                  #rebote abajo pantalla 
                  elif malo["rect"].bottom >= height:
                        if malo["dir"] == DR:
                              malo["dir"] = UR
                        elif malo["dir"] == DL:
                              malo["dir"] = UL
                  #rebote arriba pantalla 
                  elif malo["rect"].top <= 1:
                        if malo["dir"] == UL:
                              malo["dir"] = DL
                        elif malo["dir"] == UR:
                              malo["dir"] = DR
                  #-----------------------------
            for malo in malos:    
                  if malo["dir"] == DR:
                        malo["rect"].top += SPEED
                        malo["rect"].left += SPEED

                  elif malo["dir"] == DL:
                        malo["rect"].top += SPEED
                        malo["rect"].left -= SPEED
                        
                  elif malo["dir"] == UL:
                        malo["rect"].top -= SPEED
                        malo["rect"].left -= SPEED
                        
                  elif malo["dir"] == UR:
                        malo["rect"].left += SPEED
                        malo["rect"].top -= SPEED 

                  #detectamos colsion de los laser con los gatos 

                  if laser:           
                     colision=False             
                     for malo in malos:
                          if detectar_colision(malo["rect"],laser["rect"]):
                              malos.remove(malo)
                              colision = True
                              sonido_colision_laser.play()
                     if colision == True:
                       laser=None
                  
                  #detectamos colision de los puntos con personaje principal 
                       
                  for coin in coins:
                    if detectar_colision(coin["rect"],donna["rect"]):
                        coins.remove(coin)
                        contador += 1
                        texto = fuente.render(f"PUNTOS: {contador}",True,white,black)
                        rect_texto = texto.get_rect()
                        rect_texto = (0,0)
                        musica_coins.play()
                        if len(coins)==0   :
                             cargar_nuevos_coins(coins,25,coins_imagen)

                  for malo in malos:
                        if detectar_colision(malo["rect"], donna["rect"]):
                              malos.remove(malo)
                              if vidas > 1 :
                                    musica_colision.play()
                                    vidas -=  1 
                                    texto_lives = fuente.render(f"Vidas: {vidas}", True,white,black)
                                    rect_texto_live = texto_lives.get_rect(topright = (width, 0))
                              else:
                                    is_running = False
                  
                  if len(malos) == 0:
                        cant_enemigos += 1
                        cargar_enemigos(malos, cant_enemigos ,imagen_malos)
                       
                              
            #muevo el laser 
            if laser:
              if laser["rect"].bottom >= 0 :
                  laser["rect"].move_ip(0,-laser["velocidad_y"])
              else:
                   laser = None

            pantalla.blit(fondo, [0,0]) 

            # #creamos un truco 
            
            if  trick_reverse:
                  if laser: 
                       laser["velocidad_y"] += 10
                       
                       
            #ZONA DE DIBUJO
            if laser:
                  pygame.draw.rect(pantalla,laser["color"],laser["rect"])
      
            pantalla.blit(texto,rect_texto)
            pantalla.blit(texto_lives,rect_texto_live)
            
            dibujar_coins(pantalla, coins)
            dibujar_coins(pantalla, malos)
            pantalla.blit(donna["imagen"],donna["rect"])
            
            pygame.display.flip()

            try:
                  with open(high_score_file, "r") as file:
                        high_score_data = json.load(file)
                        max_contador = high_score_data.get("max_contador", 0)
            except FileNotFoundError:
            # If the file doesn't exist, set the initial high score to 0

                  max_contador = 0
            # After the game ends
            if contador > max_contador:
                  max_contador = contador
            if contador > max_contador:
                  max_contador = contador
            
            high_score_data = {"max_contador": max_contador}

            with open(high_score_file, "w") as file:
                  json.dump(high_score_data, file)


      
      pantalla.fill(black) 
      game_over_sonido.play()
      pantalla.blit(game_over, origin)
      mostar_texto(pantalla,f"max puntos: {max_contador}",fuente,(width // 2, 20),white,black)
      pygame.display.flip()
      wait_user()

terminar()