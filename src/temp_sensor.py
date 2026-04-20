import board
import busio
import adafruit_mlx90614

def inicializar_temp():
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        return adafruit_mlx90614.MLX90614(i2c)
    except Exception as e:
        print(f"Error: {e}")
        return None

def leer(sensor):
    if sensor:
        try:
            return sensor.object_temperature
        except:
            return 0.0
    return 0.0

if __name__ == "__main__":
    print("Prueba: MLX90614")
    s = inicializar_temp()
    if s:
        import time
        while True:
            print(f"Temp: {leer(s):.2f}°C")
            time.sleep(1)
