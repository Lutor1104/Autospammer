import pyautogui
while True:
    f = open("File", "r") #replace file with your txt file
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
