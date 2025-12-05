print("=====ATIVIDADE LOOPS E FUNÇÃO=====")
print()

#1. Faça um programa que peça números ao usuário até que ele digite 0. Ao final, mostre a soma de todos os números digitados.
soma = 0
numero = int(input("Digite um número (0 para sair): "))
while numero != 0:
    soma += numero
    numero = int(input("Digite um número (0 para sair): "))
print(f"A soma de todos os números é: {soma}\n")

#2. Crie um programa que peça uma senha ao usuário e só termine quando a senha correta "python123" for digitada.
senha = input("Digite a senha: ")
while senha != "python123":
    print("Senha incorreta! Tente novamente.")
    senha = input("Digite a senha: ")
print("Acesso liberado!")

#3. Escreva um programa que mostre a tabuada de um número escolhido pelo usuário, de 1 até 10, usando while.
num = int(input("Digite um número para ver a tabuada: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
print()

#4. Faça um programa que mostre todos os números pares de 1 a 20.
for n in range(2, 21, 2):
    print(n, end=" ")

#5. Escreva um programa que leia 5 números e mostre o maior deles.
maior = float('-inf')
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    if num > maior:
        maior = num
print(f"O maior número digitado foi: {maior}\n")

#6. Crie um programa que percorra uma string digitada pelo usuário e conte quantas vogais ela possui.
texto = input("Digite uma frase: ").lower()
vogais = "aeiou"
contador = 0
for letra in texto:
    if letra in vogais:
        contador += 1
print(f"A frase possui {contador} vogais.\n")

#7. Crie uma função que receba dois números e retorne a soma deles.
def somar(a, b):
    return a + b
print("Soma 7 + 5 =", somar(7, 5))

#8. Crie uma função que receba um número e retorne True se ele for par e False caso contrário.
def par(numero):
    return numero % 2 == 0
print("12 é par?", par(12))  
print("13 é par?", par(13))

#9. Crie uma função que receba uma lista de números e retorne a média deles.
def media_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)
numeros = [10, 20, 30, 40]
print("Média da lista", numeros, "=", media_lista(numeros))

#10. Crie uma função chamada saudacao que receba o nome de uma pessoa como parâmetro e exiba a mensagem: 👉 "Olá, [nome]! Seja bem-vindo(a)!"
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")
saudacao("Matuzalem")
