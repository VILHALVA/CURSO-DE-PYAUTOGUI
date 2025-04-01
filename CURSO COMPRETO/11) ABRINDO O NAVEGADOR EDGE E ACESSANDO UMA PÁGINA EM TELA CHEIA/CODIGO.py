import pyautogui
import subprocess
import time

# Caminho do navegador Edge. Ajuste o caminho conforme necessário no seu sistema.
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# URL que você quer acessar
url = 'https://www.exemplo.com'  # Substitua pela URL que você deseja abrir

# Abrir o navegador Edge
subprocess.Popen([caminho_edge, url])

# Espera 5 segundos para o navegador abrir
time.sleep(5)

# Simula a tecla F11 para colocar a janela em tela cheia
pyautogui.press('f11')

# Espera 3 segundos para garantir que a tela cheia foi ativada
time.sleep(3)

# Aqui você pode adicionar interações extras, como clicar em elementos na página, etc.
