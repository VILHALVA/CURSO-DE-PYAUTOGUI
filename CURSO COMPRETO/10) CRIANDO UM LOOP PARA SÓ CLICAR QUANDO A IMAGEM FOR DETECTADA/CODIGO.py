import pyautogui
import time

# Caminho da imagem que será buscada na tela
imagem_caminho = 'exemplo_imagem.png'  # Substitua pelo caminho correto da sua imagem

# Loop infinito que vai verificar a tela continuamente
while True:
    # Tenta localizar a imagem na tela
    imagem = pyautogui.locateOnScreen(imagem_caminho)
    
    if imagem:
        # A imagem foi encontrada, vamos clicar no centro dela
        centro_imagem = pyautogui.center(imagem)
        pyautogui.click(centro_imagem)
        print("Imagem encontrada e clique realizado!")
        
        # Pausa de 2 segundos entre cada tentativa para evitar sobrecarga de CPU
        time.sleep(2)
    else:
        print("Imagem não encontrada. Continuando a busca...")
        
    # Pausa de 1 segundo antes de buscar novamente (ajustável conforme necessidade)
    time.sleep(1)
