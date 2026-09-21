import pygame
import random
from personagem import Player
from cacto import Cacto

pygame.init()

fonte = pygame.font.SysFont("Arial",30)

largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Dino Games YOOO")

N_chao = 400 
tamanho = 100
xp = 100
yp = N_chao + tamanho  
Vel_y = 0 
G = 1     
forca_pulo = -20  
no_chao = True    
list_Players = []


yc =N_chao
xc = largura+tamanho
cacto_vel = -7
list_cactos = []
tamanhoCX =30
tamanhoCY =100
cacto_offset_X = 30


#for i in range(0, 10):
#    jogador[i] = Player(200, 500, 50)  # Inicializa o jogador na posição (400, 500) com tamanho 50
jogador = Player(xp, yp, tamanho, 0,)
list_Players.append(jogador)
jogadorIA = Player(xp, yp, tamanho, 1,)
list_Players.append(jogadorIA)


#cacto1 = Cacto(200, yc, tamanho, tamanhoCX, tamanhoCY, 0, cacto_vel)
#list_cactos.append(cacto1)
next_cacto=random.randint(0, 100)
timer_cacto=1000

# Controlador de FPS para o jogo não rodar rápido demais
Novo_cacto = pygame.USEREVENT+1
pygame.time.set_timer(Novo_cacto,1000)
Timer_cacto = pygame.USEREVENT+2
pygame.time.set_timer(Timer_cacto,3000)
relogio = pygame.time.Clock()
run = True

def proximo_cacto():
    for cacto in list_cactos:
        if cacto.x > jogador.x:
            return cacto    
        
    return None    

while run:
    relogio.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == Novo_cacto:
           next_cacto =random.randint(0, 2) 
           if next_cacto == 1:
            cacto_=Cacto(xc, yc, tamanho, tamanhoCX, tamanhoCY, 1,cacto_vel)
            list_cactos.append(cacto_)

        if event.type == Timer_cacto:
            if timer_cacto>10:
                timer_cacto-=5
                pygame.time.set_timer(Novo_cacto,timer_cacto)
                cacto_vel-=0.1


    tecla = pygame.key.get_pressed()

    for p in list_Players:
        if p.IA==0:
            if tecla[pygame.K_SPACE]:
                p.pular()
        else:
            if p.IA==1:
                if tecla[pygame.K_UP]:
                    p.pular()
        p.aplicar_gravidade()
        p.colisao_chao(N_chao)
            

    cacto_atual = proximo_cacto()
    if cacto_atual is not None:
        distancia_cacto = proximo_cacto().x-xp
    else:
        distancia_cacto = largura
    distancia_cacto /= largura

    tela.fill((30, 30, 40))

    for p in list_Players:
        p.colidir(cacto_atual)

        if p.running == True:
            p.atualizar_animacao()
            p.draw(tela)
        else:
            list_Players.remove(p)

    for cacto in list_cactos:
        cacto.Move()
        cacto.draw(tela)
        if cacto.x < -cacto.tamanho:
            list_cactos.remove(cacto)

    Num_tela_Vel = fonte.render(f"Vel cacto:{cacto_vel}", True, (255,255,255))
    Num_tela_timer = fonte.render(f"timer atual:{timer_cacto}",True, (255,255,255))
    distancia_cacto = fonte.render(f"Distancia cacto:{distancia_cacto}", True, (255, 255, 255))
    #for Dino in list_Players:


    tela.blit(Num_tela_timer ,(20,20))
    tela.blit(Num_tela_Vel,(20,50))
    tela.blit(distancia_cacto, (20, 80))
    pygame.draw.line(tela,(255,255,255), (0, N_chao+100), (largura, N_chao+100), 5)
    pygame.display.flip()

pygame.quit()
