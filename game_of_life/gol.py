from Tkinter import *
from collections import defaultdict
from time import sleep
import random

game_width = 500
game_height = 500
sleep_time = 100
square_size = 10

grid_width = game_width/square_size
grid_height = game_height/square_size


grid = {}
for y in range(-1, grid_height + 1):
    grid[y] = defaultdict(bool)


def switch_square(x, y):
    coordx = x * square_size
    coordy = y * square_size
    if grid[y][x]:
        color = 'white'
    else:
        color = 'black'
    w.create_rectangle(coordx, coordy, coordx + square_size, coordy + square_size, fill = color, width = 0)
    grid[y][x] = not grid[y][x]


def select_item(e):
    switch_square(e.x / square_size, e.y / square_size)


def run_game():
    new_grid = {}
    for y in range(0, grid_height):
        new_grid[y] = {}
        for x in range(0, grid_width):
            neigh = 0
            neigh += grid[y - 1][x] 
            neigh += grid[y][x - 1]
            neigh += grid[y + 1][x] 
            neigh += grid[y][x + 1] 
            neigh += grid[y+1][x + 1] 
            neigh += grid[y+1][x - 1] 
            neigh += grid[y-1][x + 1] 
            neigh += grid[y-1][x - 1]
                
            if grid[y][x] and neigh <= 1:
                lives = False
            elif grid[y][x] and neigh <= 3:
                lives = True
            elif neigh == 3:
                lives = True
            else:
                lives = False

            new_grid[y][x] = lives
        
    for y in range(0, grid_height):
        for x in range(0, grid_width):
            if new_grid[y][x] != grid[y][x]:
                switch_square(x, y)

    master.after(sleep_time, run_game)


def gen_random_data():
    for y in range(0, grid_height):
        for x in range(0, grid_width):
            on = bool(random.randint(0, 1))
            if grid[y][x] != on:
                switch_square(x, y)

master = Tk()

w = Canvas(master, width = game_width, height = game_height)


w.bind('<Button-1>', select_item)
w.pack()

m = Menu(master)
_file = Menu(m)
_file.add_command(label = 'Run', command = run_game)
_file.add_command(label = 'Generate random data', command = gen_random_data)
m.add_cascade(label = 'File', menu = _file)

master.config(menu = m)
master.mainloop()
