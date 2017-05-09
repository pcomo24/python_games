import pygame
import random
import time
from enemy import *

class Monster(Enemy):
    pass

monster = Monster(random.randint(0, 512),random.randint(0, 480), 15, 15, 'monster')
