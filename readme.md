# README

# Pokémon Counter Script

Este repositório contém um script Python que identifica e executa ações específicas com base em Pokémon detectados na tela. Utilizando as bibliotecas `pyautogui`, `cv2` e `numpy`, o script detecta Pokémon pré-determinados e realiza ações associadas a eles.

## Funcionalidades

- Marca a posição dos Pokémon na tela.
- Detecta Pokémon em tempo real usando captura de tela.
- Executa ações específicas ao detectar Pokémon.

## Requisitos

- Python 3.x
- Bibliotecas Python: `pyautogui`, `opencv-python`, `numpy`

## Instalação

1. Clone este repositório:

```bash
git clone https://github.com/guigasdev/script-otp-counter.git
cd script-otp-counter
```

2. Instale as dependências:

```bash
pip install pyautogui opencv-python numpy
```

## Uso

1. Execute o script:

```bash
python counter.py
```

2. Marque as posições dos Pokémon na tela:

    - Posicione o mouse sobre o Pokémon desejado e insira o número correspondente para marcar a posição.
    
    ```python
    primeiro_pokemon=str(input("posicione seu mouse e digite 1 para marcar posicao do primeiro pokémon: "))
    ```

3. O script começará a capturar a tela e procurar pelos Pokémon especificados nas posições marcadas.

4. Quando um Pokémon for detectado, a ação correspondente será executada.


