#1.Faça um programa que leia um número inteiro maior que zero e informe se é par ou ímpar.

numero_usuario = int(input("Digite o número: "))
resultado = "O número digitado é impar"


if(numero_usuario > 0):
  if(numero_usuario % 2 == 0):
    resultado = "O número       digitado é par"
    print("")
    print("")
    print(resultado)
    

  else:
    print(resultado)