import threading
def function():
    for x in range(500000):
        print("HELLO WORLD!")

if __name__ == "__main__":
    t1 = threading.Thread(target=function)
    t1.start()
    t1.join()
    # t1.join(5) # max time to wait for the thread to finish
    print("THIS IS THE END!")
