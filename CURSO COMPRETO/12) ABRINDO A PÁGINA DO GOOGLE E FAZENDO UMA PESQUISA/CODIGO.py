import pyautogui
import subprocess
import time

# Caminho do navegador Edge. Ajuste o caminho conforme necessário no seu sistema.
caminho_edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# URL do Google
url = 'https://www.google.com'

# Abrir o navegador e acessar o Google
subprocess.Popen([caminho_edge, url])

# Aguardar 5 segundos para o navegador abrir
time.sleep(5)

# Digitar a pesquisa no Google
pesquisa = "Automação com PyAutoGUI"
pyautogui.write(pesquisa)

# Pressionar "Enter" para buscar
pyautogui.press('enter')

# Aguardar os resultados carregarem
time.sleep(3)
