print("=====ATIVIDADE TIPO DE DADOS EM PYTHON=====")
print()
#1. Inteiro (int)
#Crie uma variável chamada idade que armazene sua idade e mostre o valor dela na tela

idade = 25
print(idade)

#2. Float
#Crie uma variável chamada altura que armazene a sua altura em metros (por exemplo, 1.75) e exiba-a.

altura = 1.82
print(altura)

#3. String
#Crie uma variável chamada nome que armazene o seu nome completo e exiba a frase: Olá, meu nome é
#[nome].

nome = "Matuzalem"
print(f"Olá, meu nome é {nome}.")

#4. Boolean
#Crie uma variável chamada estudando_python que indique (com True ou False) se você está estudando
#Python no momento e mostre seu valor.

estudando_python = True
print(estudando_python)

#5. Lista
#Crie uma lista chamada frutas com três frutas diferentes e exiba a segunda fruta da lista.

frutas = ["maçã", "banana", "uva"]
print(frutas[1])

#6. Tupla
#Crie uma tupla chamada cores com quatro cores diferentes e mostre a primeira cor da tupla.

cores = ("vermelho", "azul", "verde", "amarelo")
print(cores[0])

#7. Dicionário
#Crie um dicionário chamado aluno com as chaves: "nome", "idade" e "nota", preenchendo com valores
#fictícios. Exiba o valor da chave "nota".

aluno = {
 "nome": "Matuzalem",
 "idade": 25,
 "nota": 9.5
}
print(aluno["nota"])

#8. Misturando tipos
#Crie uma lista chamada dados que contenha: um número inteiro, um número float, uma string e um valor
#booleano. Exiba o conteúdo da lista.

dados = [42, 3.14, "Python", False]

print(dados)
