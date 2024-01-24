import pygame
import sys
import random

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 600, 400
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기 게임")

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 패들 클래스 정의
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((400, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# 공 클래스 정의
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 5
        self.speed_y = -5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 벽과의 충돌 체크
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top < 0:
            self.speed_y = -self.speed_y

# 블럭 클래스 정의
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 20))
        self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 그룹 생성
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()

# 패들, 공 생성
paddle = Paddle()
ball = Ball()

all_sprites.add(paddle, ball)

# 블럭 생성
for i in range(0, WIDTH, 60):
    block = Block(i, random.randint(50, 150))
    all_sprites.add(block)
    blocks.add(block)

# 게임 루프
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # 공과 패들의 충돌 체크
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y = -ball.speed_y

    # 공과 블럭의 충돌 체크
    block_hit_list = pygame.sprite.spritecollide(ball, blocks, True)
    if block_hit_list:
        ball.speed_y = -ball.speed_y

    # 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()