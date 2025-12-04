print("=====ATIVIDADE ESTRUTURAS CONDICIONAIS (if, elif, else)=====")
print()
##1. Peça um número e diga se ele é positivo.
num = int(input("Digite um numero: "))
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")

##2. Peça a idade e informe se é maior de idade ou menor de idade.
idade = int(input("Digite sua idade:"))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
    
##3. Peça uma nota (0 a 10) e informe: Aprovado (>= 7), Recuperação (5 a 6.9) ou Reprovado (< 5).
nota = float(input("Digite a nota: "))
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
    
##4. Peça um número e verifique: se é positivo, se é par e se é múltiplo de 5.
num = int(input("Digite um numero: "))
if num > 0:
    print("Positivo")
if num % 2 == 0:
    print("Par")
if num % 5 == 0:
    print("Multiplo de 5")

##5. Peça a cor do semáforo (verde, amarelo, vermelho) e exiba a ação correspondente.
cor = input("Digite a cor do semaforo: ")
if cor == "verde":
    print("Pode seguir")
elif cor == "amarelo":
    print("Atenção")
elif cor == "vermelho":
    print("Pare")
else:
    print("Cor invalida")
    
##6. Peça a idade e, se for maior de idade, pergunte se tem habilitação (sim/não) e diga se pode dirigir.
idade = int(input("Digite sua idade: "))
if idade >=18:
    habilitação = input("Tem habilitação? (Sim/Não): ")
    if habilitação == "sim":
        print("Pode dirigir")
    elif habilitação == "não":
        print("Não pode dirigir")
    elif habilitação != "sim" and "não":
        print("não esperava isso")

    
##7. Peça um número e mostre 'Par' ou 'Ímpar' usando apenas uma linha de código.
num = int(input("Digite um numero: "))
print(("par" if num % 2 == 0 else "impar"))

##8.Peça um número e diga se ele está entre 10 e 20 (inclusive).
num = int(input("Digite um numero: "))
if 10 <= num <= 20:
    print("Esta entre 10 e 20")
else:
    print("Não está entre 10 e 20")
    
##9.Peça três números e diga qual é o maior.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

print(f"O maior número é: {maior}")

##10.Peça usuário e senha. Se forem 'admin' e '1234', exiba 'Acesso permitido', caso contrário 'Acesso negado'
usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == "admin" and senha == "1234":
    print("Acesso permitido")
else:
    print("Acesso negado")
