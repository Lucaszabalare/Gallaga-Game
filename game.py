import pgzrun
import random

WIDTH = 1200
HEIGHT = 600
TITLE = "Gallaga Game!"

RED = "red"
BLACK = "black"

# Create the player
gallaga = Actor("gallaga")
gallaga.pos = (WIDTH / 2,HEIGHT - 60)

bullets = []

enemies = []
for i in range(8):
    bee = Actor("bee")
    bee.x = random.randint(0,WIDTH - 80)
    bee.y = random.randint(-100,0)
    enemies.append(bee)


pgzrun.go()
