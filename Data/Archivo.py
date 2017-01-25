import os

class Archivo:
	def __init__(self, unLugar, unIntervalo):
		self.unLugar = unLugar
		self.unIntervalo = unIntervalo
		self.ubicacion = directorioImagenes = os.getcwd() + '/Data/Datos.txt'

	def crearArchivo(self):
		f = open(self.ubicacion, 'w+')
		f.close()

	def escribirDatos(self):
		with open(self.ubicacion, 'w') as archivo:
			archivo.write("ubicacion=" + self.unLugar + '\n')
			archivo.write("intervalo=" + self.unIntervalo + '\n')

	def leerDato(self, dato):
		with open(self.ubicacion, 'r') as archivo:
			for linea in archivo:
				if dato in linea:
					datos = linea.split('=')
					return datos[1]


	def sacarSaltoDeLinea(self, cadena):
		lista = list(cadena)
		for i in range(0, len(lista)):
			if lista[i] == '\n':
					lista.pop(i)
		return ''.join(lista)

	def obtenerIntervalo(self):
		intervalo = self.sacarSaltoDeLinea(self.leerDato("intervalo"))
		valores = {'1 hora': 1, 
		'3 horas': 3, 
		'6 horas': 6, 
		'12 horas': 12, 
		'24 horas': 24
		}
		return valores[intervalo]

