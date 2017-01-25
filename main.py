#! /usr/bin/env python3
from Controllers.IndicadorController import IndicadorController
from Model.Pronostico import Pronostico
from Data.Archivo import Archivo
import gi, os, signal


gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
gi.require_version('Notify', '0.7')
from gi.repository import Notify as notify, GObject
print("Servicio de clima iniciado")
try:
	file = open(os.getcwd() + '/Data/Datos.txt','r')
	file.close()
	archivo = Archivo(None,None)
	ubicacion = archivo.leerDato("ubicacion")
	intervalo = archivo.obtenerIntervalo()
	unPronostico = Pronostico(archivo.sacarSaltoDeLinea(ubicacion))
	IndicadorController(unPronostico,intervalo)
	GObject.threads_init()
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	Gtk.main()
	
except IOError:
	notify.init("Clima App")
	notify.Notification.new("Clima App","<b> No se ingreso ningún dato, por favor ingreselos en la opción \"Configuracion\" del incicador </b>").show()
	controllerIndicador = IndicadorController(Pronostico(None), None)
	signal.signal(signal.SIGINT, signal.SIG_DFL)
	Gtk.main()
