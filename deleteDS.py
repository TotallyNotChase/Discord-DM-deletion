import keyboard, sys

def exit():
    sys.exit()

if __name__ == "__main__":
    input("start")
    i = 0
    while i < 100:
        keyboard.press_and_release(keyboard.KEY_UP)
        keyboard.press_and_release("ctrl+a")
        keyboard.press_and_release("delete")
        keyboard.press_and_release("enter")
        keyboard.press_and_release("enter")
        i += 1
    
