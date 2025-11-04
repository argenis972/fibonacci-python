# Secuência de fibonacci em Python
def fibonacci(n):
    a , b = 0 , 1 # Inicializa os primeiros números a = 0 , b = 1
    
    sequencia = [] # Lista vazia para armazenar a sequência
    for _ in range(n):
        sequencia.append(a) # Adicionando numéro atual à sequência

        a, b = b, a + b # 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8...
    return sequencia

# pidindo ao usuário quantos termos ele quer na sequência
num = int(input("Digite quantos termos da sequência de Fibonacci você quer: "))


resultado = fibonacci(num)
print(f"Os primeiros {num} termos da sequência de Fibonacci são: {resultado}")
# retornando a sequência como uma lista [0, 1, 1, 2, 3, 5, 8, ...]

