from Model.AdaptadorSistemaExterno import AdaptadorSistemaExterno
from Model.Fecha import Fecha
from Model.Clima import Clima

class Pronostico:
	def __init__(self,unLugar):
		if unLugar == None:
			self.sinDatos()
		else:
			adapter = AdaptadorSistemaExterno(unLugar)
			climaEncontrado = adapter.obtenerClima()
			self.lugar = unLugar
			self.clima = climaEncontrado
			self.fecha = Fecha()
			self.climas = adapter.climasOtrosDias

	def sinDatos(self):
		self.lugar = "No ingresado"
		self.clima = Clima('??', '??', '??', '??', '??', '??', '??', '??', '??', '??')
		self.fecha = Fecha()
		self.climas = []

