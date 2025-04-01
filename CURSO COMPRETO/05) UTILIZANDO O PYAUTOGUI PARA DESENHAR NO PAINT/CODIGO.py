import pyautogui
import math
import time

# Mensagem inicial
print("O desenho começará em 5 segundos...")
time.sleep(5)  # Tempo para abrir o Paint e selecionar o pincel

# Obtém o tamanho da tela
largura, altura = pyautogui.size()

# Define o centro da tela como ponto inicial do desenho
centro_x, centro_y = largura // 2, altura // 2

# Define o raio do círculo
raio = 100

# Move o mouse até o ponto inicial do círculo
pyautogui.moveTo(centro_x + raio, centro_y)

# Pressiona o botão do mouse para começar a desenhar
pyautogui.mouseDown()

# Desenha um círculo
for i in range(100):
    angulo = (i / 100) * 2 * math.pi  # Divide o círculo em 100 pontos
    x = centro_x + int(raio * math.cos(angulo))
    y = centro_y + int(raio * math.sin(angulo))
    pyautogui.moveTo(x, y, duration=0.01)

# Solta o botão do mouse para parar de desenhar
pyautogui.mouseUp()

print("Desenho concluído!")
