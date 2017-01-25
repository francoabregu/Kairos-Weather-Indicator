#! /usr/bin/env python3
import os

with open('/usr/share/applications/kairos-weather-indicator.desktop', 'w+') as archivo:
	archivo.write("[Desktop Entry]\n")
	archivo.write("Name=Kairos Weather Indicator\n")
	archivo.write("Comment=Aplicacion de clima\n")
	archivo.write("Exec=" + os.getcwd() + "/Clima.sh\n")
	archivo.write("Terminal=false\n")
	archivo.write("Type=Application\n")
	archivo.write("Icon=indicator-weather\n")

