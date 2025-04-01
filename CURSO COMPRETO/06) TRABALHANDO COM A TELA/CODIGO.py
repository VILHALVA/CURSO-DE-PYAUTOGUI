import pyautogui
import time

# Mensagem inicial
print("O script começará a procurar pela imagem em 5 segundos...")
time.sleep(5)

# Localiza a imagem na tela
imagem = "imagem.png"  # Nome da imagem capturada

# Tenta encontrar a imagem na tela
localizacao = pyautogui.locateOnScreen(imagem)

# Verifica se a imagem foi localizada
if localizacao:
    print(f"Imagem encontrada na posição: {localizacao}")
    # Calcula o centro da imagem
    centro = pyautogui.center(localizacao)
    # Move o mouse até o centro da imagem
    pyautogui.moveTo(centro[0], centro[1], duration=1)
    # Clica na imagem
    pyautogui.click()
    print("Imagem clicada com sucesso!")
else:
    print("Imagem não encontrada na tela.")
