from Model.Pronostico import Pronostico
from Controllers.ImagenController import ImagenController
from Controllers.TipoImagen import TipoImagen
from Controllers.PronosticoController import PronosticoController
from View.Desktop.PantallaConfiguracion import PantallaConfiguracion
import signal
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator, GObject, Notify as notify
import time
from threading import Thread

class IndicadorController():
    def __init__(self, pronostico,intervalo):
        self.intervalo = intervalo
        self.pronostico = pronostico
        self.app = 'Clima App'
        self.indicador =  appindicator.Indicator.new(
            self.app, 
            self.seleccionarIcono(self.pronostico.clima.descripcionClima), 
            appindicator.IndicatorCategory.OTHER)
        self.indicador.set_status(appindicator.IndicatorStatus.ACTIVE)       
        self.indicador.set_menu(self.crearMenu())
        self.indicador.set_label(self.pronostico.clima.temperatura + " ºC", self.app)
        self.update = Thread(target=self.actualizarIndicador)
        self.update.setDaemon(True)
        self.update.start()

    def crearMenu(self):
        menu = gtk.Menu()
        clima = self.pronostico.clima
        lugar = gtk.MenuItem(self.pronostico.lugar)
        menu.append(lugar)
        descripcion = gtk.MenuItem(clima.descripcionClima)
        menu.append(descripcion)
        if clima.temperatura == "??":
            reintentar = gtk.MenuItem('Reintentar')
            reintentar.connect('activate', self.modificarIndicador)
            menu.append(reintentar)
        temperatura = gtk.MenuItem('Temperatura: ' + clima.temperatura + ' ºC')
        menu.append(temperatura)
        humedad = gtk.MenuItem('Humedad: ' + clima.humedad + ' %')
        menu.append(humedad)
        viento = gtk.MenuItem('Viento: ' + clima.viento + ' km/h')
        menu.append(viento)
        verMas = gtk.MenuItem('Ver mas')
        verMas.connect('activate', self.verMas)
        menu.append(verMas)
        configuracion = gtk.MenuItem('Configuracion')
        configuracion.connect('activate', self.configuracion)
        menu.append(configuracion)
        salir = gtk.MenuItem('Salir')
        salir.connect('activate', self.salir)
        menu.append(salir)
        menu.show_all()
        return menu

    def seleccionarIcono(self,descripcionClima):
        imagenController = ImagenController()
        return imagenController.obtenerImagen(descripcionClima, TipoImagen.panel)

    def salir(self,source):
        gtk.main_quit()

    def verMas(self,source):
        PronosticoController(self.pronostico).pantalla.show_all()

    def configuracion(self,source):
        PantallaConfiguracion(self.pronostico.lugar,self.intervalo).show_all()

    def actualizarIndicador(self):
       while True:
            intervaloEnSegundos = self.intervalo * 3600
            time.sleep(intervaloEnSegundos)
            GObject.idle_add(self.modificarIndicador,None)
             
    def modificarIndicador(self, source):
        lugar = self.pronostico.lugar
        self.pronostico =  Pronostico(lugar)
        self.indicador.set_label(self.pronostico.clima.temperatura + " ºC",'Clima App')
        self.indicador.set_menu(self.crearMenu())
        self.indicador.set_icon(self.seleccionarIcono(self.pronostico.clima.descripcionClima))
        notify.init(self.app)
        notify.Notification.new(self.app,"<b>La infomación del tiempo en " + self.pronostico.lugar + " fue actualizada, consulte el indicador para mas detalles</b>").show()