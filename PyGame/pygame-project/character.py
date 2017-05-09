class Character():
    def __init__(self, x, y, speed_x, speed_y, name):
        self.name = name
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x > 512 - 64:
            self.x = 512 - 64
        if self.x < 32:
            self.x = 32
        if self.y > 480 - 64:
            self.y = 480 - 64
        if self.y < 32:
            self.y = 32
