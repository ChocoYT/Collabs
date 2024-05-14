import keyboard
import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int], size: int, colour: tuple[int]) -> None:
        super().__init__()

        self.x, self.y = position
        self.xVel, self.yVel = 0, 0
        self.speed = 2
        self.friction = 0.8

        self.size = size
        self.colour = colour
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.colour)

        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def move(self, collisions: list[pygame.sprite.Group | None]) -> None:
        moveX = (keyboard.is_pressed("D") or keyboard.is_pressed("RIGHT")) - (keyboard.is_pressed("A") or keyboard.is_pressed("LEFT"))
        moveY = (keyboard.is_pressed("W") or keyboard.is_pressed("UP")) - (keyboard.is_pressed("S") or keyboard.is_pressed("DOWN"))
        moveDist = ((moveX ** 2) + (moveY ** 2)) ** 0.5

        if moveDist > 1:
            moveX /= moveDist
            moveY /= moveDist

        self.xVel += moveX * self.speed
        self.yVel += moveY * self.speed

        # X collision / movement
        oldX = self.x
        self.rect.x += self.xVel
        if self.collide(collisions):
            while self.collide(collisions):
                self.rect.x -= abs(self.xVel) // self.xVel
        self.x = self.rect.x
        self.rect.x = oldX

        # Y collision / movement
        oldY = self.y
        self.rect.y -= self.yVel
        if self.collide(collisions):
            while self.collide(collisions):
                self.rect.y += abs(self.yVel) // self.yVel
        self.y = self.rect.y
        self.rect.y = oldY

        self.xVel *= self.friction
        self.yVel *= self.friction

    def collide(self, spriteGroups: list[pygame.sprite.Group | None]) -> None:
        player = pygame.sprite.GroupSingle(self)
        collision = False

        for spriteGroup in spriteGroups:
            if pygame.sprite.spritecollide(player.sprite, spriteGroup, False):
                collision = True

        return collision

    def update(self) -> None:
        self.rect.center = self.x, self.y

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect.center)
