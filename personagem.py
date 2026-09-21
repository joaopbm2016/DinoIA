import pygame

class Player:
    def __init__(self, x, y, tamanho, IA):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.IA = IA
        self.Vel_y = 0
        self.G = 1
        self.forca_pulo = -20
        self.no_chao = True
        self.inx_anim = 0
        self.vel_anim = 0.125
        self.running = True
        self.time = 0
        self.spr = None
        self.DinoP=pygame.image.load("DinoP.png")
        self.DinoP=pygame.transform.scale(self.DinoP,(tamanho,tamanho))
        self.Dino=[]
        for i in range(0, 2):
            img=pygame.image.load(f"Dino{i}.png")
            img=pygame.transform.scale(img,(tamanho,tamanho))
            self.Dino.append(img)

    def pular(self):
        if self.no_chao:
            self.Vel_y = self.forca_pulo
            self.no_chao = False

    def aplicar_gravidade(self):
        self.Vel_y += self.G
        self.y += self.Vel_y

    def colisao_chao(self, N_chao):
        if self.y >= N_chao:
            self.y = N_chao
            self.Vel_y = 0
            self.no_chao = True

    def atualizar_animacao(self):
        if self.no_chao:
            self.inx_anim += self.vel_anim
            if self.inx_anim >= len(self.Dino):
                self.inx_anim = 0
            self.spr = self.Dino[int(self.inx_anim)]
        else:
            self.spr = self.DinoP

    def draw(self, tela):
        tela.blit(self.spr, (self.x, self.y))  

    def colidir(self, cacto):

        if cacto is None:
            return
        
        if (self.x + self.tamanho > cacto.x + 30 and 
            self.x < cacto.x + cacto.tamanhoX - 30 and # Ajustado para caixas mais precisas
            self.y + self.tamanho > cacto.y):

            self.running = False 
        