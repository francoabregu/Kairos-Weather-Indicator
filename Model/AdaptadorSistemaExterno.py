from urllib.request import urlopen
import sys
import json
import urllib
from Model.Clima import Clima
from Model.ClimaResumido import ClimaResumido

#http://api.openweathermap.org/data/2.5/forecast/city?q=London&APPID=8dadf00064ee857ba76905b51959da02
#Si el lugar tiene 2 palabras hay q agregar un%20 por ejemplo Buenos Aires quedaria: Buenos%20Aires

class AdaptadorSistemaExterno:
	def __init__(self,lugar):
		self.lugar = lugar
		self.yahooApiUrl = 'https://query.yahooapis.com/v1/public/yql'
		self.climasOtrosDias = []

	def obtenerInformacion(self):
		print("Obteniendo datos de la ciudad " +self.lugar + "...")
		try:
			parametroQuery = '?q='
			parametroJson = '&format=json'
			# la parte de and u='c' en el where es para que devuelva en celcius
			yqlQuery = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=' + "\"" + self.lugar + "\")"
			url = self.yahooApiUrl + parametroQuery + self.adaptarEspacios(yqlQuery) + parametroJson
			response = urlopen(url, None, 1000)
			jsonCiudad = response.read().decode('utf-8')
			return json.loads(jsonCiudad)
		except urllib.error.URLError:
			self.imprimirError("No se pudo conectar con el servidor")
			sys.exit()
			
	def obtenerClima(self):
		arrayCiudad = self.obtenerInformacion()
		clima = "---"
		humedad = "---"
		presion = "---"
		amanecer = "---"
		anochecer = "---"
		viento = "---"
		sensacionTermica = "---"
		temperatura = "??"
		temperaturaMaxima = "---"
		temperaturaMinima = "---"
		descripcionClima = "Sin datos"
		visibilidad = "---"
		if arrayCiudad['query']['results'] == None:
			self.imprimirError("No se encontraron datos sobre este lugar, asegurese de haber escrito bien el nombre o inténtelo mas tarde.")
		else:
			clima = arrayCiudad['query']['results']['channel']
			humedad = clima['atmosphere']['humidity']
			presion = clima['atmosphere']['pressure']
			visibilidad = "%.2f" %float(clima['atmosphere']['visibility'])
			amanecer = self.corregirHora(clima['astronomy']['sunrise'])
			anochecer = self.corregirHora(clima['astronomy']['sunset'])
			viento = clima['wind']['speed']
			sensacionTermica = self.farenheitACelcius(clima['wind']['chill'])
			temperatura = self.farenheitACelcius(clima['item']['condition']['temp'])
			temperaturaMaxima = self.farenheitACelcius(clima['item']['forecast'][0]['high'])
			temperaturaMinima = self.farenheitACelcius(clima['item']['forecast'][0]['low'])
			descripcionClima = self.traducirClima(clima['item']['condition']['text'])
			self.obtenerPronosticoExtendido(clima['item']['forecast'])
			self.imprimirExito("Datos obtenidos con exito!")
		return Clima(descripcionClima,	temperatura, sensacionTermica, temperaturaMaxima, temperaturaMinima, presion,	humedad, viento, amanecer, anochecer, visibilidad)
	
	def adaptarEspacios(self,unLugar):
		if ' ' in unLugar:
			lista = list(unLugar)
			for i in range(0, len(lista)):
				if lista[i] == ' ':
					lista[i] = '%20'
			return ''.join(lista)
		else:
			return unLugar

	def traducirClima(self, unClima):
		tiposClima = {
		'Partly Cloudy':'Parcialmente nublado', 
		'Mostly Cloudy': 'Parcialmente nublado',
		'Cloudy': 'Nublado',
		'Windy': 'Ventoso',
		'Breezy': 'Ventoso',
		'Sunny': 'Soleado',
		'Mostly Sunny': 'Mayormente soleado',
		'Scattered Thunderstorms': 'Tormentas eléctricas dispersas',
		'Thunderstorms': 'Tormentas eléctricas',
		'Showers' : 'Tormentas',
		'Rain': 'Lluvia',
		'Clear': 'Despejado'
		}
		if tiposClima.get(unClima) == None:
			return unClima
		else:
			return tiposClima[unClima]

	def traducirDia(self,unDia):
		dias = {
		'Mon': 'Lunes',
		'Tue': 'Martes',
		'Wed': 'Miércoles',
		'Thu': 'Jueves',
		'Fri': 'Viernes',
		'Sat': 'Sábado',
		'Sun': 'Domingo'
		}
		return dias[unDia]

	def obtenerPronosticoExtendido(self, unArray):
		for i in [1, 2, 3, 4]:
			dia = unArray[i]
			clima = ClimaResumido(self.traducirClima(dia["text"]), self.traducirDia(dia['day']), self.farenheitACelcius(dia['high']), self.farenheitACelcius(dia['low']))
			self.climasOtrosDias.append(clima)
	
	def farenheitACelcius(self, unaTemp):
		return str(int((int(unaTemp)- 32) * 5/9))

	def imprimirError(self,unError):
		print('\033[91mError: ' + unError + '\033[0m')

	def imprimirExito(self,mensaje):
		print('\033[32m' + mensaje + '\033[0m')

	def corregirHora(self, unaHora):
		componentes = unaHora.split(' ')
		am_o_pm = componentes[1]
		partesHora = componentes[0].split(':')
		hora = partesHora[0]
		minutos = partesHora[1]
		if len(minutos) < 2:
			return hora + ":0" + minutos + " " + am_o_pm
		else:
			return unaHora