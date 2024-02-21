#Feito por Samuel

#entrada

print()
print()
lado_a = input("Informe o tamanho de um lado do triangulo: ")
lado_b = input("Informe o tamanho de outro lado do triangulo: ")
lado_c = input("Informe o tamanho do último lado do triangulo: ")





#saída

if lado_a == lado_b and lado_b == lado_c:
    print()
    print('Este é um triângulo Equilátero!')

elif lado_a == lado_b and lado_b != lado_c:
    print()
    print('Este é um triângulo Isósceles!')
    

elif lado_a == lado_c and lado_a != lado_b:
    print()
    print('Este é um triângulo Isósceles!')

elif lado_c == lado_b and lado_b != lado_a:
    print()
    print('Este é um triângulo Isósceles!')

else:
    print()
    print('Este é um triângulo Escaleno!')
