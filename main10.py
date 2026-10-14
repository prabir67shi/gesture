import random
import pygame

# Initialize Pygame and Mixer for sound
pygame.init()
pygame.mixer.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Part 2")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font for score display
font = pygame.font.SysFont(None, 36)

# --- Load Background and Sounds ---
# Note: Ensure you have an 'assets' folder containing 'background.png', 
# 'laser.wav', and 'explosion.wav', or replace these paths with your own files.
try:
    background = pygame.image.load("assets/background.png").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
except Exception:
    # Fallback to black screen if image is missing
    background = None

try:
    pygame.mixer.music.load("assets/background_music.mp3")
    pygame.mixer.music.play(-1)  # Loop background music infinitely
    pygame.mixer.music.set_volume(0.5)
except Exception:
    pass

try:
    collision_sound = pygame.mixer.Sound("assets/explosion.wav")
except Exception:
    collision_sound = None


# Define Player Class
class Player(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((40, 40))
    self.image.fill(BLUE)
    self.rect = self.image.get_rect()
    self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
    self.speed = 5

  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and self.rect.left > 0:
      self.rect.x -= self.speed
    if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
      self.rect.x += self.speed


# Define Enemy Class
class Enemy(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((30, 30))
    self.image.fill(RED)
    self.rect = self.image.get_rect()
    self.rect.x = random.randint(0, SCREEN_WIDTH - 30)
    self.rect.y = random.randint(50, 200)


# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create 7 enemy sprites positioned randomly
for _ in range(7):
  enemy = Enemy()
  all_sprites.add(enemy)
  enemies.add(enemy)

# Game variables
score = 0
clock = pygame.time.Clock()
running = True

# Main Game Loop
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Update all sprites
  all_sprites.update()

  # Check for collisions between player and enemies
  collisions = pygame.sprite.spritecollide(player, enemies, True)
  if collisions:
    score += len(collisions)
    if collision_sound:
      collision_sound.play()
    # Respawn new enemies to keep 7 active on screen
    for _ in range(len(collisions)):
      new_enemy = Enemy()
      all_sprites.add(new_enemy)
      enemies.add(new_enemy)

  # Draw background image or fill color
  if background:
    screen.blit(background, (0, 0))
  else:
    screen.fill(BLACK)

  # Draw all sprites
  all_sprites.draw(screen)

  # Render and display the score
  score_text = font.render(f"Score: {score}", True, WHITE)
  screen.blit(score_text, (10, 10))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()