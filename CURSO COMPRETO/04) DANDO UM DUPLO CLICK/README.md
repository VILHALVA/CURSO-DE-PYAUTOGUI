# PROJETO: MOVENDO E DANDO DUPLO CLIQUE AUTOMATICAMENTE
Este script fará o mouse **se mover para diferentes posições e dar um duplo clique** em cada uma delas.  

## **📄 1. Código do Projeto**  
Crie um arquivo **`CODIGO.py`** e adicione o seguinte código:  

```python
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
```

## **🚀 2. Como Executar**  
1️⃣ **Salve o arquivo** como `mover_e_duplo_clique.py`.  
2️⃣ **Execute o script:**  
   ```bash
   python CODIGO.py
   ```  
3️⃣ O mouse **se moverá para diferentes posições e dará um duplo clique automaticamente**.  

## **🔍 Explicação do Código**  
✔ **`pyautogui.size()`** → Obtém a resolução da tela.  
✔ **Lista `posicoes`** → Define pontos estratégicos para clicar.  
✔ **`pyautogui.moveTo(x, y, duration=1)`** → Move o mouse suavemente.  
✔ **`pyautogui.doubleClick()`** → Simula um duplo clique do mouse.  
✔ **`time.sleep(1)`** → Aguarda 1 segundo entre os cliques.  

## **🎯 Desafios Extras**  
1️⃣ Use **`pyautogui.rightClick()`** para fazer um duplo clique com o botão direito.  
2️⃣ Faça o script **clicar duas vezes em um botão de um site** e simular um duplo clique real.  
3️⃣ Modifique para capturar a posição do mouse antes de clicar (`pyautogui.position()`).  
