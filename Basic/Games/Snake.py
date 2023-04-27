import pygame
import random

# initialize pygame
pygame.init()

# define game variables
width = 500
height = 500
block_size = 20
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# set up the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# define the snake
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(width/2, height/2)]
        self.direction = random.choice([pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0]+(x*block_size)), (cur[1]+(y*block_size)))
        if new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(width/2, height/2)]
        self.direction = random.choice([pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN])

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, green, pygame.Rect(p[0], p[1], block_size, block_size))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))
                elif event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))

# define the food
class Food:
    def __init__(self):
        x = random.randint(0, (width-block_size )//block_size )*block_size 
        y = random.randint(0, (height-block_size)//block_size )*block_size 
        self.position = (x, y)
        self.color = red

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], block_size, block_size))

# define the main function
def main():
    # create objects
    snake = Snake()
    food = Food()

    # set up the game loop
    while True:
        clock.tick(10)

        # handle user input
        snake.handle_keys()

        # move the snake
        snake.move()

        # check for collisions
        if snake.get_head_position() == food.position:
            snake.length += 1
            food = Food()

        # draw the game objects
        screen.fill(black)
        snake.draw(screen)
        food.draw(screen)
