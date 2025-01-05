import pygame
from constants import *
from circleshape import *

class Bullet(CircleShape):
    def __init__(self,player):
        super().__init__(player.position.x,player.position.y,SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1).rotate(player.rotation)*PLAYER_SHOT_SPEED

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,SHOT_RADIUS,2)

    def update(self,dt):
        self.position+=self.velocity*dt
