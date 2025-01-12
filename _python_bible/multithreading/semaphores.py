import threading
import time
import random

# Descrever o problema: Controle de acesso a um recurso compartilhado (por exemplo, um banco de dados) por múltiplas threads.
# Implementar um exemplo em Python usando a biblioteca threading e Semaphore.
# Criar múltiplas threads que tentam acessar o recurso compartilhado.
# Usar um Semaphore para limitar o número de threads que podem acessar o recurso ao mesmo tempo.


# Recurso compartilhado
class Database:
    def __init__(self):
        self.data = 0

    def read(self):
        print(f"Reading data: {self.data}")

    def write(self, value):
        print(f"Writing data: {value}")
        self.data = value

# Função que simula o acesso ao banco de dados
def access_database(semaphore, db, thread_id):
    print(f"Thread {thread_id} tentando acessar o banco de dados...")
    with semaphore:
        print(f"Thread {thread_id} acessou o banco de dados.")
        db.read()
        time.sleep(random.uniform(0.1, 1.0))  # Simula tempo de leitura/escrita
        db.write(thread_id)
        print(f"Thread {thread_id} liberou o banco de dados.")
    print(f"Thread {thread_id} terminou.")

# Número máximo de threads que podem acessar o banco de dados simultaneamente
MAX_THREADS = 3

# Cria o semáforo
semaphore = threading.Semaphore(MAX_THREADS)

# Cria o banco de dados
db = Database()

# Cria e inicia múltiplas threads
threads = []
for i in range(10):
    thread = threading.Thread(target=access_database, args=(semaphore, db, i))
    threads.append(thread)
    thread.start()

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

print("Todas as threads terminaram.")