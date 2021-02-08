import pyautogui, time

word = input("Word: ")
n = int(input("Number Of Spam Messages: "))

time.sleep(5)

for number in range(n):
    pyautogui.typewrite(str(word))
    pyautogui.press("enter")
