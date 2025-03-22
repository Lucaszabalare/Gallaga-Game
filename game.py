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

is_game_over = False
bullets = []
score = 0
lives = 3
enemies = []
for i in range(8):
    enemy = Actor("bee")
    enemy.x = random.randint(0,WIDTH - 80)
    enemy.y = random.randint(-100,0)
    enemies.append(enemy)

speed = 5
# Function to display score
def display_score():
    screen.draw.text(f"Score: {score}",(50,30))
    screen.draw.text(f"Lives: {lives}",(50,60))

# Function to handle bullets
def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        bullet.x = gallaga.x
        bullet.y = gallaga.y - 50
        bullets.append(bullet)

def update():
    global score
    global lives
    
    # Moving the ship right or left
    if keyboard.left:
        gallaga.x -= speed
        if gallaga.x <= 0:
            gallaga.x = 0
    if keyboard.right:
        gallaga.x += speed
        if gallaga.x >= WIDTH:
            gallaga.x = WIDTH
    # Move bullets
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 10
    
    # Move enemies
    move_down = False
    for enemy in enemies:
        enemy.y += 5
        if enemy.y > HEIGHT:
            enemy.x = random.randint(0,WIDTH - 80)
            enemy.y = random.randint(-100,0)
        # Check collision with bullets
        for bullet in bullets:
            if enemy.colliderect(bullet):
                sounds.eep.play()
                score += 100
                bullets.remove(bullet)
                enemies.remove(enemy)
        # Check collision with gallaga
        if enemy.colliderect(gallaga):
            lives -= 1
            enemies.remove(enemy)
            if lives == 0:
                game_over()

    # Continue creating enemies
    if len(enemies) < 8:
        enemy = Actor("bee")
        enemy.x = random.randint(0,WIDTH - 80)
        enemy.y = random.randint(-100,0)
        enemies.append(enemy)







pgzrun.go()