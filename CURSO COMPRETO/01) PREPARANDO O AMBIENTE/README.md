# PREPARANDO O AMBIENTE
Antes de começar a automação com **PyAutoGUI**, é importante garantir que o ambiente esteja configurado corretamente.  

## 📌 **1. INSTALAR O PYAUTOGUI**  
Abra o terminal (ou Prompt de Comando no Windows) e execute:  

```bash
pip install pyautogui
```

Para verificar se a instalação foi bem-sucedida, abra o **Python** no terminal e execute:  

```python
import pyautogui
print(pyautogui.size())  # Exibe a resolução da tela
```

Se não houver erro, o PyAutoGUI está instalado corretamente.  

## ⚙️ **2. INSTALAR DEPENDÊNCIAS ADICIONAIS (OPCIONAL)**  
Algumas funções do PyAutoGUI podem exigir bibliotecas extras:  

- **Para capturas de tela e reconhecimento de imagem**:  
  ```bash
  pip install pillow
  ```  
- **Para detectar teclas pressionadas**:  
  ```bash
  pip install keyboard
  ```  

No Linux, pode ser necessário instalar `scrot` para capturas de tela:  

```bash
sudo apt install scrot
```

## 🔍 **3. TESTAR O AMBIENTE**  
Crie um arquivo **`teste.py`** e adicione o seguinte código:  

```python
import pyautogui

# Exibir informações da tela
print(f"Resolução da tela: {pyautogui.size()}")
print(f"Posição atual do cursor: {pyautogui.position()}")
```

Agora, execute o script:  

```bash
python teste.py
```

Se os valores forem exibidos corretamente, o ambiente está pronto para automação! 🚀  

