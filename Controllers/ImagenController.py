from Controllers.TipoImagen import TipoImagen
import os
class ImagenController():
	
	def __init__(self):
		self.rutaImagenesDesktop = "/View/Desktop/Icons/"
		self.rutaImagenesPanel = "/View/Panel/Icons/"
		self.imagenesDesktop = {'Soleado': 'Soleado.png',
		'Parcialmente nublado':'Parcialmente_nublado.png',
		'Mayormente soleado':'Parcialmente_nublado.png',
		'Ventoso': 'Ventoso.png',
		'Tormentas eléctricas dispersas': 'Tormenta_electrica.png',
		'Nublado': 'Nublado.png',
		'Tormentas eléctricas' : 'Tormenta_electrica.png',
		'Tormentas' : 'Tormenta.png',
		'Lluvia': 'Tormenta.png',
		'Despejado': 'Soleado.png',
		'Desconocido': 'desconocido.png'
		}
		self.imagenesPanel ={'Parcialmente nublado':'parcialmente_nublado.png',
		'Nublado': 'nublado.png',
		'Ventoso': 'ventoso.png',
		'Soleado': 'soleado.png',
		'Mayormente soleado': 'mayormente_soleado.png',
		'Tormentas eléctricas dispersas': 'tormenta_electrica.png',
		'Tormentas eléctricas' : 'tormenta_electrica.png',
		'Tormentas' : 'tormenta.png',
		'Lluvia': 'tormenta.png',
		'Despejado': 'soleado.png',
		'Desconocido': 'no_disponible.png'
		}

	def obtenerImagen(self, unClima, unTipo):
		directorioImagenes = os.getcwd()
		imagenes = {}
		if unTipo == TipoImagen.desktop:
			directorioImagenes = directorioImagenes + self.rutaImagenesDesktop
			imagenes = self.imagenesDesktop
		elif unTipo == TipoImagen.panel:
			directorioImagenes = directorioImagenes + self.rutaImagenesPanel
			imagenes = self.imagenesPanel
		imagen = imagenes.get(unClima)
		if imagen == None:
			return directorioImagenes + imagenes['Desconocido'] 
		else:
			return directorioImagenes + imagen