# Chat entre 2 Clientes usando Sockets em Python

Este projeto consiste em duas versões de um programa de chat entre dois clientes utilizando sockets em Python. Uma em TCP e outra em UDP. O programa quimera une as duas versões em uma só.
## Requisitos

- Python 3.11.4

## Execução

### Ligar o cliente

```bash
python quimera.py UDP
```
ou

```bash
python quimera.py TCP
```

- para mandar mensagens basta escrever no terminal, após definir as portas *dos dois clientes*
- exemplo: minha porta: 1010, porta do amigo 1011 se comunicando com 1011 com porta do amigo 1010

## Funcionalidades
- Ambas as versões permitem a comunicação em tempo real entre dois clientes através de sockets.
- basta executar o programa em dois terminais separados para iniciar dois clientes.
- as versões não são compatíveis entre si (quimera.py UDP não deve se comunicar com quimera.py TCP)


## Observações
- É necessário esclarescer se vai ser executado em UDP ou TCP
---

*Este projeto foi desenvolvido por Amaury Junior.
