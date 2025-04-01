import pyautogui
import time

# Mensagem inicial
print("O mouse começará a se mover e clicar em 3 segundos...")
time.sleep(3)

# Obtém a resolução da tela
largura, altura = pyautogui.size()

# Define algumas posições para clicar
posicoes = [
    (largura // 4, altura // 4),
    (largura // 2, altura // 2),
    (3 * largura // 4, altura // 4),
    (3 * largura // 4, 3 * altura // 4),
    (largura // 4, 3 * altura // 4)
]

# Move e clica em cada posição
for pos in posicoes:
    pyautogui.moveTo(pos[0], pos[1], duration=1)  # Move suavemente
    pyautogui.click()  # Clica
    print(f"Clicou na posição {pos}")
    time.sleep(1)  # Aguarda um segundo antes do próximo clique

print("Movimentação e cliques concluídos!")
