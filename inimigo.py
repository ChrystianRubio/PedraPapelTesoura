import pygame


class Inimigo:
    def __init__(self):
        self.escolha = ''
        self.escolha_texto = ''
        self.pontos = 0

        self.papel = pygame.image.load('Imagens/open-hand.png')
        self.papel = pygame.transform.scale(self.papel, (312, 312))
        self.pedra = pygame.image.load('Imagens/hand-closed.png')
        self.pedra = pygame.transform.scale(self.pedra, (312, 312))
        self.tesoura = pygame.image.load('Imagens/letter-v.png')
        self.tesoura = pygame.transform.scale(self.tesoura, (312, 312))
