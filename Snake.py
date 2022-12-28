# Snake Game replicated in Python, simple premise
# Move with W,A,S,D for control to collect white food
# to increase in length. Collide with yourself or the edge would
# cause a Game Over.
# Author: Monthon Paul
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set the width and height of the screen
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption('Snake')

# Set the dimensions of each segment of the snake
segment_width, segment_height = 20, 20

# Set the movement speed of the snake (in pixels per frame)
movement_speed = 20

# Set the color of the snake
snake_color = (0, 255, 0)

# Set the color of the food
food_color = (255, 0, 0)

# Set the font and size for the score text
font = pygame.font.Font(None, 36)

# Initialize the snake's position and direction
snake_position = [(screen_width / 2), (screen_height / 2)]
direction = "right"

# Initialize the list of segments for the snake
snake_segments = [[(screen_width / 2), (screen_height / 2)],
                  [(screen_width / 2) - movement_speed, (screen_height / 2)]]

# Initialize the position of the food
food_position = [random.randrange(1, (screen_width / segment_width)) * movement_speed,
                 random.randrange(1, (screen_height / segment_height)) * movement_speed]
food_spawn = True

# Initialize the score
score = 0

# Set the game clock
clock = pygame.time.Clock()

# Run the game loop
while True:
    # Check for events (key presses, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if direction != "down":
                    direction = "up"
            elif event.key == pygame.K_s:
                if direction != "up":
                    direction = "down"
            elif event.key == pygame.K_a:
                if direction != "right":
                    direction = "left"
            elif event.key == pygame.K_d:
                if direction != "left":
                    direction = "right"

    # Check if the snake has collided with the edge of the screen
    if snake_position[0] > screen_width - segment_width or snake_position[0] < 0 or snake_position[1] > screen_height - segment_height or snake_position[1] < 0:
        pygame.quit()
        sys.exit()

    # Check if the snake has collided with itself
    for segment in snake_segments[1:]:
        if snake_position == segment:
            pygame.quit()
            sys.exit()

    # Move the snake
    if direction == "up":
        snake_position[1] -= movement_speed
    elif direction == "down":
        snake_position[1] += movement_speed
    elif direction == "left":
        snake_position[0] -= movement_speed
    elif direction == "right":
        snake_position[0] += movement_speed

    # Add the new segment to the front of the snake and remove the last segment
    snake_segments.insert(0, list(snake_position))
    if snake_position == food_position:
        score += 1
        food_spawn = False
    else:
        snake_segments.pop()

    # Check if the food needs to be spawned
    if not food_spawn:
        food_position = [random.randrange(1, (screen_width / segment_width)) * movement_speed,
                         random.randrange(1, (screen_height / segment_height)) * movement_speed]
    food_spawn = True

    # Draw the screen
    screen.fill((0, 0, 0))
    for position in snake_segments:
        pygame.draw.rect(screen, snake_color, pygame.Rect(
            position[0], position[1], segment_width, segment_height))
    pygame.draw.rect(screen, food_color, pygame.Rect(
        food_position[0], food_position[1], segment_width, segment_height))
    score_text = font.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(score_text, (5, 10))
    pygame.display.update()
    clock.tick(10)
