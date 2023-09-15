"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] * 4
state = {'mark': None}
hide = [True] * 32
tap_count = 0  # Variable para contar los taps
all_uncovered = False  # Variable para rastrear si todas las tarjetas están destapadas


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global tap_count, all_uncovered

    if all_uncovered:
        return  # Si todas las tarjetas están destapadas, no hagas nada

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    tap_count += 1  # Incrementa el conteo de taps
    print("Taps:", tap_count)  # Muestra el conteo de taps en la consola

    hidden_count = hide.count(True)
    if hidden_count == 0:
        all_uncovered = True
        print("¡Todos los cuadros están destapados!")


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
     hidden_count = hide.count(True)

    for count in range(32):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
