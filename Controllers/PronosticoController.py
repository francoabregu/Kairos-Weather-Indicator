from Controllers.ImagenController import ImagenController
from Controllers.TipoImagen import TipoImagen
from View.Desktop.PantallaPronostico import PantallaPronostico
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class PronosticoController():
	
	def __init__(self, unPronostico):
		self.pronostico = unPronostico
		self.pantalla = PantallaPronostico()
		elementos = self.getListBoxes()
		for i in range(len(elementos)):
			self.pantalla.boxPrincipal.pack_start(elementos[i], True, True, 0)

	def getListBoxes(self):
		listaDeListBox = []
		listaDeListBox.append(self.listboxDatosPrincipales())
		if len(self.pronostico.climas) > 0:
			listaDeListBox.append(self.listboxPronosticoExtendido())
		return listaDeListBox

	def rutaImagen(self, descripcionClima):
		imagenController = ImagenController()
		return imagenController.obtenerImagen(descripcionClima, TipoImagen.desktop)

	def listboxDatosPrincipales(self):
		listbox = Gtk.ListBox()
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		listbox.set_name('listbox')
		row = Gtk.ListBoxRow()
		vbox = Gtk.VBox()
		vbox.set_margin_top(10) 
		vbox.set_margin_bottom(10)
		vbox.set_margin_left(10) 
		vbox.set_margin_right(10)
		row.add(vbox)
		titulo = Gtk.Label(self.pronostico.lugar, xalign=0)
		titulo.set_name('titulo')
		fechaYHora = Gtk.Label(self.pronostico.fecha.formatearFecha(), xalign=0)
		descripcionClima = Gtk.Label(self.pronostico.clima.descripcionClima, xalign=0)
		rutaIcono = self.rutaImagen(self.pronostico.clima.descripcionClima)
		imagen = Gtk.Image(xalign=0)
		imagen.set_from_file(rutaIcono)
		temperatura = Gtk.Label(self.pronostico.clima.temperatura + "º", xalign=0)
		temperatura.set_name('temperatura')
		maxima = Gtk.Label("Max: " + self.pronostico.clima.temperaturaMaxima + "º", xalign=0)
		maxima.set_name('tempMax')
		minima = Gtk.Label("Min: " + self.pronostico.clima.temperaturaMinima + "º", xalign=0)
		minima.set_name('tempMin')
		humedad = Gtk.Label("Humedad: " + self.pronostico.clima.humedad +" %", xalign=0)
		presion = Gtk.Label("Presion: " + self.pronostico.clima.presion + " mb", xalign=0)
		viento = Gtk.Label("Viento: " + self.pronostico.clima.viento + " km/h", xalign=0)
		amanecer = Gtk.Label("Amanecer: " + self.pronostico.clima.amanecer, xalign=0)
		anochecer = Gtk.Label("Anochecer: " + self.pronostico.clima.anochecer, xalign=0)
		visibilidad = Gtk.Label("Visibilidad: " + self.pronostico.clima.visibilidad + " km", xalign=0)
		vbox.pack_start(titulo, True, True, 0)
		vbox.pack_start(fechaYHora, True, True, 0)
		vbox.pack_start(descripcionClima, True, True, 0)
		hbox = Gtk.HBox()
		vbox.pack_start(hbox, True, True, 0)
		datosClima = Gtk.VBox()
		datosClima.pack_start(humedad, True, True, 0)
		datosClima.pack_start(presion, True, True, 0)
		datosClima.pack_start(viento, True, True, 0)
		datosClima.pack_start(amanecer, True, True, 0)
		datosClima.pack_start(anochecer, True, True, 0)
		datosClima.pack_start(visibilidad, True, True, 0)
		vBoxDerecha = Gtk.VBox()
		hboxIcono = Gtk.HBox()
		hboxTemp = Gtk.HBox()
		hboxTemp.pack_start(maxima, True, True, 0)
		hboxTemp.pack_start(minima, True, True, 0)
		hboxIcono.pack_start(imagen, True, True, 0)
		hboxIcono.pack_start(temperatura, True, True, 3)
		vBoxDerecha.pack_start(hboxIcono, True, True, 0)
		vBoxDerecha.pack_start(hboxTemp, True, True, 0)
		hbox.pack_start(vBoxDerecha, True, True, 0)
		hbox.pack_start(datosClima, True, True, 40)
		listbox.add(row)
		return listbox

	def listboxDatosAdicionales(self):
		listbox = Gtk.ListBox()
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		row = Gtk.ListBoxRow()
		vbox = Gtk.VBox(spacing=3)
		vbox.set_margin_top(10) 
		vbox.set_margin_bottom(10)
		vbox.set_margin_left(10) 
		row.add(vbox)
		humedad = Gtk.Label("Humedad: " + self.pronostico.clima.humedad +" %", xalign=0)
		presion = Gtk.Label("Presion: " + self.pronostico.clima.presion + " mb", xalign=0)
		viento = Gtk.Label("Viento: " + self.pronostico.clima.viento + " km/h", xalign=0)
		amanecer = Gtk.Label("Amanecer: " + self.pronostico.clima.amanecer, xalign=0)
		anochecer = Gtk.Label("Anochecer: " + self.pronostico.clima.anochecer, xalign=0)
		vbox.pack_start(humedad, True, True, 0)
		vbox.pack_start(presion, True, True, 0)
		vbox.pack_start(viento, True, True, 0)
		vbox.pack_start(amanecer, True, True, 0)
		vbox.pack_start(anochecer, True, True, 0)
		listbox.add(row)
		return listbox

	def listboxPronosticoExtendido(self):
		listbox = Gtk.ListBox()
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		listbox.set_name('listbox')
		row = Gtk.ListBoxRow()
		hbox = Gtk.HBox()
		hbox.set_margin_top(10) 
		hbox.set_margin_bottom(10)
		hbox.set_margin_left(10)
		hbox.set_margin_right(10) 
		row.add(hbox)
		for i in range(len(self.pronostico.climas)):
			vbox1 = Gtk.VBox(spacing=4)
			dia = Gtk.Label(self.pronostico.climas[i].dia)
			dia.set_name('titulo')
			tempMaxima =Gtk.Label("Max: " + self.pronostico.climas[i].maxTemp + "º")
			tempMaxima.set_name('tempMax')
			tempMinima = Gtk.Label("Min: " + self.pronostico.climas[i].minTemp + "º")
			tempMinima.set_name('tempMin')
			imagen = Gtk.Image()
			rutaIcono = self.rutaImagen(self.pronostico.climas[i].descripcion)
			imagen.set_from_file(rutaIcono)
			vbox1.pack_start(dia, True, True, 0)
			vbox1.pack_start(imagen, True, True, 0)
			vbox1.pack_start(tempMaxima, True, True, 0)
			vbox1.pack_start(tempMinima, True, True, 0)
			hbox.pack_start(vbox1, True, True, 0)
		listbox.add(row)
		return listbox