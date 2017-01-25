#!/bin/sh
echo Instalando aplicación...
cd ..
chmod +x GenerarLanzador.py
sudo ./GenerarLanzador.py
chmod -x GenerarLanzador.py
echo Instalación realizada con exito
