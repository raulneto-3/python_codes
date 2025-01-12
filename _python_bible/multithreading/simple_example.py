import threading

def function1():
    for x in range(1000):
        print("ONE")

def function2():
    for x in range(1000):
        print("TWO")

if __name__ == "__main__":
    t1 = threading.Thread(target=function1)
    t2 = threading.Thread(target=function2)
    t1.start()
    t2.start()

