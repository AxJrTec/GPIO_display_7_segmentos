import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Pines de los segmentos a-g
    pines_segmentos = [6, 13, 19, 26, 16, 20, 21]
    for pin in pines_segmentos:
        GPIO.setup(pin, GPIO.OUT)

    return pines_segmentos

def display_number(pines_segmentos, patron):
    for i in range(len(pines_segmentos)):
        GPIO.output(pines_segmentos[i], patron[i])

def main():
    pines_segmentos = setup()

    # Patrones para 0-F en display de 7 segmentos
    patron_digitos = [
        [1, 1, 1, 1, 1, 1, 0],  # 0
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 1, 0, 1, 1],  # 9
        [1, 1, 1, 0, 1, 1, 1],  # A
        [0, 0, 1, 1, 1, 1, 1],  # b
        [1, 0, 0, 1, 1, 1, 0],  # C
        [0, 1, 1, 1, 1, 0, 1],  # d
        [1, 0, 0, 1, 1, 1, 1],  # E
        [1, 0, 0, 0, 1, 1, 1]   # F
    ]

    digitos_hex = ['0', '1', '2', '3', '4', '5', '6', '7', 
                   '8', '9', 'A', 'b', 'C', 'd', 'E', 'F']

    while True:
        for i in range(len(patron_digitos)):
            print(digitos_hex[i])
            display_number(pines_segmentos, patron_digitos[i])
            time.sleep(1)

    GPIO.cleanup()

if __name__ == "__main__":
    main()
