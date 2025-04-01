import pyautogui
import time

# Mensagem inicial
print("O mouse começará a se mover e dar duplo clique em 3 segundos...")
time.sleep(3)

# Obtém a resolução da tela
largura, altura = pyautogui.size()

# Define algumas posições para dar duplo clique
posicoes = [
    (largura // 3, altura // 3),
    (2 * largura // 3, altura // 3),
    (largura // 3, 2 * altura // 3),
    (2 * largura // 3, 2 * altura // 3)
]

# Move e dá duplo clique em cada posição
for pos in posicoes:
    pyautogui.moveTo(pos[0], pos[1], duration=1)  # Move suavemente
    pyautogui.doubleClick()  # Dá duplo clique
    print(f"Duplo clique na posição {pos}")
    time.sleep(1)  # Aguarda um segundo antes do próximo clique

print("Movimentação e duplo clique concluídos!")
