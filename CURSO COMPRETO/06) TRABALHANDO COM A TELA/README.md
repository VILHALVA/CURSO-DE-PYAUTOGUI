# PROJETO: TRABALHANDO COM A TELA (CAPTURA E LOCALIZAÇÃO)
Neste projeto, vamos usar **PyAutoGUI** para tirar uma captura de tela de uma área da tela e localizar essa imagem automaticamente na tela. O script irá procurar pela imagem capturada e clicar nela.

## **📄 1. Passos Antes de Executar**  
1️⃣ **Abra o aplicativo ou tela onde a imagem que você deseja localizar está presente.**  
2️⃣ **Tire uma captura de tela de um ícone ou área da tela que você deseja localizar automaticamente.**  
   - Use qualquer ferramenta de captura de tela (como **Snipping Tool** ou **Print Screen**) para capturar a área desejada.
   - **Salve essa captura** como **`imagem.png`** na mesma pasta do seu script.

## **📄 2. Código do Projeto**  
Crie um arquivo **`CODIGO.py`** e adicione o seguinte código:

```python
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
```

## **🚀 3. Como Executar**  
1️⃣ **Abra a tela ou aplicativo que contém o ícone ou área capturada.**  
2️⃣ **Salve a captura da área que você deseja localizar como `imagem.png`.**  
3️⃣ **Execute o script:**  
   ```bash
   python CODIGO.py
   ```  
4️⃣ O script procurará pela **imagem na tela**, moverá o mouse até ela e **clicará** na área encontrada.

## **🔍 Explicação do Código**  
✔ **`pyautogui.locateOnScreen(imagem)`** → Localiza a imagem na tela. Retorna as coordenadas da área onde a imagem foi encontrada.  
✔ **`pyautogui.center(localizacao)`** → Calcula o centro da área onde a imagem foi localizada.  
✔ **`pyautogui.moveTo(x, y, duration=1)`** → Move o mouse suavemente até o centro da imagem localizada.  
✔ **`pyautogui.click()`** → Clica na imagem encontrada.  
✔ **`time.sleep(5)`** → Dá tempo para o usuário preparar a tela antes de o script iniciar.

## **🎯 Desafios Extras**  
1️⃣ **Capture mais de uma imagem** e procure por elas na tela.  
2️⃣ **Automatize ações diferentes** após localizar a imagem (como arrastar ou digitar algo).  
3️⃣ **Ajuste a precisão da localização** usando o parâmetro `confidence` (requer OpenCV instalado).  

## **Instalando OpenCV** (para usar a opção `confidence`):
```bash
pip install opencv-python
```

Ajuste a linha de busca para:
```python
localizacao = pyautogui.locateOnScreen(imagem, confidence=0.8)
```

Agora, o código será mais flexível em reconhecer imagens com pequenas variações.  
