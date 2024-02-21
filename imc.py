# Programa para calcular IMC
# Desenvolvido por Celso

print("****************************************")
print("*        CALCULADORA DE IMC            *")
print("****************************************")
print()

# CRIAÇÃO DAS VARIÁVEIS
nome = ""
peso = 0
altura = 0.0
imc = 0.0

# ENTRADA DOS DADOS
nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMC
imc = peso / altura ** 2

# SAÍDA DO PROCESSAMENTO
print()
print("*******************************")
print("*          RESULTADO          *")
print("*******************************")
print("*                             *")
print(f"NOME: {nome}")
print(f"PESO: {peso}Kg")
print(f"ALTURA: {altura}m")
print(f"IMC: {imc}")


if imc < 18.5:
    situacao = "Abaixo do Peso"
    print(f'Situação: {situacao}')
    
elif imc >= 18.5 and imc < 25.0:
    situacao = "Peso Normal"
    print(f"Situação: {situacao}")

elif imc >= 25.0 and imc < 29.9:
    situacao = "Acima do Peso"
    print(f"Situação: {situacao}")

elif imc >= 30.0 and imc < 34.9:
    situacao = "Obesidade Grau I"
    print(f"Situação: {situacao}")

elif imc >= 35.0 and imc < 39.9:
    situacao = "Obesidade Grau II"
    print(f"Situação: {situacao}")

else:
    situacao = "Obesidade Grau III ou Mórbida"
    print(f"Situação: {situacao}")
