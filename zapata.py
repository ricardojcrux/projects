lista=[]
continuar=True
num=int(input('Número de diccionarios: '))

for i in range(num):
	persona={}
	print(f'Bienvenido al diccionario N°{i+1}\n')
	while True:
		clave=input('¿Que datos quieres introducir?: ')
		valor=input(f'{clave}: ')
		persona[clave] = valor
		print(persona)
		decision = input('¿Quieres añadir mas información (s/n): ')
		if decision == "n":
			print('Gracias por la información')
			lista.append(persona)
			break
		elif decision == 's':
			print('Continuemos')
		else:
			decision = input('Elegir entre si o no (s/n)')	

print(lista)

c=(int(input('Consulta el libro necesario: '))-1)
print(lista[c])

