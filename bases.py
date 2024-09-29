import pymysql
from pymysql import Error
from tkinter import *
import threading

# Función para conectar a la base de datos
def crear_conexion():
    try:
        connection = pymysql.connect(
        host='junction.proxy.rlwy.net',
        user='Editor_Stephany',
        password='123456',
        database='ProyectoParcial',
        port=25596,
        connect_timeout=10
    )
        if connection.open:
            print("Conexión exitosa a la base de datos")
        return connection
    except Error as e:
        print(f"Error al conectar: {e}")
        return None

# Función para llamar al procedimiento almacenado y registrar el voto
def enviar_direccion_a_db(direccion, usuario_id):
    connection = crear_conexion()
    if connection:
        try:
            cursor = connection.cursor()
            # Llamada al procedimiento almacenado con dirección y usuario_id
            cursor.callproc('registrar_voto', [direccion, usuario_id])
            
            # Obtener el resultado del procedimiento
            result = cursor.fetchall()
            for row in result:
                print(row)
            
            connection.commit()
            cursor.close()
        except Error as e:
            print(f"Error al insertar el voto: {e}")
        finally:
            connection.close()

# Funciones para los botones de movimiento que envían el voto
def move_up():
    enviar_direccion_a_db("up", 1)  # Asigna un ID de usuario (cambiar 1 por el ID real)

def move_down():
    enviar_direccion_a_db("down", 1)

def move_left():
    enviar_direccion_a_db("left", 1)

def move_right():
    enviar_direccion_a_db("right", 1)

# Interfaz gráfica con Tkinter
def tkinter_controls():
    ventana = Tk()
    ventana.title("Control del juego")
    ventana.geometry("400x200")

    # Botones de dirección
    btn_up = Button(ventana, text="↑", command=move_up, width=5, height=2)
    btn_up.pack(side=TOP, pady=5)

    btn_down = Button(ventana, text="↓", command=move_down, width=5, height=2)
    btn_down.pack(side=BOTTOM, pady=5)

    btn_left = Button(ventana, text="←", command=move_left, width=5, height=2)
    btn_left.pack(side=LEFT, padx=5)

    btn_right = Button(ventana, text="→", command=move_right, width=5, height=2)
    btn_right.pack(side=RIGHT, padx=5)

    ventana.mainloop()

# Ejecutar la ventana en un hilo separado
if __name__ == "__main__":
    tkinter_thread = threading.Thread(target=tkinter_controls)
    tkinter_thread.start()
