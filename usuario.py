import pygame


class Usuario:
    def __init__(self):
        self.coordenada_mouse_x = 0
        self.coordenada_mouse_y = 0
        self.escolha = ''
        self.escolha_texto = ''
        self.pontos = 0

        self.papel = pygame.image.load('Imagens/open-hand.png')
        self.papel = pygame.transform.scale(self.papel, (312, 312))
        self.pedra = pygame.image.load('Imagens/hand-closed.png')
        self.pedra = pygame.transform.scale(self.pedra, (312, 312))
        self.tesoura = pygame.image.load('Imagens/letter-v.png')
        self.tesoura = pygame.transform.scale(self.tesoura, (312, 312))

    def rect_do_mouse(self, janela):
        self.escolha = pygame.draw.rect(janela, (120, 120, 120), (self.coordenada_mouse_x, self.coordenada_mouse_y,
                                        20, 20))
