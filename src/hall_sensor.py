from gpiozero import DigitalInputDevice

# Pin GPIO 17 
# pull_up=True (Active Low)
sensor = DigitalInputDevice(17, pull_up=True)

contador_pulsos = 0

def detectar():
    global contador_pulsos
    contador_pulsos += 1

# interrupción
sensor.when_activated = detectar

def obtener_pulsos():
    return contador_pulsos

if __name__ == "__main__":
    print("Prueba individual: Sensor Hall (A3144)")
    from signal import pause
    sensor.when_activated = lambda: print(f"Imán detectado un  Total: {contador_pulsos + 1}")
    pause()
