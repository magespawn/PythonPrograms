import time
import sys

def type(text, delay):
    for beep in text:
        print(beep, end = "")
        sys.stdout.flush()
        time.sleep(delay)

type("What is your name?\n", 0.05)
type("I hope it is a good name.\n", 0.5)

response = input("")

type("{} is a nice name!".format(response), 0.05)
