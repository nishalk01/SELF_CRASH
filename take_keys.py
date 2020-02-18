from pynput import keyboard
from pynput.keyboard import Key, Controller
# The key combination to check
COMBINATIONS = [
    { keyboard.KeyCode(char='a')},
    {keyboard.KeyCode(char='A')}
]
def do_something(a):
    if(a=='a'):
        print(a+"is ok")
# The currently active modifiers
current = set()

def execute():
    pass
    #print ("Do Something")

def on_press(key):
    #print(key==keyboard.KeyCode(char='a'))
    if(key==keyboard.KeyCode(char='a')):
        keys='a'
        do_something(keys)
    if(key==keyboard.KeyCode(char='w')):
        pass
    if(key==keyboard.KeyCode(char='d')):
        print("d is pressed")
    if(key==keyboard.KeyCode(char='s')):
        print("s is pressed")
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
