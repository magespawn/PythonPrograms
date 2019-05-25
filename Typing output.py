import sys
import time

def type(text, delay):
    i = 0
    amount = len(text)
    while amount < i:
        sys.stdout.write( text[ i ])
        sys.stdout.flush()
        i += 1
        time.sleep(delay)

type("What is your name?", 0.05)
response = input("")
type("{} is a very nice name!".format(response), 0.05)
