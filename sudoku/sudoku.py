# Importando as bibliotecas
import pygame as pg
import pandas as pd
import random 
import math

# Cores do jogo
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul_claro = (200, 200, 255)
azul = (100, 100, 255)
branco = (255, 255, 255)

# Setando o display com a tela do jogo
window = pg.display.set_mode((1000,700))

# Inicializando a fonte do jogo
pg.font.init()

# Escolhendo a fonte e o tamanho do jogo
font = pg.font.SysFont("Courier New", 50, bold=True)

# Criando o tabuleiro do jogo, sem nenhum espaço em branco
tabuleiro_data = [["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                  ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                  ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                  ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                  ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                  ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                  ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                  ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                  ["n", "n", "n", "n", "n", "n", "n", "n", "n"]]

# Numeros preenchidos e em branco
jogo_data = [["n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
             ["n", "n", "n", "n", "n", "n", "n", "n", "n"]]

# Os dois primeiros servirão para um looping 
escondendo_numeros = True
tabuleiro_preenchido = True
# Começa os status de click como false m
click_last_status = False
# Click position -1 para começar fora do tabuleiro
click_position_x = -1
click_position_y = -1
# faz com que o zero seja ignorado no jogo
numero = 0

# Função do hover no tabuleiro
def Tabuleiro_Hover(window, mouse_position_x, mouse_position_y):
    # pixels de tamanho do quadrado
    quadrado = 66.7
    # Ajuste para dentro do jogo
    ajuste = 50
    # Indexando as posições de x e y para mapear o tabuleiro
    x = (math.ceil((mouse_position_x - ajuste) / quadrado) - 1)
    y = (math.ceil((mouse_position_y - ajuste) / quadrado) - 1)
    # setando a cor branca
    pg.draw.rect(window, branco, (0, 0, 1000, 700))
    # Setando a cor azul no Hover quando está dentro do tabuleiro mapeado
    if x >= 0 and x <= 8 and y >= 0 and y <=8:
        pg.draw.rect(window, azul_claro, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))


# Faz quase a mesma coisa que a de cima, mas armaneza o valor de X e Y em uma variável e adiciona a cor azul
def Celula_Selecionada(window, mouse_position_x, mouse_position_y, click_last_status, click, x, y):
    quadrado = 66.7
    ajuste = 50
    if click_last_status == True and click == True:
        x = (math.ceil((mouse_position_x - ajuste) / quadrado) - 1)
        y = (math.ceil((mouse_position_y - ajuste) / quadrado) - 1)
    if x >= 0 and x <= 8 and y >= 0 and y <=8:
        pg.draw.rect(window, azul, ((ajuste + x * quadrado, ajuste + y * quadrado, quadrado, quadrado)))
    return x, y

# Desenho do tabuleiro
def Tabuleiro(window):
    pg.draw.rect(window, preto, (50, 50, 600, 600), 6)
    pg.draw.rect(window, preto, (50, 250, 600, 200), 6)
    pg.draw.rect(window, preto, (250, 50, 200, 600), 6)
    pg.draw.rect(window, preto, (50, 117, 600, 67), 2)
    pg.draw.rect(window, preto, (50, 317, 600, 67), 2)
    pg.draw.rect(window, preto, (50, 517, 600, 67), 2)
    pg.draw.rect(window, preto, (117, 50, 67, 600), 2)
    pg.draw.rect(window, preto, (317, 50, 67, 600), 2)
    pg.draw.rect(window, preto, (517, 50, 67, 600), 2)

# Desenha o botão de restart
def Botao_Restart(window):
    pg.draw.rect(window, verde, (700, 50, 250, 100))
    palavra = font.render("Restart", True, preto)
    window.blit(palavra, (725, 75))

# Verifica os números dentro da linha escolhida
def Linha_Escolhida(tabuleiro_data, y):
    linha_sorteada = tabuleiro_data[y]
    return linha_sorteada

# Armazena na coluna todos os números dela
def Coluna_Escolhida(tabuleiro_data, x):
    coluna_sorteada = []
    for n in range(8):
        coluna_sorteada.append(tabuleiro_data[n][x])
    return coluna_sorteada

# Verifica onde o número escolhido, com base em x e y, cai no tabuleiro
def Quadrante_Selecionado(tabuleiro_data, x, y):
    quadrante = []
    if x >=0 and x <=2 and y >=0 and y <=2:
        quadrante.extend([tabuleiro_data[0][0], tabuleiro_data[0][1], tabuleiro_data[0][2],
                          tabuleiro_data[1][0], tabuleiro_data[1][1], tabuleiro_data[1][2],
                          tabuleiro_data[2][0], tabuleiro_data[2][1], tabuleiro_data[2][2]])
    if x >=3 and x <=5 and y >=0 and y <=2:
        quadrante.extend([tabuleiro_data[0][3], tabuleiro_data[0][4], tabuleiro_data[0][5],
                          tabuleiro_data[1][3], tabuleiro_data[1][4], tabuleiro_data[1][5],
                          tabuleiro_data[2][3], tabuleiro_data[2][4], tabuleiro_data[2][5]])
    if x >=6 and x <=8 and y >=0 and y <=2:
        quadrante.extend([tabuleiro_data[0][6], tabuleiro_data[0][7], tabuleiro_data[0][8],
                          tabuleiro_data[1][6], tabuleiro_data[1][7], tabuleiro_data[1][8],
                          tabuleiro_data[2][6], tabuleiro_data[2][7], tabuleiro_data[2][8]])
    if x >=0 and x <=2 and y >=3 and y <=5:
        quadrante.extend([tabuleiro_data[3][0], tabuleiro_data[3][1], tabuleiro_data[3][2],
                          tabuleiro_data[4][0], tabuleiro_data[4][1], tabuleiro_data[4][2],
                          tabuleiro_data[5][0], tabuleiro_data[5][1], tabuleiro_data[5][2]])
    if x >=3 and x <=5 and y >=3 and y <=5:
        quadrante.extend([tabuleiro_data[3][3], tabuleiro_data[3][4], tabuleiro_data[3][5],
                          tabuleiro_data[4][3], tabuleiro_data[4][4], tabuleiro_data[4][5],
                          tabuleiro_data[5][3], tabuleiro_data[5][4], tabuleiro_data[5][5]])
    if x >=6 and x <=8 and y >=3 and y <=5:
        quadrante.extend([tabuleiro_data[3][6], tabuleiro_data[3][7], tabuleiro_data[3][8],
                          tabuleiro_data[4][6], tabuleiro_data[4][7], tabuleiro_data[4][8],
                          tabuleiro_data[5][6], tabuleiro_data[5][7], tabuleiro_data[5][8]])
    if x >=0 and x <=2 and y >=6 and y <=8:
        quadrante.extend([tabuleiro_data[6][0], tabuleiro_data[6][1], tabuleiro_data[6][2],
                          tabuleiro_data[7][0], tabuleiro_data[7][1], tabuleiro_data[7][2],
                          tabuleiro_data[8][0], tabuleiro_data[8][1], tabuleiro_data[8][2]])
    if x >=3 and x <=5 and y >=6 and y <=8:
        quadrante.extend([tabuleiro_data[6][3], tabuleiro_data[6][4], tabuleiro_data[6][5],
                          tabuleiro_data[7][3], tabuleiro_data[7][4], tabuleiro_data[7][5],
                          tabuleiro_data[8][3], tabuleiro_data[8][4], tabuleiro_data[8][5]])
    if x >=6 and x <=8 and y >=6 and y <=8:
        quadrante.extend([tabuleiro_data[6][6], tabuleiro_data[6][7], tabuleiro_data[6][8],
                          tabuleiro_data[7][6], tabuleiro_data[7][7], tabuleiro_data[7][8],
                          tabuleiro_data[8][6], tabuleiro_data[8][7], tabuleiro_data[8][8]])
    return quadrante

# Escreve os números para o quadrante 
def Preenchendo_Quadrantes(tabuleiro_data, x2, y2):
    quadrante_preenchido = True
    loop = 0
    try_count = 0
    numero = 1
    while quadrante_preenchido == True:
        x = random.randint(x2, x2 + 2)
        y = random.randint(y2, y2 + 2)
        linha_sorteada = Linha_Escolhida(tabuleiro_data, y)
        coluna_sorteada = Coluna_Escolhida(tabuleiro_data, x)
        quadrante = Quadrante_Selecionado(tabuleiro_data, x, y)
        if tabuleiro_data[y][x] == "n" and numero not in linha_sorteada and numero not in coluna_sorteada and numero not in quadrante:
            tabuleiro_data[y][x] = numero
            numero +=1
        loop +=1
        if loop == 50:
            tabuleiro_data[y2][x2] = "n"
            tabuleiro_data[y2][x2 + 1] = "n"
            tabuleiro_data[y2][x2 + 2] = "n"
            tabuleiro_data[y2 + 1][x2] = "n"
            tabuleiro_data[y2 + 1][x2 + 1] = "n"
            tabuleiro_data[y2 + 2][x2 + 2] = "n"
            tabuleiro_data[y2 + 2][x2] = "n"
            tabuleiro_data[y2 + 2][x2 + 1] = "n"
            tabuleiro_data[y2 + 2][x2 + 2] = "n"
            loop = 0
            numero = 1
            try_count += 1
        if try_count == 10:
            break
        count = 0
        for n in range(9):
            if quadrante[n] != "n":
                count +=1
        if count == 9:
            quadrante_preenchido = False
    return tabuleiro_data

# Reinicia o tabuleiro
def Reiniciando_Tabuleiro_Data(tabuleiro_data):
    tabuleiro_data = [["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                      ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                      ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                      ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                      ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                      ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                      ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                      ["n", "n", "n", "n", "n", "n", "n", "n", "n"],
                      ["n", "n", "n", "n", "n", "n", "n", "n", "n"]]
    return tabuleiro_data

# gera o tabuleiro no terminal
def Gabarito_do_Tabuleiro(tabuleiro_data, tabuleiro_preenchido):
    while tabuleiro_preenchido == True:
        # Quadrante 1
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 0, 0)
        # Quadrante 2
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 3, 0)
        # Quadrante 3
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 6, 0)
        # Quadrante 4
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 0, 3)
        # Quadrante 7
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 0, 6)
        # Quadrante 5
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 3, 3)
        # Quadrante 8
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 3, 6)
        # Quadrante 6
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 6, 3)
        # Quadrante 9
        tabuleiro_data = Preenchendo_Quadrantes(tabuleiro_data, 6, 6)
        for nn in range(9):
            for n in range(9):
                if tabuleiro_data[nn][n] == "n":
                    tabuleiro_data = Reiniciando_Tabuleiro_Data(tabuleiro_data)
        count = 0
        for nn in range(9):
            for n in range(9):
                if tabuleiro_data[nn][n] != "n":
                    count +=1
        if count == 81:
            tabuleiro_preenchido = False
    return tabuleiro_data, tabuleiro_preenchido    

# No terminal adiciona os "n" como espaços em branco
def Escondendo_Numeros(tabuleiro_data, jogo_data, escondendo_numeros):
    if escondendo_numeros == True:
        for n in range(40):
            sorteando_numeros = True
            while sorteando_numeros == True:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
                if jogo_data[y][x] == "n":
                    jogo_data[y][x] = tabuleiro_data[y][x]
                    sorteando_numeros = False
        escondendo_numeros = False
    return jogo_data, escondendo_numeros 

# Coloca os números no tabuleiro
def Escrevendo_Numeros(window, jogo_data):
    quadrado = 66.7
    ajuste = 67
    for nn in range(9):
        for n in range(9):
            if jogo_data[nn][n] != "n":
                palavra = font.render(str(jogo_data[nn][n]), True, preto)
                window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))
                if jogo_data[nn][n] == "X":
                    palavra = font.render(str(jogo_data[nn][n]), True, vermelho)
                    window.blit(palavra, (ajuste + n * quadrado, ajuste - 5 + nn * quadrado))

# Colocar o número do teclado e do teclado numérico como iguais
def Digitando_Numeros(numero):
    try:
        numero = int(numero[1])
    except:
        numero = int(numero)
    return numero

# Coloca o número digitado no tabuleiro e faz a checagem de acerto ou erro
def Checando_Numero_Digitado(tabuleiro_data, jogo_data, click_position_x, click_position_y, numero):
    x = click_position_x
    y = click_position_y
    # numero digitado = numero correto
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro_data[y][x] == numero and jogo_data[y][x] == "n" and numero != 0:
        jogo_data[y][x] = numero
        numero = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro_data[y][x] == numero and jogo_data[y][x] == numero and numero != 0:
        pass
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro_data[y][x] != numero and jogo_data[y][x] == "n" and numero != 0:
        jogo_data[y][x] = "X"
        numero = 0
    if x >= 0 and x <= 8 and y >= 0 and y <= 8 and tabuleiro_data[y][x] == numero and jogo_data[y][x] == "X" and numero != 0:
        jogo_data[y][x] = numero
        numero = 0
    return jogo_data, numero

# Fazendo o botão de restart funcionar
def Click_Botao_Restart(mouse_position_x, mouse_position_y, click_last_status, click, tabuleiro_preenchido, escondendo_numeros, tabuleiro_data, jogo_data):
    x = mouse_position_x
    y = mouse_position_y
    if x >= 700 and x <= 950 and y >= 50 and y <= 150 and click_last_status == False and click == True:
        tabuleiro_preenchido = True
        escondendo_numeros = True
        tabuleiro_data = Reiniciando_Tabuleiro_Data(tabuleiro_data)
        jogo_data = Reiniciando_Tabuleiro_Data(jogo_data)
    return tabuleiro_preenchido, escondendo_numeros, tabuleiro_data, jogo_data

# Looping do jogo 
while True:
    # Primeiro foi feito um for para identificar quando se fecha o jogo
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        # A variável número identifica qual tecla do teclado foi apertada
        if event.type == pg.KEYDOWN:
            numero = pg.key.name(event.key)
    # Declarando a variável da posição do mouse dentro do jogo
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]

    # Declarando a variável de click do mouse
    click = pg.mouse.get_pressed()

    # Jogo
    Tabuleiro_Hover(window, mouse_position_x, mouse_position_y)
    click_position_x, click_position_y = Celula_Selecionada(window, mouse_position_x, mouse_position_y, click_last_status, click[0], 
    click_position_x, click_position_y)
    Tabuleiro(window)
    Botao_Restart(window)
    tabuleiro_data, tabuleiro_preenchido = Gabarito_do_Tabuleiro(tabuleiro_data, tabuleiro_preenchido)
    jogo_data, escondendo_numeros = Escondendo_Numeros(tabuleiro_data, jogo_data, escondendo_numeros)
    Escrevendo_Numeros(window, jogo_data)
    numero = Digitando_Numeros(numero)
    jogo_data, numero = Checando_Numero_Digitado(tabuleiro_data, jogo_data, click_position_x, click_position_y, numero)
    tabuleiro_preenchido, escondendo_numeros, tabuleiro_data, jogo_data = Click_Botao_Restart(mouse_position_x, mouse_position_y, click_last_status, click[0], tabuleiro_preenchido, escondendo_numeros, tabuleiro_data, jogo_data)

    # Status pós click
    # Verdadeiro ou falso após o último click 
    if click[0] == True:
        click_last_status = True
    else:
        click_last_status = False
        
    pg.display.update()