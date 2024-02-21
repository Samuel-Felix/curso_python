#Programa feito por Samuel

#Entrada

print()
print('************************')
print('Calculando a media final')
print('************************')
print()
nome = input('Informe seu Nome: ')
nota_1 = float(input('Informe a Nota do 1° Bimestre: '))
nota_2 = float(input('Informe a Nota do 2° Bimestre: '))
nota_3 = float(input('Informe a Nota do 3° Bimestre: '))
nota_4 = float(input('Informe a Nota do 4° Bimestre: '))
media = float(nota_1 + nota_2 + nota_3 + nota_4)
media_final = (media / 4)


#Saída
if media_final < 5:
    print(f'{nome} sua media final é: {media_final}. Você não foi aprovado')
    
elif media_final >= 7:
    print(f'{nome} sua media final é: {media_final}. Parabéns você foi aprovado')

else:
    print(f'{nome} sua media final é: {media_final}. Você está de recuperação')
