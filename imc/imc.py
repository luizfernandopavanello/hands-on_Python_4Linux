

def main() :
  try:
    peso = input('Qual é seu peso atual(kg): ')
    peso = float(peso)
    altura = float(input('E a sua altura(m): '))

  except ValueError: 
    print('Valor inválido')
    return

  imc = peso / altura ** 2
  
  if imc < 17:
    situacao = 'Muito abaixo do peso'
  
  elif imc <= 18.5:
    situacao = 'Abaixo do peso'

  elif imc <= 25:
    situacao = 'Peso ideal'
  
  elif imc <= 30:
    situacao = 'Acima do peso'
  
  elif imc <= 35:
    situacao = 'Obesidade 1'
  
  elif imc <= 40:
    situacao = 'Obesidade 2'

  else:
    situacao = 'Obesidade 3'

  print('O seu imc é igual a:', imc)
  print('A sua situacao é:', situacao)

main()