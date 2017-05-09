import pygame
import random
import time

class Enemy():
    def __init__ (self, x, y, speed_x,speed_y, name):
        self.name = name
        self.speed_x = 15
        self.speed_y = 15
        self.x = x
        self.y = y

    def move_right(self):
        self.x += self.speed_x
        if self.x > 512:
            self.x = 0
    def move_left(self):
        self.x -= self.speed_x
        if self.x < 0:
            self.x = 512
    def move_north(self):
        self.y -= self.speed_y
        if self.y < 0:
            self.y = 480
    def move_south(self):
        self.y += self.speed_y
        if self.y > 480:
            self.y = 0
    def move_nr(self):
        self.x += self.speed_x
        self.y -= self.speed_y
        if self.y < 0:
            self.y = 480
        if self.x < 0:
            self.x = 512
    def move_sr(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y < 0:
            self.y = 480
        if self.x < 0:
            self.x = 512
    def move_nl(self):
        self.x -= self.speed_x
        self.y -= self.speed_y
        if self.y < 0:
            self.y = 480
        if self.x < 0:
            self.x = 512
    def move_sl(self):
        self.x -= self.speed_x
        self.y += self.speed_y
        if self.y < 0:
            self.y = 480
        if self.x < 0:
            self.x = 512

    def move_enemy(self):
        if direction_change == 0:
            self.move_right()
        elif direction_change == 1:
            self.move_north()
        elif direction_change == 2:
            self.move_left()
        elif direction_change == 3:
            self.move_south()
        elif direction_change == 4:
            self.move_sl()
        elif direction_change == 5:
            self.move_sr()
        elif direction_change == 6:
            self.move_nr()
        elif direction_change == 7:
            self.move_nl()
        pygame.time.delay(2000)

change_dir_countdown = 120
change_dir_countdown -=1
if change_dir_countdown is 0:
    direction_change = random.randint(0,7)
    change_dir_countdown = 120
clock.tick(60)
