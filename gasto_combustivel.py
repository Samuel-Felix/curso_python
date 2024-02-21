#Programa feito por Samuel 07/02/2024

#Entrada
print('*****************************************')
print('*****   CONSUMO DE COMBUSTÍVEL     ******')
print('*****************************************')
print()
veiculo = input('Informe o modelo do veículo: ')
autonomia = int(input('Informe a autonomia do carro: '))
distancia = float(input('Distancia da viagem: '))
preco = float(input('Preço do Combustível: '))

quantidade = float(distancia / autonomia)
total = float(quantidade * preco)

#Saída

print()
print(f'Modelo do veículo: {veiculo}')
print(f'Autonomia do veículo: {autonomia} Km/1')
print(f'Distancia percorrida: {distancia}Km')
print(f'Valor do Combustível: {preco}')
print()
print(f'Quantidade de combutivel utilizado: {quantidade}')
print(f'Total gasto com a viagem: R${total}')
