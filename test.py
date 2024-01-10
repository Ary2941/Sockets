import threading
import time

def input_thread():
    user_input = input("Digite algo: ")
    # Faça algo com o input, se necessário

input_thread = threading.Thread(target=input_thread)
input_thread.start()

time.sleep(5)

if input_thread.is_alive():
    print("Tempo expirado. Encerrando o programa.")
    import os
    os._exit(0)  # Isso encerrará o programa abruptamente; use com cautela

#Aguarda a thread encerrar (opcional)
#input_thread.join()

print("Thread encerrada.")
