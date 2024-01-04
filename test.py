import threading
import time

def minha_funcao(nome):
    for _ in range(5):
        time.sleep(1)
        print(f"Olá, {nome}!")

# Criar uma thread
thread1 = threading.Thread(target=minha_funcao, args=("Thread 1",))

# Iniciar a thread
thread1.start()

# Fazer algo na thread principal
for _ in range(5):
    time.sleep(1)
    print("Trabalhando na thread principal...")

# Aguardar a thread terminar antes de encerrar o programa principal
thread1.join()

print("Programa encerrado.")