import pygame
import random

# Các hằng số
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Các màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Hàm để vẽ rắn và mồi
def draw_block(surface, color, position):
    r = pygame.Rect((position[0] * GRID_SIZE, position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, color, r)

# Hàm main
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Snake Game')
    clock = pygame.time.Clock()

    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    snake_direction = (1, 0)

    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != (0, 1):
                    snake_direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                    snake_direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                    snake_direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                    snake_direction = (1, 0)

        # Di chuyển rắn
        snake_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, snake_head)

        # Kiểm tra va chạm
        if snake_head == food:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        else:
            snake.pop()

        # Kiểm tra nếu rắn va chạm vào biên
        if snake_head[0] < 0 or snake_head[0] >= GRID_WIDTH or snake_head[1] < 0 or snake_head[1] >= GRID_HEIGHT:
            pygame.quit()
            return

        # Vẽ màn hình
        screen.fill(BLACK)
        draw_block(screen, RED, food)
        for block in snake:
            draw_block(screen, GREEN, block)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == '__main__':
    main()