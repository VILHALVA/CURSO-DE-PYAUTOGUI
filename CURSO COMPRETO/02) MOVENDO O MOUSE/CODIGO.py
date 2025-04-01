import pyautogui
import math
import time

# Configurações do círculo
raio = 100  # Tamanho do círculo
centro_x, centro_y = pyautogui.size()[0] // 2, pyautogui.size()[1] // 2  # Centro da tela
passos = 36  # Quantidade de pontos no círculo

print("O mouse começará a se mover em um círculo em 3 segundos...")
time.sleep(3)

# Move o mouse em um círculo
for i in range(passos + 1):
    angulo = (i / passos) * 2 * math.pi  # Calcula o ângulo
    x = centro_x + int(raio * math.cos(angulo))  # Calcula a posição X
    y = centro_y + int(raio * math.sin(angulo))  # Calcula a posição Y
    pyautogui.moveTo(x, y, duration=0.05)  # Move o mouse suavemente

print("Movimentação concluída!")
