import threading
import time

path = "F:/Projects/python_codes/python_bible/multithreading/text.txt"
text = ""

def read_file():
    global path, text
    while True:
        with open(path, "r") as file:
            text = file.read()
        time.sleep(3)

def printloop():
    global text
    for x in range(30):
        print(text)
        time.sleep(1)

t1 = threading.Thread(target=read_file)
t2 = threading.Thread(target=printloop)
t1.start()
t2.start()