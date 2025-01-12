import threading
import time

# Descrever o problema: Sincronização entre múltiplas threads usando um evento.
# Implementar um exemplo em Python usando a biblioteca threading e Event.
# Criar múltiplas threads que esperam por um evento para continuar a execução.
# Usar um Event para sinalizar quando as threads podem continuar.


# Função que simula uma tarefa que espera por um evento
def wait_for_event(event, thread_id):
    print(f"Thread {thread_id} esperando pelo evento...")
    event.wait()  # Espera pelo evento ser sinalizado
    print(f"Thread {thread_id} detectou o evento e está continuando...")

# Cria o evento
event = threading.Event()

# Cria e inicia múltiplas threads
threads = []
for i in range(5):
    thread = threading.Thread(target=wait_for_event, args=(event, i))
    threads.append(thread)
    thread.start()

# Simula algum processamento antes de sinalizar o evento
time.sleep(2)
print("Sinalizando o evento para todas as threads continuarem...")
event.set()  # Sinaliza o evento

# Aguarda todas as threads terminarem
for thread in threads:
    thread.join()

print("Todas as threads terminaram.")