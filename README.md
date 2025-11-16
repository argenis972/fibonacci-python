🐍 Fibonacci em Python

Gerador simples da sequência de Fibonacci, desenvolvido em Python, ideal para prática de lógica de programação e estruturas básicas.

📘 Descrição

A sequência de Fibonacci é formada pela soma dos dois números anteriores:

0, 1, 1, 2, 3, 5, 8, 13, ...

Este programa solicita ao usuário a quantidade de termos desejados e exibe a sequência correspondente.

🧠 Conceitos praticados

Funções em Python

Estruturas de repetição (for)

Manipulação de listas

Entrada e saída de dados

Lógica matemática básica

💻 Código
def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

num = int(input("Digite quantos termos da sequência de Fibonacci você quer: "))
print(f"Os primeiros {num} termos são: {fibonacci(num)}")

🚀 Como executar

Salve o arquivo como fibonacci.py

Execute no terminal:

python fibonacci.py


Informe o número de termos desejado quando solicitado.

📂 Estrutura do projeto
fibonacci-python/
│── fibonacci.py
│── README.md

📈 Possíveis melhorias (opcionais)

Criar interface web simples com HTML + JS

Permitir salvar a sequência em arquivo .txt

Implementar testes automatizados com pytest

Tratar erros de entrada (valores negativos ou não numéricos)