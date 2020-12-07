import pygame
import sys

from definicoes_de_tela import Tela
from usuario import Usuario
from inimigo import Inimigo

tela = Tela()
usuario = Usuario()
inimigo = Inimigo()


while True:
    tela.janela.fill((0, 0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            usuario.coordenada_mouse_x = pygame.mouse.get_pos()[0]
            usuario.coordenada_mouse_y = pygame.mouse.get_pos()[1]

    tela.mensagem_principal()
    tela.botao_para_escolha()

    tela.tela_aparecendo_escolha_usuario(usuario)
    tela.tela_aparecendo_escolha_inimigo(inimigo)
    usuario.rect_do_mouse(tela.janela)
    tela.colisao_escolha_dos_botoes(usuario, inimigo)
    tela.pontuacao(usuario, inimigo)
    tela.mostrar_pontuacao(usuario, inimigo)
    tela.finalizando(usuario, inimigo)

    tela.atualizando_tela()
