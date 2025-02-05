import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (128, 128, 128)
        self.font = pygame.font.SysFont(None, 30)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,
                                            True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.health_image, self.health_rect)


    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Record *{:,}*".format(high_score)
        self.high_score_image = self.font.render(high_score_str,
                                                 True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        level = str(self.stats.level)
        level_str = "Level {}".format(level)
        self.level_image = self.font.render(level_str,
                                            True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        health = str(self.stats.ship_left)
        health_str = "Health {}".format(health)
        self.health_image = self.font.render(health_str,
                                            True, self.text_color, self.ai_settings.bg_color)
        self.health_rect = self.health_image.get_rect()
        self.health_rect.left = self.screen_rect.left + 20
        self.health_rect.top = 20

