# PROJETO: LOOP QUE SÓ CLICA QUANDO A IMAGEM FOR DETECTADA
Para criar um **loop que só clica quando uma imagem for detectada** na tela, podemos usar o **PyAutoGUI** para localizar a imagem e então realizar a ação de clique. O PyAutoGUI tem a função `pyautogui.locateOnScreen()` que permite procurar uma imagem na tela e retornar a posição dela, se encontrada.

Aqui está um exemplo de como fazer isso:

## **1. Instale o PyAutoGUI**
Se você ainda não tem o **PyAutoGUI** instalado, use o seguinte comando:

```bash
pip install pyautogui
```

## **2. Preparando a Imagem**
Antes de usar a função de detecção de imagem, você deve ter uma imagem salva em seu computador. Certifique-se de que a imagem que você deseja localizar na tela esteja no formato PNG ou JPEG e tenha um nome simples.

## **3. Exemplo de Código para Criar um Loop que Só Clica Quando a Imagem For Detectada**
Crie um arquivo chamado **`CODIGO.py`** e adicione o seguinte código:

```python
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
```

## **4. Como Funciona o Código**  
- **`pyautogui.locateOnScreen(imagem_caminho)`** → Localiza a imagem na tela. Se a imagem for encontrada, retorna a posição dela. Caso contrário, retorna `None`.
- **`pyautogui.center(imagem)`** → Obtém as coordenadas do centro da imagem encontrada.
- **`pyautogui.click(centro_imagem)`** → Realiza um clique no centro da imagem detectada.
- O loop continua verificando a tela a cada 1 segundo e só realiza o clique quando a imagem for encontrada.

## **5. Ajustando o Intervalo de Busca**  
Você pode ajustar o tempo de espera entre cada busca modificando o **`time.sleep(1)`**. Se você quiser buscar mais frequentemente, diminua o valor (por exemplo, `time.sleep(0.5)`). Se preferir que o script procure com menos frequência, aumente o tempo.

## **🔍 Explicações Adicionais**  
- **Precisão da Detecção de Imagem**: A função `locateOnScreen()` pode ser sensível a mudanças na resolução da tela, cor e outros fatores. Certifique-se de que a imagem a ser detectada seja o mais fiel possível ao que aparece na tela.  
- **Otimização**: Este loop pode consumir muitos recursos do sistema dependendo da frequência de busca. Usar um intervalo de tempo adequado entre as buscas ajuda a evitar sobrecarga da CPU.

## **🎯 Desafios Extras**  
1️⃣ **Adicione uma condição de parada no loop**, como por exemplo, clicar 5 vezes e depois terminar a execução.  
2️⃣ **Detecte várias imagens**. Adapte o código para procurar por diferentes imagens e realizar ações específicas dependendo de qual imagem foi detectada.  
3️⃣ **Adicione um contador de tentativas**, que irá tentar um número específico de vezes antes de desistir de procurar a imagem.

Esse projeto pode ser útil para automatizar cliques em elementos de interface gráfica (como botões, ícones ou notificações) que você precisa identificar e interagir.