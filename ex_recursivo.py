'''#1) Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.
def fat(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * fat(N - 1)

numero = 5
resultado = fatorial(numero)
print(f"O fatorial de {numero} é {resultado}.")

#2) Faça uma função recursiva que calcule e retorne o N-ésimo termo da sequência Fibonacci. Alguns números desta sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 10
print(f"O {n}º termo da sequência de Fibonacci é: {fibonacci(n)}")

#3) Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321

def inverter_numero(n, inverso=0):
    if n == 0:
        return inverso
    else:
        return inverter_numero(n // 10, inverso * 10 + n % 10)

numero = 123
resultado = inverter_numero(numero)
print(resultado)  

#4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

def soma_vetor(vetor):
    if not vetor:
        return 0
    else:
        return vetor[0] + soma_vetor(vetor[1:])

vetor = [1, 2, 3, 4, 5]
resultado = soma_vetor(vetor)
print("A soma dos elementos do vetor é:", resultado)

#5) Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N.
def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n-1)

numero = int(input('informe um numero'))
print('a soma é', soma(numero))'''

#6) Crie um programa em Python que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule k. Utilize apenas multiplicações. 
#O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função.

def potencia(k, n):
    if n == 0:
        return 1
    return k * potencia(k, n - 1)

def main():
    k = int(input("Digite um número inteiro positivo k: "))
    n = int(input("Digite um número inteiro positivo n: "))
    
    resultado = potencia(k, n)
    print(f"{k} elevado a {n} é: {resultado}")

if __name__ == "__main__":
    main()

#8) O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y.
# Escreva uma função recursiva mdc em C, que retorna o máximo divisor comum de x e y.
#O mdc de x e y é definido como segue: se y é igual a 0, então mdc(x,y) é x; caso
#contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto.



