import pygame
import random


class Tela:
    def __init__(self):
        self.lampada = True
        pygame.init()
        self.tamanho_da_tela = (1000, 700)
        self.janela = pygame.display.set_mode(self.tamanho_da_tela)
        pygame.display.set_caption('Pedra Papel Tesoura')
        self.icon = pygame.image.load('Imagens/v-live.png')
        pygame.display.set_icon(self.icon)
        self.flag_de_pontuacao = False
        self.msg_principal = pygame.font.Font('freesansbold.ttf', 70)
        self.msg_botoes = pygame.font.Font('freesansbold.ttf', 30)

        self.escolha_start = pygame.draw.rect(self.janela, (120, 120, 120), (100, 600, 100, 50))

        self.escolha_papel = pygame.draw.rect(self.janela, (120, 120, 120), (50, 500, 100, 50))

        self.escolha_pedra = pygame.draw.rect(self.janela, (120, 120, 120), (180, 500, 100, 50))

        self.escolha_tesoura = pygame.draw.rect(self.janela, (120, 120, 120), (310, 500, 120, 50))

        self.go = pygame.mixer.Sound('Sons/go.wav')
        self.menu = pygame.mixer.Sound('Sons/menu.wav')
        self.perda = pygame.mixer.Sound('Sons/no.wav')
        self.vitoria = pygame.mixer.Sound('Sons/vitoria.wav')
        self.empate = pygame.mixer.Sound('Sons/try_again.wav')

    def mensagem_principal(self):
        msg_principal_colocando = self.msg_principal.render('Pedra Papel Tesoura', True,
                                                            (255, 0, 0))
        self.janela.blit(msg_principal_colocando, (150, 0))

    def botao_para_escolha(self):

        self.escolha_papel = pygame.draw.rect(self.janela, (255, 0, 0), (50, 500, 100, 50))
        self.escolha_pedra = pygame.draw.rect(self.janela, (255, 0, 0), (180, 500, 100, 50))
        self.escolha_tesoura = pygame.draw.rect(self.janela, (255, 0, 0), (310, 500, 120, 50))
        self.escolha_start = pygame.draw.rect(self.janela, (255, 0, 0), (700, 500, 100, 50))

        escolha_papel_texto = self.msg_botoes.render('Papel', True, (0, 0, 0))
        self.janela.blit(escolha_papel_texto, (57, 510))

        escolha_pedra_texto = self.msg_botoes.render('Pedra', True, (0, 0, 0))
        self.janela.blit(escolha_pedra_texto, (187, 510))

        escolha_tesoura_texto = self.msg_botoes.render('Tesoura', True, (0, 0, 0))
        self.janela.blit(escolha_tesoura_texto, (313, 510))

        botao_start_texto = self.msg_botoes.render('Start', True, (0, 0, 0))
        self.janela.blit(botao_start_texto, (713, 510))

    def tela_aparecendo_escolha_usuario(self, usuario):
        pygame.draw.rect(self.janela, (120, 120, 120), (0, 100, 500, 350))

        if usuario.escolha_texto == 'Papel':
            self.janela.blit(usuario.papel, (80, 120))
        if usuario.escolha_texto == 'Tesoura':
            self.janela.blit(usuario.tesoura, (80, 120))
        if usuario.escolha_texto == 'Pedra':
            self.janela.blit(usuario.pedra, (80, 120))

    def tela_aparecendo_escolha_inimigo(self, inimigo):

        if inimigo.escolha_texto == 'Papel':
            pygame.draw.rect(self.janela, (120, 120, 120), (505, 100, 500, 350))
            self.janela.blit(inimigo.papel, (585, 120))

        if inimigo.escolha_texto == 'Tesoura':
            pygame.draw.rect(self.janela, (120, 120, 120), (505, 100, 500, 350))
            self.janela.blit(inimigo.tesoura, (585, 120))

        if inimigo.escolha_texto == 'Pedra':
            pygame.draw.rect(self.janela, (120, 120, 120), (505, 100, 500, 350))
            self.janela.blit(inimigo.pedra, (585, 120))

        if inimigo.escolha_texto == '':
            pygame.draw.rect(self.janela, (120, 120, 120), (505, 100, 500, 350))

    def colisao_escolha_dos_botoes(self, usuario, inimigo):

        if pygame.Rect.colliderect(usuario.escolha, self.escolha_papel):
            usuario.escolha_texto = 'Papel'
            inimigo.escolha_texto = ''
            self.menu.play()

        if pygame.Rect.colliderect(usuario.escolha, self.escolha_pedra):
            usuario.escolha_texto = 'Pedra'
            inimigo.escolha_texto = ''
            self.menu.play()

        if pygame.Rect.colliderect(usuario.escolha, self.escolha_tesoura):
            usuario.escolha_texto = 'Tesoura'
            inimigo.escolha_texto = ''
            self.menu.play()
        usuario.coordenada_mouse_x = usuario.coordenada_mouse_y = -100

        if pygame.Rect.colliderect(usuario.escolha, self.escolha_start):
            self.go.play()
            inimigo.escolha = random.randint(1, 3)

            if inimigo.escolha == 1:
                inimigo.escolha_texto = 'Pedra'
            if inimigo.escolha == 2:
                inimigo.escolha_texto = 'Tesoura'
            if inimigo.escolha == 3:
                inimigo.escolha_texto = 'Papel'

            usuario.coordenada_mouse_y = -10
            usuario.coordenada_mouse_x = -10
            pygame.time.delay(1000)
            self.flag_de_pontuacao = True

    def pontuacao(self, usuario, inimigo):
        if self.flag_de_pontuacao:
            pygame.time.delay(500)
            if usuario.escolha_texto == 'Pedra' and inimigo.escolha_texto == 'Papel':
                inimigo.pontos += 1
                self.perda.play()
            if usuario.escolha_texto == 'Papel' and inimigo.escolha_texto == 'Pedra':
                usuario.pontos += 1
                self.vitoria.play()
            if usuario.escolha_texto == 'Pedra' and inimigo.escolha_texto == 'Tesoura':
                usuario.pontos += 1
                self.vitoria.play()
            if usuario.escolha_texto == 'Tesoura' and inimigo.escolha_texto == 'Pedra':
                inimigo.pontos += 1
                self.perda.play()
            if usuario.escolha_texto == 'Tesoura' and inimigo.escolha_texto == 'Papel':
                usuario.pontos += 1
                self.vitoria.play()
            if usuario.escolha_texto == 'Papel' and inimigo.escolha_texto == 'Tesoura':
                inimigo.pontos += 1
                self.perda.play()
            if usuario.escolha_texto == inimigo.escolha_texto:
                self.empate.play()
            self.flag_de_pontuacao = False

    def mostrar_pontuacao(self, usuario, inimigo):

        pontuacao = self.msg_botoes.render(f'Usuario: {str(usuario.pontos)} X Robo: {str(inimigo.pontos)}',
                                           True, (120, 120, 120))
        self.janela.blit(pontuacao, (350, 610))

    def finalizando(self, usuario, inimigo):
        if usuario.pontos >= 10:
            self.janela.fill((0, 0, 0))
            msg_vitoria = self.msg_principal.render(f'Vitoria', True, (255, 0, 0))
            self.janela.blit(msg_vitoria, (350, 300))
        if inimigo.pontos >= 10:
            self.janela.fill((0, 0, 0))
            msg_derrota = self.msg_principal.render(f'Derrota', True, (255, 0, 0))
            self.janela.blit(msg_derrota, (350, 300))

    @staticmethod
    def atualizando_tela():
        pygame.display.update()
