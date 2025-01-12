import queue

q = queue.LifoQueue()

numbers = [x for x in range(1, 21)]
for number in numbers:
    q.put(number)

while not q.empty():
    print(q.get())