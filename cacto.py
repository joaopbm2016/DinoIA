import pygame

class Cacto:
    def __init__(self, x, y, tamanho, tamanhoX, tamanhoY, mov, vel):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.tamanhoX = tamanhoX
        self.tamanhoY = tamanhoY    
        self.vel = vel
        self.mov = mov
        self.image = pygame.image.load("cacto.png")
        self.image = pygame.transform.scale(self.image, (tamanho, tamanho))

    def draw(self, tela):
        tela.blit(self.image, (self.x, self.y))

    def Move(self):
        if self.mov ==1:
            self.x += self.vel

    