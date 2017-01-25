from Data.Archivo import Archivo
import os, gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
gi.require_version('Notify', '0.7')
from gi.repository import Notify as notify


class PantallaConfiguracion(Gtk.ApplicationWindow):

	
	def guardarDatos(self,source):
		nombreLugar = self.lugar.get_text()
		intervalo = self.intervalo
		archivo = Archivo(nombreLugar,intervalo)
		archivo.crearArchivo()
		archivo.escribirDatos()
		notify.init("Clima App")
		notify.Notification.new("Clima App","<b> Datos actualizados correctamente, reinicie la aplicación para ver los cambios. </b>").show()
		self.destroy()


	def __init__(self,  unLugar, unIntervalo):
		super(Gtk.ApplicationWindow, self).__init__(title='Configuracion')
		self.set_icon_from_file(os.getcwd()+ "/View/Desktop/Icons/icono.svg")
		self.set_resizable (False)
		self.set_name('clima')
		screen = Gdk.Screen.get_default()
		css_provider = Gtk.CssProvider()
		css_provider.load_from_path(os.getcwd() + '/View/Desktop/estilos.css')
		context = Gtk.StyleContext()
		context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
		self.set_border_width(10)
		self.set_position (Gtk.WindowPosition.CENTER)
		# box principal
		boxPrincipal = Gtk.VBox(spacing=6)
		self.add(boxPrincipal)
		listbox = Gtk.ListBox()
		listbox.set_name('listbox')
		listbox.set_selection_mode(Gtk.SelectionMode.NONE)
		boxPrincipal.pack_start(listbox, True, True, 0)
		row = Gtk.ListBoxRow()
		hbox = Gtk.HBox(spacing=30)
		hbox.set_margin_top(10) 
		hbox.set_margin_bottom(10)
		hbox.set_margin_left(10) 
		hbox.set_margin_right(10)
		row.add(hbox)
		vbox = Gtk.VBox(spacing=10)
		hbox.pack_start(vbox, True, True, 0)
		labelText = Gtk.Label("Ingrese una ciudad", xalign=0)
		self.lugar = Gtk.Entry()
		self.lugar.set_size_request(400,10)
		self.lugar.get_buffer().set_max_length(100);
		self.lugar.set_text(unLugar)
		labelCombo = Gtk.Label("Intervalo de actualización", xalign=0)
		intervaloActualizacion = self.generarComboActualizacion(unIntervalo)
		vbox.pack_start(labelText, True, True, 0)
		vbox.pack_start(self.lugar, True, True, 0)
		vbox.pack_start(labelCombo, True, False, 0)
		vbox.pack_start(intervaloActualizacion, False, False, True)
		hboxBotones = Gtk.HBox(spacing=10)
		botonAceptar = Gtk.Button(label="Aceptar")
		botonAceptar.connect("clicked", self.guardarDatos)
		botonCancelar = Gtk.Button(label="Cancelar")
		botonCancelar.connect("clicked", self.cancelar)
		hboxBotones.pack_start(botonAceptar, True, True, 0)
		hboxBotones.pack_start(botonCancelar, True, True, 0)
		vbox.pack_start(hboxBotones, True, True, 10)
		listbox.add(row)

	def generarComboActualizacion(self, unIntervalo):
		intervalos = Gtk.ListStore(str)
		horas = ["1 hora", "3 horas", "6 horas", "12 horas", "24 horas"]
		for hora in horas:
			intervalos.append([hora])
		combo = Gtk.ComboBox.new_with_model(intervalos)
		combo.connect("changed", self.obtenerIntervalo)
		renderer_text = Gtk.CellRendererText()
		combo.pack_start(renderer_text, True)
		combo.add_attribute(renderer_text, "text", 0)
		elemento = ""
		if unIntervalo > 1:
			elemento = str(unIntervalo) + " horas"
		else:
			elemento = str(unIntervalo) + " hora"
		combo.set_active(horas.index(elemento))
		return combo

	def obtenerIntervalo(self, combo):
		tree_iter = combo.get_active_iter()
		if tree_iter != None:
			model = combo.get_model()
			seleccionado = model[tree_iter][0]
			self.intervalo = seleccionado

	def cancelar(self,source):
		self.destroy()