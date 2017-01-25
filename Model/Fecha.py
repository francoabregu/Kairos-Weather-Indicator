from datetime import datetime
class Fecha:
	def __init__(self):
		fechaActual = datetime.now().strftime('%d-%B-%H:%M-%A')
		componentes = fechaActual.split('-')
		self.dia = componentes[0]
		self.mes = componentes[1]
		self.hora = componentes[2]
		self.diaSemana = componentes[3]

	def formatearFecha(self):
		return self.diaSemana.title() + " " + self.dia + " de " + self.mes.title() + ", " + self.hora

	

