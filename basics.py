print('Hello World')

# input('Username: ')

if 2 + 2 == 4:
  print('Answer is 4')
elif 2 + 2 == 5:
  print('Noooo')
else:
  print('Math is  hard')


for x in range(1, 5):
  print('Number: ', x)

nomes = [ 'Fernando', 'Francisco' ]
nomes.append('Fabricio')
nomes2 = []

nomes2.append('Fernando')
nomes2.append('Francisco')
nomes2.append('Fabricio')

nomes3 = nomes2
nomes.clear()
nomes2.append('Thiago')

print(nomes)
print(nomes2)
print(nomes3)