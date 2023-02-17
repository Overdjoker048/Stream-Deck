from pynput.keyboard import Listener, Key
from keyboard import is_pressed
import graphic

def main():

    def on_press(key):
        if is_pressed("ctrl+m"):
            graphic.run()

    def on_release(key):
        if key == Key.esc:
            return False

    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()