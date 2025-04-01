# PROJETO: DESENHANDO NO PAINT AUTOMATICAMENTE
Este script **abre o Paint, seleciona o pincel e desenha um círculo** automaticamente.  

## **📄 1. Passos Antes de Executar**  
1️⃣ **Abra o Paint** manualmente antes de rodar o código.  
2️⃣ **Maximize a janela** do Paint para garantir que o script funcione corretamente.  

## **📄 2. Código do Projeto**  
Crie um arquivo **`CODIGO.py`** e adicione o seguinte código:  

```python
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
```

## **🚀 3. Como Executar**  
1️⃣ **Abra o Paint** e maximize a janela.  
2️⃣ **Execute o script:**  
   ```bash
   python CODIGO.py
   ```  
3️⃣ **Não toque no mouse** enquanto o script estiver rodando.  
4️⃣ **O círculo será desenhado automaticamente**!  

## **🔍 Explicação do Código**  
✔ **`time.sleep(5)`** → Dá tempo para abrir o Paint.  
✔ **`pyautogui.moveTo(x, y)`** → Move o mouse para o ponto inicial do círculo.  
✔ **`pyautogui.mouseDown()`** → Pressiona o botão do mouse.  
✔ **`math.cos()` e `math.sin()`** → Calculam pontos do círculo.  
✔ **`pyautogui.mouseUp()`** → Solta o botão do mouse para finalizar o desenho.  

## **🎯 Desafios Extras**  
1️⃣ **Desenhe um quadrado ou uma estrela** usando `pyautogui.moveTo()`.  
2️⃣ **Mude o raio e a velocidade do desenho** ajustando `raio` e `duration`.  
3️⃣ **Use `pyautogui.click()` para selecionar a ferramenta de desenho automaticamente**.  

