from typing import Tuple

escala_imc = {
  'amp': 'Muito abaixo do peso',
  'ap': 'Abaixo do peso',
  'pi': 'Peso ideal',
  'ac': 'Acima do peso',
  'o1': 'Obesidade 1',
  'o2': 'Obesidade 2',
  'o3': 'Obesidade 3'
}

def calcular_imc(peso_kg: float, altura_m: float)-> Tuple[float, str] :
  imc = peso_kg / altura_m ** 2

  if imc < 17:
    situacao = 'amp'
  elif imc <= 18.5:
    situacao = 'ap'
  elif imc <= 25:
    situacao = 'pi'
  elif imc <= 30:
    situacao = 'ac'
  elif imc <= 35:
    situacao = 'o1'
  elif imc <= 40:
    situacao = 'o2'
  else:
    situacao = 'o3'

  saida = (imc, situacao) 
  return saida

def main() :
  try:
    peso = input('Qual é seu peso atual(kg): ')
    peso = float(peso)
    altura = float(input('E a sua altura(m): '))

  except ValueError: 
    print('Valor inválido')
    return

  resultado = calcular_imc(peso, altura)
  (imc, referencia) = resultado

  situacao = escala_imc[referencia]

  print('O seu imc é igual a:', imc)
  print('A sua situacao é:', situacao)

if __name__ == "__main__":
  main()