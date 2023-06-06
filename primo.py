a=int(input('Escriba un número: '))
for x in range(2,a):
  if a%x == 0:
    print('El número no es primo')
    break
else:
  print('El número es primo')