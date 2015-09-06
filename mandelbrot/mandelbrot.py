from Tkinter import *

WIDTH = 400
HEIGHT = WIDTH
MAXN = 16

master = Tk()

canvas = Canvas(master, width = WIDTH, height = HEIGHT)
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state='normal')

def color(x):
    if x == MAXN:
        return '#000000'
    assert x > 0 and x < MAXN
    x = 1.0 / x 
    x = 0xFF * x 
    red = int(x)
    green = 0x00
    blue = 0x00
    def conv(c):
        return ('000' + hex(c)[2:])[-2:]

    return '#' + conv(red) + conv(green) + conv(blue)
    

def draw_pixel(x, y, c):
    img.put(c, (x, y))


def compute_pixel(a, b):
    x, y = (0.0, 0.0)
    n = 0
    while x**2 + y**2 < 4 and n < MAXN:
        x2 = x**2 - y**2 + a
        y2 = 2*x*y + b
        x, y = x2, y2
        n += 1
    n = min(n, MAXN)
    return n


def run():
    step = 4.0 / WIDTH
    a = -2.0
    EPS = 0.0000001
    results = []
    pixels = []
    while a < 2 + EPS:
        b = -2.0
        while b < 2 + EPS:
            n = compute_pixel(a, b)
            pixels += [(a, b)]
            c = color(n)
            pixx = int((a + 2) * (WIDTH / 4))
            pixy = int((b + 2) * (HEIGHT / 4))
            draw_pixel(pixx, pixy, c)

            b += step
        a += step

run()
canvas.pack()
master.mainloop()
