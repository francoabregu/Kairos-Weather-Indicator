import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import os

class PantallaPronostico(Gtk.ApplicationWindow):
	def __init__(self):
		super(Gtk.ApplicationWindow, self).__init__(title='Pronóstico')
		self.set_icon_from_file(os.getcwd()+ "/View/Desktop/Icons/icono.svg")
		self.set_name('clima')
		screen = Gdk.Screen.get_default()
		css_provider = Gtk.CssProvider()
		css_provider.load_from_path(os.getcwd() + '/View/Desktop/estilos.css')
		context = Gtk.StyleContext()
		context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
		self.set_border_width(10)
		self.set_position (Gtk.WindowPosition.CENTER)
		self.set_resizable (False)
		box = Gtk.VBox(spacing=10)
		self.add(box)
		self.boxPrincipal = box