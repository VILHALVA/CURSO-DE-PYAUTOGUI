# PROJETO: RECONHECENDO E UTILIZANDO UMA IMAGEM NA TELA
Para **reconhecer uma imagem na tela** e utilizá-la, como realizar uma ação após localizar a imagem (como clicar nela ou realizar outra interação), podemos expandir o conceito de captura de tela e localização de imagem. O **PyAutoGUI** permite buscar e interagir com imagens salvas ou capturadas na tela, de forma simples e eficiente.

A seguir, vou criar um exemplo onde o script **reconhece uma imagem na tela** e realiza uma ação, como clicar sobre ela. Isso pode ser útil, por exemplo, para automatizar a interação com botões, ícones, ou outros elementos gráficos.

Neste projeto, vamos usar **PyAutoGUI** para:
1. **Reconhecer uma imagem na tela.**
2. **Mover o mouse até o centro da imagem localizada.**
3. **Clicar na imagem.**

## **📄 1. Passos Antes de Executar**  
1️⃣ **Capture a imagem ou área desejada da tela.**  
   - Use uma ferramenta de captura de tela (como o **Snipping Tool** ou **Print Screen**) para capturar a área de interesse.
   - **Salve a imagem** como **`imagem.png`** na mesma pasta do seu script.

2️⃣ **Abra a aplicação ou janela que contém a imagem que você deseja reconhecer.**  
   - Pode ser uma janela de aplicativo, ícone na área de trabalho, ou qualquer outro elemento gráfico visível.

## **📄 2. Código do Projeto**  
Crie um arquivo **`CODIGO.py`** e adicione o seguinte código:

```python
import pyautogui
import time

# Mensagem inicial
print("O script começará a procurar pela imagem em 5 segundos...")
time.sleep(5)

# Nome da imagem a ser reconhecida
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
1️⃣ **Abra o aplicativo ou tela onde a imagem que você deseja localizar está presente.**  
2️⃣ **Capture a imagem que você deseja reconhecer** e salve como `imagem.png`.  
3️⃣ **Execute o script** para que ele localize a imagem na tela e realize a ação:
   ```bash
   python CODIGO.py
   ```

## **🔍 Explicação do Código**  
✔ **`pyautogui.locateOnScreen(imagem)`** → Localiza a imagem na tela. Retorna as coordenadas da área onde a imagem foi encontrada.  
✔ **`pyautogui.center(localizacao)`** → Calcula o centro da área onde a imagem foi localizada.  
✔ **`pyautogui.moveTo(x, y, duration=1)`** → Move o mouse suavemente até o centro da imagem localizada.  
✔ **`pyautogui.click()`** → Simula um clique na imagem encontrada.  
✔ **`time.sleep(5)`** → Dá tempo para o usuário preparar a tela antes de o script começar a procurar pela imagem.

## **🎯 Desafios Extras**  
1️⃣ **Reconheça várias imagens diferentes** e faça ações distintas para cada uma.  
2️⃣ **Use `pyautogui.doubleClick()`** para dar um duplo clique após localizar a imagem.  
3️⃣ **Ajuste a precisão da localização** usando o parâmetro `confidence` (para imagens com variações pequenas).  
4️⃣ **Automatize outras ações** após clicar na imagem, como preencher campos, mover janelas, ou enviar teclas.

## **📈 Aumentando a Precisão com `confidence`**  
Se você quiser melhorar a precisão do reconhecimento de imagens, pode ajustar o parâmetro `confidence`. Isso ajuda quando a imagem pode ter pequenas variações (como mudanças de cor ou resolução).

Exemplo:

```python
localizacao = pyautogui.locateOnScreen(imagem, confidence=0.8)
```

**Nota:** Para usar `confidence`, é necessário instalar o **OpenCV**:

```bash
pip install opencv-python
```

## **📍 Onde Usar Esse Projeto?**  
Este tipo de automação pode ser utilizado em tarefas como:  
- **Automatizar cliques em botões específicos de um aplicativo.**  
- **Interagir com jogos ou outros programas gráficos.**  
- **Navegar automaticamente por interfaces gráficas.**
