import pygame
from monster import *
from hero import *
from goblin import *
from enemy import *
import math
import random

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            background_image = pygame.image.load('images/background.png').convert_alpha()
            hero_image = pygame.image.load('images/hero.png')
            monster_image = pygame.image.load('images/monster.png')
            goblin_image = pygame.image.load('images/goblin.png')
            
            monster_life = True
            win_img = False
            pygame.font.init()
            myfont = pygame.font.Font('fonts/Krungthep.ttf', 15)
            play_again_img = myfont.render("YOU WON! To play again press enter", True, (255, 0, 0))

            # Event handling
                #hero moves
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.speed_y = -20
                elif event.key == pygame.K_s:
                    hero.speed_y = 20
                elif event.key == pygame.K_a:
                    hero.speed_x  = -20
                elif event.key == pygame.K_d:
                    hero.speed_x = 20
                elif event.key == pygame.K_RETURN:
                    monster.x = random.randint(0, 512)
                    monster.y = random.randint(0, 480)
                    monster_life = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.speed_y = 0
                elif event.key == pygame.K_s:
                    hero.speed_y = 0
                elif event.key == pygame.K_a:
                    hero.speed_x  = 0
                elif event.key == pygame.K_d:
                    hero.speed_x = 0
                elif event.key == pygame.K_RETURN:
                    monster_life = True

                #hero catches monster
            if math.sqrt(((hero.x - monster.x)**2) + ((hero.y - monster.y)**2)) < 32:
                monster_life = False
                win_img = True
                pygame.mixer.music.load('sounds/win.wav')
                pygame.mixer.music.play(1)








            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        hero.move()
        monster.move_enemy()
        goblin.move_enemy()

        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_image, (hero.x, hero.y))
        screen.blit(goblin_image, (goblin.x, goblin.y))
        if monster_life is True:
            screen.blit(monster_image, (monster.x, monster.y))
        if win_img is True:
            screen.blit(play_again_img, (125, 240))
        pygame.display.update()
        clock.tick(60)


    pygame.quit()

if __name__ == '__main__':
    main()
