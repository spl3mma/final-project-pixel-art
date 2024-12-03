import pygame
pygame.init()

def main():
    screen = pygame.display.set_mode((960, 540))

    sprites_down = [pygame.image.load("pixil-frame-0.png"),
                    pygame.image.load("pixil-frame-1.png"),
                    pygame.image.load("pixil-frame-2.png")]
    sprites_right = [pygame.image.load("pixil-frame-3.png"),
                    pygame.image.load("pixil-frame-4.png"),
                    pygame.image.load("pixil-frame-5.png")]
    sprites_left = [pygame.image.load("pixil-frame-6.png"),
                    pygame.image.load("pixil-frame-7.png"),
                    pygame.image.load("pixil-frame-8.png")]
    sprites_up = [pygame.image.load("pixil-frame-9.png"),
                    pygame.image.load("pixil-frame-10.png"),
                    pygame.image.load("pixil-frame-11.png")]

    current_sprites = sprites_down
    current_frame = 0

    bg_img = pygame.image.load("bg.png")

    sprite_rect = sprites_down[0].get_rect()

    sprite_rect.x = 430
    sprite_rect.y = 220

    speed = 3

    bg_x = 0
    bg_y = 0

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        current_frame += animate(keys)
        if keys[pygame.K_UP]:
            current_sprites = sprites_up
            sprite_rect.y -= speed
        if keys[pygame.K_DOWN]:
            current_sprites = sprites_down
            sprite_rect.y += speed
        if keys[pygame.K_RIGHT]:
            current_sprites = sprites_right
            sprite_rect.x += speed
        if keys[pygame.K_LEFT]:
            current_sprites = sprites_left
            sprite_rect.x -= speed

        if current_frame >= len(current_sprites):
            current_frame = 0

        current_frame = idle(keys, current_frame)

        sprite_rect.x, sprite_rect.y = screen_bounds(sprite_rect.x,sprite_rect.y)
        
        screen.blit(bg_img, [bg_x, bg_y])
        screen.blit(current_sprites[int(current_frame)], sprite_rect)

        pygame.display.flip()

        clock.tick(60)

def animate(inputKey):
    if any(inputKey):
        return 0.1
    else:
        return 0


def screen_bounds(x, y):
    if x < -25:
        x = -25
    if  y < -35:
        y = -35
    if x > 885:
        x = 885
    if y > 469:
        y = 469
    return x, y

def idle(inputKey, frame):
    if not any(inputKey):
        return 0
    else:
        return frame


if __name__ == "__main__":
    main()