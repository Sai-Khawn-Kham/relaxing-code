import pyautogui
import time
import pyperclip

# Give yourself time to click into the Telegram chat box
time.sleep(5)

for i in range(10):
    message = f"{i+1} : I am sorry"
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(0.3)
print("done")