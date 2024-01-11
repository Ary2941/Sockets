# Chat entre 2 Clientes usando Sockets em Python

Este projeto consiste em duas versões de um programa de chat entre dois clientes utilizando sockets em Python. O projeto oferece uma versão com interface gráfica usando a biblioteca PySimpleGUI (opcional) e uma versão de console. Ambas as versões são equivalentes em funcionalidade.

## Requisitos

- Python 3.11.4
- PySimpleGUI (opcional, apenas para a versão com interface gráfica)

## Instalação de Dependências (Apenas para a versão com interface gráfica)

```bash
pip install PySimpleGUI
```

## Execução

### Versão com Interface Gráfica

```bash
python client+.py {coloque aqui o endereço localhost}
```

### Versão de Console

```bash
python client.py {coloque aqui o endereço localhost}
```

## Funcionalidades

- Ambas as versões permitem a comunicação em tempo real entre dois clientes através de sockets.
- Na versão de console, a frase `!quit` encerra ambos os programas, na da interface o botão x encerra ambos os programas e em ambas as versões crtl+C encerra ambos os programas.
- Para a versão com interface gráfica, basta executar o programa duas vezes para iniciar dois clientes.

## Observações

- A biblioteca PySimpleGUI é opcional e pode ser instalada apenas se a versão com interface gráfica for desejada.
- Ambas as versões do programa são equivalentes em funcionalidade, proporcionando uma experiência de chat entre dois clientes.

---

*Este projeto foi desenvolvido por Amaury Junior.*