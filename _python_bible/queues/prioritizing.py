import queue

q = queue.PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))
q.put((1, 'repeat'))

while not q.empty():
    print(q.get())

while not q.empty():
    print(q.get()[1])