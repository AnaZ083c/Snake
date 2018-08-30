# Author: a GitHub user AnaZ083c

import pygame
import time
import random

class Window:
    window_w = 800
    window_h = 600

    def __init__(self, window_h = 600, window_w = 800):
        self.window_h = window_h
        self.window_w = window_w
        self.win = pygame.display.set_mode((self.window_w, self.window_h))

    def close(self):
        pygame.quit()
        quit()

class Snake(Window):
    snake_w = 10
    snake_h = 10

    def __init__(self, x = (0.5 * (Window.window_w - snake_w)), y = (0.5 * (Window.window_h - snake_w)), snake_w = 10, snake_h = 10):
        self.snake_w = snake_w
        self.snake_h = snake_h
        self.x = x
        self.y = y

    #def __del__(self):


    def draw(self):
        pygame.draw.rect(window.win, (255, 0, 0), [self.x, self.y, self.snake_w, self.snake_h])


class Apple(Window):
    apple_w = 20
    apple_h = 20

    def __init__(self, apple_w = 20, apple_h = 20):
        self.apple_w = apple_w
        self.apple_h = apple_h
        self.x = random.randrange(0, (Window.window_w - self.apple_w))
        self.y = random.randrange(0, (Window.window_h - self.apple_h))

    def draw(self):
        pygame.draw.rect(window.win, (255, 255, 0), [self.x, self.y, self.apple_w, self.apple_h])

pygame.init()

window = Window(600, 800)
win = window.win
pygame.display.set_caption('Kaca')
clock = pygame.time.Clock()

snake_part = Snake(10, 10)

snake_body = [Snake(), Snake(), Snake()]
snake_body[1].x -= snake_body[1].snake_w
snake_body[2].x += snake_body[2].snake_w

apple = Apple()

def apple_reset():
    apple.x = random.randrange(0, (Window.window_w - apple.apple_w/2))
    apple.y = random.randrange(0, (Window.window_h - apple.apple_h/2))

def got_apple():
    if snake_body[0].x > apple.x and snake_body[0].x < apple.x + apple.apple_w or snake_body[0].x + snake_body[0].snake_w > apple.x and snake_body[0].x + snake_body[0].snake_w < apple.x + apple.apple_w:
      if snake_body[0].y > apple.y and snake_body[0].y < apple.y + apple.apple_h:
          snake_body.append((Snake(snake_body[0].x + 2 * snake_body[0].snake_w)))
          apple_reset()

      elif snake_body[0].y + snake_body[0].snake_h > apple.y and snake_body[0].y + snake_body[0].snake_h < apple.y + apple.apple_h:
           snake_body.append((Snake(snake_body[0].x + 2 * snake_body[0].snake_w)))
           apple_reset()

def reset_position():
    if len(snake_body) > 3:
        for i in range(3, len(snake_body)):
            del snake_body[i]

    snake_body[0].x = (0.5 * (window.window_w - snake_body[0].snake_w))
    snake_body[0].y = (0.5 * (window.window_h - snake_body[0].snake_w))

    snake_body[1].x = snake_body[0].x - snake_body[1].snake_w
    snake_body[1].y = (0.5 * (window.window_h - snake_body[1].snake_w))

    snake_body[2].x = snake_body[0].x + snake_body[2].snake_w
    snake_body[2].y = (0.5 * (window.window_h - snake_body[2].snake_w))


def snake_w():
    width = 0
    for i in range(len(snake_body)):
        width += snake_body[i].snake_w

    return width

def draw_snake():
    for i in range(len(snake_body)):
        snake_body[i].draw()

speed = 0.05 # v sekundah
snake_width = snake_w()
glava = snake_body[0]
x = glava.x
y = glava.y

def move_snake(direction):
    for i in range(0, len(snake_body)):
        head = snake_body[0]

        if direction == 'left':
            time.sleep(speed)
            snake_body.insert(0, Snake((head.x - head.snake_w), head.y))
            del snake_body[-1]

        elif direction == 'right':
            time.sleep(speed)
            snake_body.insert(0, Snake((head.x + head.snake_w), head.y))
            del snake_body[-1]

        elif direction == 'up':
            time.sleep(speed)
            snake_body.insert(0, Snake(head.x, (head.y - head.snake_h)))
            del snake_body[-1]

        elif direction == 'down':
            time.sleep(speed)
            snake_body.insert(0, Snake(head.x, (head.y + head.snake_h)))
            del snake_body[-1]

def apple_scores(scores):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Tocke: " + str(scores), True, (255, 255, 255))
    win.blit(text, (0, 0))

def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 0))
    return textSurface, textSurface.get_rect()

def display_msg(text):
    largeText = pygame.font.Font('ARCADECLASSIC_0.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((window.window_w / 2), (window.window_h/2))
    win.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(3)

    apple_reset()
    reset_position()
    restart()

def game_over():
    display_msg("Konec igre")

def restart():
   # moving = True
    left = False
    right = False
    up = False
    down = False

    exit = False
    while not exit:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.close()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            window.close()

        if keys[pygame.K_LEFT]:
            left = True
            right = False
            up = False
            down = False

        elif keys[pygame.K_RIGHT]:
            left = False
            right = True
            up = False
            down = False

        elif keys[pygame.K_UP]:
            left = False
            right = False
            up = True
            down = False

        elif keys[pygame.K_DOWN]:
            left = False
            right = False
            up = False
            down = True

        if left:
            move_snake('left')

        elif right:
            move_snake('right')

        elif up:
            move_snake('up')

        elif down:
            move_snake('down')

        win.fill((0, 0, 0))
        apple.draw()
        draw_snake()

        if ((snake_body[0].x + snake_body[0].snake_w * len(snake_body)) >= window.window_w) or ((snake_body[0].x - snake_body[0].snake_w) <= 0) or ((snake_body[0].y - snake_body[0].snake_h) <= 0) or ((snake_body[0].y + snake_body[0].snake_h) >= window.window_h):
            game_over()

        got_apple()

        pygame.display.update()

restart()
window.close()


