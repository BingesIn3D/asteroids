import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from bullet import *

def quit():
    game_active=False
def main():
    pygame.init
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidable = pygame.sprite.Group()
    fireable = pygame.sprite.Group()
    Player.containers=(updatable,drawable)
    Asteroid.containers=(updatable,drawable,asteroidable)
    AsteroidField.containers=(updatable)
    Bullet.containers=(fireable,updatable,drawable)
    print("Starting asteroids!\nScreen width:",SCREEN_WIDTH,"\nScreen height:",SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()
    game_active=True
    timer=pygame.time.Clock()
    dt=0
    while game_active:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroidable:
            for bullet in fireable:
                if asteroid.collide(bullet):
                    asteroid.split()
                    bullet.kill()
            if asteroid.collide(player):
                print("|======== GAME OVER ========|")
                return
        dt=timer.tick(60) /1000
        pygame.display.flip()

if __name__ == "__main__":
    main()
