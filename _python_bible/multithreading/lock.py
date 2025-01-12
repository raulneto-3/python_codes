import threading

# Descrever o problema: Controle de acesso a um recurso compartilhado (por exemplo, um contador) por múltiplas threads.
# Implementar um exemplo em Python usando a biblioteca threading e Lock.
# Criar múltiplas threads que tentam incrementar o contador.
# Usar um Lock para garantir que apenas uma thread possa modificar o contador por vez.


# Recurso compartilhado
class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            local_value = self.value
            local_value += 1
            self.value = local_value

# Função que simula o incremento do contador
def increment_counter(counter, thread_id):
    for _ in range(1000):
        counter.increment()
    print(f"Thread {thread_id} terminou.")

# Cria o contador
counter = Counter()

# Cria e inicia múltiplas threads
threads = []
for i in range(10):
    thread = threading.Thread(target=increment_counter, args=(counter, i))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

print(f"Valor final do contador: {counter.value}")