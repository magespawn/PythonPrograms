import time
import sys

def type(text, delay):
    for beep in text:
        print(beep, end = "")
        sys.stdout.flush()
        time.sleep(delay)

py = input("Type: ") 

def decor(func):
    def wrap():
        print("=============" + "=" * len(py))
        func()
        print("=============" + "=" * len(py))
    return wrap

def print_text():
    type("Hello world! " + py + "\n", 0.2)

decorated = decor(print_text)
decorated()
