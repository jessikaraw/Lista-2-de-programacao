#2. Escreva um programa que leia um número e informe se ele é divisível por 10, por 5 ou por 2, ou se não é divisível por nenhum deles.

Numero_tipo = int(0)
divisor_dez = int(0)
divisor_cinco = int(0)
divisor_dois = int(0)

Numero_tipo = int(input("Digite um número: "))

#manipulação
if(Numero_tipo % 10 == 0):
  print("número é dividido por dez")

if(Numero_tipo % 5 == 0):
  print("número é dividido por cinco")

if(Numero_tipo % 2 == 0):
  print("número é dividido por dois")