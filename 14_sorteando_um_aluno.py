import random
n1 = str(input("Digite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
lista = [n1, n2, n3]
escolhido = random.choice(lista)
print(f"O aluno escolhido foi {escolhido}")