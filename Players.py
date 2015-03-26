__author__ = 'Jack Gerulskis'
#Handles player coords
import pygame

class Player:
    def __init__(self, start_x, start_y, player_id, image_url):
        self.player_coord = [start_x, start_y, player_id]
        self.image = pygame.image.load(image_url)

    def get_player(self):
        return self.player_coord

    def update_player(self, change_x, change_y):
        self.player_coord = [change_x + self.player_coord[0], change_y + self.player_coord[1], self.player_coord[2]]

    def get_x(self):
        return self.player_coord[0]

    def get_y(self):
        return self.player_coord[1]

    def get_w(self):
        return self.image.get_width()

    def get_h(self):
        return self.image.get_height()

    def get_rect(self):
        return (self.get_x(), self.get_y(), self.get_w(), self.get_h())

    def get_image(self):
        return self.image


class Players:
    def __init__(self, player_list):
        self.player_list = player_list

    def get_players(self):
        return self.player_list

    def update_players(self, players_coords_list):
        counter = 0
        for coords in players_coords_list:
            #match id's
            self.get_players()[counter].update_player(coords[0] - self.get_players()[counter].get_x(),
                                                      coords[1] - self.get_players()[counter].get_y())
            counter += 1

