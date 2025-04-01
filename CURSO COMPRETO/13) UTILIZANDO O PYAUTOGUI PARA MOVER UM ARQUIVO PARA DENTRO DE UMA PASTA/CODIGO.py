import pyautogui
import time

# Tempo para trocar de janela antes de iniciar o script (opcional)
time.sleep(5)

# Coordenadas do arquivo e da pasta (Ajuste conforme necessário)
x_arquivo, y_arquivo = 300, 400  # Posição inicial do arquivo
x_pasta, y_pasta = 600, 400      # Posição da pasta de destino

# Clicar e segurar no arquivo
pyautogui.moveTo(x_arquivo, y_arquivo, duration=1)  # Move até o arquivo
pyautogui.mouseDown()  # Pressiona o botão do mouse

# Arrastar até a pasta
pyautogui.moveTo(x_pasta, y_pasta, duration=1)  # Move até a pasta

# Soltar o arquivo na pasta
pyautogui.mouseUp()

print("✅ Arquivo movido com sucesso!")
