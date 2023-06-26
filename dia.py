import pyautogui
import time


pyautogui.alert('Bom dia !')

# Acessar o Google 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(2)
# Abrir conta MD e o Zap da MD 
pyautogui.click(984,609, duration=2)
pyautogui.click(677,111, duration=2)
time.sleep(2)

#voltar para Área de Trabalho
pyautogui.hotkey('win', 'd')
time.sleep(2)

# Acessar o Google 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Abrir Conta pessoal e zap
pyautogui.click(765,644, duration=2)
pyautogui.click(52,114, duration=2)

pyautogui.alert('Bom dia , Liberado para uso.')
