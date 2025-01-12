import threading
import time

x = 8192

def halve():
    global x
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("HALF DONE!")

def double():
    global x
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("DOUBLE DONE!")

if __name__ == "__main__":
    t1 = threading.Thread(target=halve)
    t2 = threading.Thread(target=double)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

