import threading
import queue
import math

q = queue.Queue()
threads = []

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print(f'Working on {item}')
        q.task_done()

for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

zahlen = [x for x in range(1, 21)]
for item in zahlen:
    q.put(item)

q.join()

for i in range(5):
    q.put(None)
    