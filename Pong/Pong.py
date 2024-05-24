import pygame
import sys
import math
import random

# initialize the stuffs
pygame.init()

# sets up the screen
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Pongpong")

# colorful
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# paddle setup
paddleWidth = 10
paddleHeight = 80
paddleSpeed = 4

# ball setup
ballSize = 10
ballSpeed = 5
ballSpeedIncr = 1.1

# fonts for the scorekeep
fontBigness = 36
FONT = pygame.font.Font(None, fontBigness)

# the scorekeep itself
pScore = 0
cScore = 0

# paddle initialization/use
class Paddle(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def move(self, dy):
        self.y += dy
        self.clamp_ip(screen.get_rect())

# ball initialization/use
class Ball(pygame.Rect):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)
        self.speed = ballSpeed
        self.dx = 1
        self.dy = 0

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def reset(self):
        self.center = (w // 2, h // 2)
        self.dx = 1 if random.random() < 0.5 else -1
        self.dy = 0
        self.speed = ballSpeed

# actually makes the paddles and ball
pPaddle = Paddle(50, h // 2 - paddleHeight // 2, paddleWidth, paddleHeight)
cPaddle = Paddle(w - 50 - paddleWidth, h // 2 - paddleHeight // 2, paddleWidth, paddleHeight)
ball = Ball(w // 2 - ballSize // 2, h // 2 - ballSize // 2, ballSize)

# game goes game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # moves paddle towards mouse at set speed
    yMouse = pygame.mouse.get_pos()[1]
    if abs(yMouse - pPaddle.centery) > paddleSpeed:
        if yMouse > pPaddle.centery:
            pPaddle.move(paddleSpeed)
        else:
            pPaddle.move(-paddleSpeed)

    # moves computer paddle towards current ball height at set speed
    if ball.dx > 0:
        if cPaddle.centery < ball.centery:
            cPaddle.move(paddleSpeed)
        elif cPaddle.centery > ball.centery:
            cPaddle.move(-paddleSpeed)

    # ball go brrr
    ball.move()

    # checks for paddle hit ball nad what happen when hit ball
    if ball.colliderect(pPaddle) or ball.colliderect(cPaddle):
        ball.dx *= -1
        pCenter = pPaddle.centery if ball.colliderect(pPaddle) else cPaddle.centery
        cDistance = ball.centery - pCenter
        dNormalized = cDistance / (paddleHeight / 2)
        angle = dNormalized * math.radians(45)
        ball.dy = math.sin(angle)
        ball.speed *= ballSpeedIncr

    # if hit top or bottom wall, bounce!
    if ball.top <= 0 or ball.bottom >= h:
        ball.dy *= -1

    # if it goes past a paddle, SCOOOOOORRRE!!
    if ball.left <= 0:
        cScore += 1
        ball.reset()
    elif ball.right >= w:
        pScore += 1
        ball.reset()

    # BLACK!
    screen.fill(BLACK)

    # draws pretty pictures for everything
    pygame.draw.rect(screen, WHITE, pPaddle)
    pygame.draw.rect(screen, WHITE, cPaddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # draw the score
    pScoreText = FONT.render(str(pScore), True, WHITE)
    cScoreText = FONT.render(str(cScore), True, WHITE)
    screen.blit(pScoreText, (w // 4, 20))
    screen.blit(cScoreText, (w * 3 // 4, 20))

    # refreshes display
    pygame.display.flip()

    # framerate baby!
    pygame.time.delay(10)