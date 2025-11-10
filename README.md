🐍 Sequência de Fibonacci em Python

Programa simples que gera os n primeiros termos da sequência de Fibonacci.

📘 Descrição

A sequência de Fibonacci é formada pela soma dos dois números anteriores:
0, 1, 1, 2, 3, 5, 8, ...

O usuário informa quantos termos deseja, e o programa exibe a lista correspondente.

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

🚀 Execução

Salve como fibonacci.py

Execute no terminal:

python fibonacci.py


Digite o número de termos desejado.