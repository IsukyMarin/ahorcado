import random

def obtener_palabra():
    palabras = [
        'casa', 'perro', 'gato', 'arbol', 'coche', 'sol', 'luna', 'estrella',
        'cielo', 'mar', 'montana', 'rio', 'computadora', 'telefono', 'zapato',
        'camisa', 'pantalon', 'musica', 'libro', 'silla', 'mesa', 'ventana', 
        'puerta', 'jardin', 'reloj', 'lampara', 'cocina', 'bano', 'plato', 'cuchara'
    ]
    return random.choice(palabras)

def mostrar_tablero(palabra, intentos):
    tablero = ''
    for letra in palabra:
        if letra in intentos:
            tablero += letra
        else:
            tablero += '_'
    return tablero

def juego_ahorcado():
    print("¡Bienvenido al juego de Ahorcado!")
    palabra_secreta = obtener_palabra()
    intentos = []
    intentos_fallidos = 0
    max_intentos = 6

    while intentos_fallidos < max_intentos:
        tablero = mostrar_tablero(palabra_secreta, intentos)
        print(f"Palabra: {tablero}")
        print(f"Intentos fallidos: {intentos_fallidos} de {max_intentos}")
        print(f"Letras intentadas: {', '.join(intentos)}")

        if tablero == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra.")
            break

        intento = input("Adivina una letra: ").lower()
        if intento in intentos:
            print("Ya has intentado esa letra.")
        elif intento in palabra_secreta:
            intentos.append(intento)
        else:
            intentos.append(intento)
            intentos_fallidos += 1

    if intentos_fallidos == max_intentos:
        print(f"Has perdido. La palabra era: {palabra_secreta}")
    
    if input("Lo siento, has fallado. ¿Quieres intentarlo de nuevo? (s/n): ").lower() == 's':
        juego_ahorcado()
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")
        input("Presiona cualquier tecla para salir...")

if __name__ == "__main__":
    juego_ahorcado()

