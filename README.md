<h1 align="center">
    <br>
    <img src="https://raw.githubusercontent.com/joancipria/ireves-map/master/public/img/ireves-logo.png" alt="Reves Map">
</h1>

Reves Map forma parte de [iReves](http://ireves.webs.upv.es/), una herramienta inteligente de ayuda a la toma de decisiones para la innovación en la Reubicación de Vehículos de Emergencias Sanitarias. Reves Map tiene como finalidad ayudar a visualizar fácilmente el impacto que las decisiones pueden tener sobre la cantidad de población que estaría cubierta ante una emergencia. Este repositorio contiene el código fuente del servidor. Puedes acceder al repositorio del cliente web desde [aquí](https://github.com/joancipria/ireves-map).

![screenshot](https://raw.githubusercontent.com/joancipria/ireves-map/master/screenshot.png)

## 📦 Instalación
Probado con `Python 3.7.12` y `pip 20.1.1`.

### Instala `rasterio` en tu sistema
```
sudo apt install rasterio # o pamac install python-rasterio
```

### Clona el repositorio
```
git clone https://github.com/joancipria/ireves-map-server.git
cd ireves-map-server
```

### Crea un entorno virtual
```
python3.7 -m venv venv
. venv/bin/activate
```

### Instala las dependencias
```
sudo pip install rasterio --no-binary :all:
sudo pip install -r requirements.txt
```

## 🤖 Ejecución
```
export FLASK_ENV=development
flask run --host=0.0.0.0
```

## 📝 Publicaciones
   
- Se actualizará próximamente.

## 👨‍💻 Contribuciones
Siéntete libre de enviar una `pull request` a este repositorio con tus contribuciones.

## 📜 Licencia
Licenciado bajo GNU General Public License v3. [iReves](http://ireves.webs.upv.es/) es un proyecto de investigación de la Universitat Politècnica de València.
<div align="center">
<img style="width: 15%" title="a title" alt="Alt text" src="https://raw.githubusercontent.com/joancipria/VIHrtualApp-app/master/static/img/logos/upv.jpg">
</div>
