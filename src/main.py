import time
import threading
import hall_sensor
import temp_sensor

def main():
    print("Iniciando")

    sensor_ir = temp_sensor.inicializar_temp()
    
    #última temperatura leída
    datos = {"temp": 0.0}

    #temperatura sin bloquear los pulsos
    def loop_temp():
        while True:
            datos["temp"] = temp_sensor.leer(sensor_ir)
            time.sleep(1) # Actualizar cada segundo

    hilo_t = threading.Thread(target=loop_temp, daemon=True)
    hilo_t.start()

    try:
        while True:
            pulsos_actuales = hall_sensor.obtener_pulsos()
            temperatura = datos["temp"]

            print("-" * 40)
            print(f"Temp. Motor: {temperatura:.2f} °C")
            print(f"Pulsos Hall: {pulsos_actuales}")
            
            # Pausa de visualización (no afecta el conteo de pulsos)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nSaliendo")

if __name__ == "__main__":
    main()
