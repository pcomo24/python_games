import pygame
from enemy import *
import random

class Goblin(Enemy):
    pass

goblin = Goblin(random.randint(0, 512), random.randint(0, 480), 15, 15, 'goblin')
