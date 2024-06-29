import pyautogui
import time

print("Posicione o cursor no ponto desejado.")
time.sleep(5)  # Dá tempo para você mover o cursor para o ponto desejado

# Obtém a posição atual do cursor do mouse
x, y = pyautogui.position()
print(f"A posição do cursor é: X = {x}, Y = {y}")
