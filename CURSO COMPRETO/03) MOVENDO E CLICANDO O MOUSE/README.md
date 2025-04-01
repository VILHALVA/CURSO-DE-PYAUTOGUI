# PROJETO: MOVENDO E CLICANDO O MOUSE AUTOMATICAMENTE  
Este script fará o mouse se mover para diferentes posições na tela e clicar automaticamente.  

## **📄 1. Código do Projeto**  
Crie um arquivo **`CODIGO.py`** e adicione o seguinte código:  

```python
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
```

## **🚀 2. Como Executar**  
1️⃣ **Salve o arquivo** como `mover_e_clicar.py`.  
2️⃣ **Execute o script:**  
   ```bash
   python CODIGO.py
   ```  
3️⃣ O mouse **se moverá para diferentes posições e clicará automaticamente**.  

## **🔍 Explicação do Código**  
✔ **`pyautogui.size()`** → Obtém a resolução da tela.  
✔ **Lista `posicoes`** → Define pontos estratégicos para clicar.  
✔ **`pyautogui.moveTo(x, y, duration=1)`** → Move o mouse suavemente.  
✔ **`pyautogui.click()`** → Simula um clique do mouse.  
✔ **`time.sleep(1)`** → Aguarda 1 segundo entre os cliques.  

## **🎯 Desafios Extras**  
1️⃣ Modifique para **clicar duas vezes** (`pyautogui.doubleClick()`).  
2️⃣ Use **`pyautogui.rightClick()`** para simular um clique direito.  
3️⃣ Faça o script **clicar repetidamente em um botão de um site**.  

