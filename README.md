# Telemetría Raspberry Pi

Proyecto de pruebas para adquisición de datos usando Raspberry Pi 4 y sensores.

## Objetivo
Desarrollar y probar código en una computadora local para después implementarlo en una Raspberry Pi dentro del sistema de telemetría.

## Hardware objetivo
- Raspberry Pi 4
- Sensores
- Comunicación por GPIO e I2C

## Estructura del proyecto
src/        -> Código fuente
tests/      -> Pruebas
docs/       -> Documentación técnica

## Instalación

1. Clonar el repositorio
git clone https://github.com/usuario/proyecto.git
ejemplo: git clone https://github.com/Sromero25/electraton-telemetria

2. Crear entorno virtual
python -m venv venv

3. Activar entorno

Linux / Mac:
source venv/bin/activate

Windows:
venv\Scripts\activate

4. Instalar dependencias
pip install -r requirements.txt

## Objetivo de desarrollo
El código se desarrolla en PC y posteriormente se despliega en Raspberry Pi para pruebas con hardware real.

## Estructura
* **Base de Datos:** InfluxDB (Almacenamiento de series de tiempo).
* **Visualización:** Grafana (Dashboards de telemetría en tiempo real).
* **Lenguaje:** Python

## Flujo de Desarrollo(sw)
1. **Simulación (VMware):** Desarrollo y pruebas de lógica.
2. **Despliegue:** Migración del código a la Raspberry Pi física vía Git.
3. **Verificación:** Pruebas de campo con sensores reales y ajuste de calibración.

## Configuración de Red (Importante para la Universidad)
Debido a las restricciones de la red universitaria, es obligatorio usar **HTTPS**. 
Para actualizar los repositorios e instalar librerías, se utilizaron los siguientes comandos para forzar dominios seguros:

    sudo nano /etc/apt/sources.list
Cambiar: http:// por https:// *Solo se agrega una s lo vuelve Security*
    Ctrl + o para guardar
    Enter
    Ctrl + x para salir