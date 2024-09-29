import threading
from tkinter import *
import pygame as pg
import pygame_menu as pgm
from random import randrange, choice

# Variables para la interfaz
move_direction = None
pg.init()
H = pg.display.Info().current_h
W = pg.display.Info().current_w
CLOCK = pg.time.Clock()

# Crear ventana de juego
pg.display.set_mode((W // 2, H // 2), pg.RESIZABLE)
pg.display.set_caption("Snake")

# Colores de configuración
configColors = {
    "marco": "#FFFFFF",
    "background": "#000000",
    "head": "#10BD3E",
    "body": "#01DF3C",
    "food": "#952121",
    "ui": "#FFFFFF",
}
configNumbers = {
    "dimention": 25,
    "numManzanas": 1,
    "longManzana": 1,
    "speed": 250,
}

# Funciones de movimiento con Tkinter
def move_up():
    global move_direction
    move_direction = "up"

def move_down():
    global move_direction
    move_direction = "down"

def move_left():
    global move_direction
    move_direction = "left"

def move_right():
    global move_direction
    move_direction = "right"

# Interfaz de Tkinter
def tkinter_controls():
    ventana = Tk()
    ventana.title("Control del juego")
    ventana.geometry("400x200")

    btn_up = Button(ventana, text="↑", command=move_up, width=5, height=2)
    btn_up.pack(side=TOP, pady=5)

    btn_down = Button(ventana, text="↓", command=move_down, width=5, height=2)
    btn_down.pack(side=BOTTOM, pady=5)

    btn_left = Button(ventana, text="←", command=move_left, width=5, height=2)
    btn_left.pack(side=LEFT, padx=5)

    btn_right = Button(ventana, text="→", command=move_right, width=5, height=2)
    btn_right.pack(side=RIGHT, padx=5)

    ventana.mainloop()

# Clase para el juego Snake
class SnakeGame:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.snake = [(5, 5)]  # Posición inicial de la serpiente
        self.food = (10, 10)  # Posición de la comida
        self.direction = 'right'  # Dirección inicial
        self.running = True

    def update_direction(self):
        global move_direction
        if move_direction in ["up", "down", "left", "right"]:
            self.direction = move_direction

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == 'up':
            y -= 1
        elif self.direction == 'down':
            y += 1
        elif self.direction == 'left':
            x -= 1
        elif self.direction == 'right':
            x += 1

        # Actualizar la posición de la serpiente
        self.snake = [(x, y)] + self.snake[:-1]

    def check_collision(self):
        # Check colisiones con bordes o con el cuerpo
        x, y = self.snake[0]
        if x < 0 or y < 0 or x >= W // 2 or y >= H // 2 or len(self.snake) != len(set(self.snake)):
            self.running = False

    def draw(self):
        self.screen.fill(configColors["background"])
        for segment in self.snake:
            pg.draw.rect(self.screen, configColors["head"], (*segment, 25, 25))

        pg.draw.rect(self.screen, configColors["food"], (*self.food, 25, 25))
        pg.display.flip()

    def run_game(self):
        while self.running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False

            self.update_direction()
            self.move_snake()
            self.check_collision()
            self.draw()
            CLOCK.tick(configNumbers["speed"] // 10)

# Ejecutar ambas interfaces en hilos separados
if __name__ == "__main__":
    # Iniciar la interfaz de Tkinter en un hilo
    tkinter_thread = threading.Thread(target=tkinter_controls)
    tkinter_thread.start()

    # Iniciar el juego de Snake
    snake_game = SnakeGame()
    snake_game.run_game()

    # Esperar que el hilo de Tkinter termine
    tkinter_thread.join()