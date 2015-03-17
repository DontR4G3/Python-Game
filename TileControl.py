__author__ = 'Jack Gerulskis'
# Version  V1.1
#
# Start Date: March 1st, 2015
# End Date: Still in progress
#
# Description: Ultimate tile mapping engine
#
# Capabilities: Set list of a tiles and a second list of tile properties if desired.
# Has built in debugger to eliminate logic errors. Tile Properties go as following,
# 0 means tile is permeable, 1 means solid, 2 is special tile like an exit or
# checkpoint.
#
# Made by: Jack Gerulskis

import pygame


class Tiles:

    # init this sexy code
    def __init__(self, tile_width , tile_height, image_width, image_height, file_url, debug):
        self.tiles = []

        self.whole_image = pygame.image.load(file_url)

        # tile properties
        self.tile_w = tile_width
        self.tile_h = tile_height
        self.whole_image_w = image_width
        self.whole_image_h = image_height

        # count tiles in row
        self.row_tiles = int(self.whole_image_w / self.tile_w)
        # count tiles in col
        self.col_tiles = int(self.whole_image_h / self.tile_h)

        # for testing purposes
        self.debug = debug

        if self.debugger() or debug == False:
            self.init_tiles()

    # sets all tiles to position in array
    def init_tiles(self):

        cur_y = 0
        cur_x = 0
        iteration_counter = 0
        row_tiles = int(self.whole_image_w / self.tile_w)
        col_tiles = int(self.whole_image_h / self.tile_h)

        for i in range(0, col_tiles, 1):
            for j in range(0, row_tiles, 1):
                chop_rect = (cur_x, cur_y, self.tile_w, self.tile_h)
                if self.debug:
                    print("Tile " + str(iteration_counter) + " Rect: " + str(chop_rect))
                subsurface = self.whole_image.subsurface(chop_rect)
                self.tiles.append(subsurface)
                cur_x += self.tile_w
                iteration_counter += 1
            if self.debug:
                print("Next Row")
            cur_x = 0
            cur_y += self.tile_h

    # returns true if program is all set to run
    def debugger(self):
        if self.debug:
            print("There are " + str(self.row_tiles) + " row tiles")
            print("There are " + str(self.col_tiles) + " col tiles")
            print("There are " + str(self.row_tiles * self.col_tiles) + " total tiles")
            if self.whole_image_w % self.tile_w:
                print("ATTRIBUTE_ERROR: can't resolve whole number for row tiles")
            elif self.whole_image_h % self.tile_h:
                print("ATTRIBUTE_ERROR: can't resolve whole number for col tiles")
            else:
                return True
        return False

    # returns tiles
    def get_tiles(self):
        return self.tiles

    def get_tile_h(self):
        return self.tile_h

    def get_tile_w(self):
        return self.tile_w

    def get_tile(self, index):
        return self.tiles[index]


class TilesProperties:
    def __init__(self, tiles):
        self.tp = []
        # every tile is permeable
        for i in range(0, len(tiles.get_tiles()), 1):
            self.tp.append(0)
        # solid rectangles set in the printer method
        self.s_rect = []
        self.sp_rect = []

    def set_tile(self, index, property):
        self.tp[index] = property

    def get_tp(self):
        return self.tp

    def get_specific_t(self, index):
        return self.tp[index]

    def get_solid_rect(self):
        return self.s_rect

    def set_solid_rect(self, rect, index):
        self.s_rect[index] = rect

    def init_solid_rect(self, rect):
        self.s_rect.append(rect)

    def get_special_rect(self):
        return self.sp_rect

    def set_special_rect(self, rect, index):
        self.sp_rect[index] = rect

    def init_special_rect(self, rect):
        self.sp_rect.append(rect)

    def solid_rec_collided(self, rect):
        if pygame.Rect(rect).collidelist(self.get_solid_rect()) != -1:
            return True
        else:
            return False

    def special_rec_collided(self, rect):
        if pygame.Rect(rect).collidelist(self.get_special_rect()) != -1:
            return True
        else:
            return False

class Printer():
    @staticmethod
    def print(s, display, tiles, tile_p):
        cur_x = 0
        cur_y = 0
        cur_index = 0
        # loop through level string
        for i in range(0, len(s.split("\n")), 1):
            for j in range(0, len(s.split("\n")[i]), 1):

                if s[cur_index:cur_index + 1:] != " ":
                    tile_index = int(s[cur_index:cur_index + 1:])
                    display.blit(tiles.get_tile(tile_index), (cur_x, cur_y))

                cur_x += tiles.get_tile_h()
                cur_index += 1
            # to account for \n
            cur_index += 1
            # reset x to the left
            cur_x = 0
            # increment y position
            cur_y += tiles.get_tile_h()

    # needs to be called first to init tile_p's solids array
    @staticmethod
    def init(s, display, tiles, tile_p, debugger):
        if debugger:
            print("\nInputted Level", end="")
            print(s)
        cur_x = 0
        cur_y = 0
        cur_index = 0
        tile_index = 0
        rec_index = 0
        spec_index = 0
        # loop through level string
        for i in range(0, len(s.split("\n")), 1):
            for j in range(0, len(s.split("\n")[i]), 1):
                if s[cur_index:cur_index + 1:] != " ":
                    tile_index = int(s[cur_index:cur_index + 1:])
                    display.blit(tiles.get_tile(int(s[cur_index:cur_index + 1:])), (cur_x, cur_y))

                # if tile is a solid
                if tile_p.get_specific_t(tile_index) == 1 and s[cur_index:cur_index + 1:].capitalize() != " ":
                    rect = (cur_x, cur_y, tiles.get_tile_w(), tiles.get_tile_h())
                    if debugger:
                        print("Solid Rect " + str(rec_index) + " : " + str(rect))
                        rec_index += 1
                    tile_p.init_solid_rect(rect)

                # if tile is special
                if tile_p.get_specific_t(tile_index) == 2 and s[cur_index:cur_index + 1:].capitalize() != " ":
                    rect2 = (cur_x, cur_y, tiles.get_tile_w(), tiles.get_tile_h())
                    if debugger:
                        print("Special Rect " + str(spec_index) + " : " + str(rect2))
                        spec_index += 1
                    tile_p.init_special_rect(rect2)

                cur_x += tiles.get_tile_h()
                cur_index += 1
            # to account for \n
            cur_index += 1
            # reset x to the left
            cur_x = 0
            # increment y position
            cur_y += tiles.get_tile_h()

# testing purposes
x = Tiles(32, 32, 96, 96, "32x32TileMap.png", False)
b = TilesProperties(x)
b.set_tile(3,1)
b.set_tile(4,1)
b.set_tile(5,1)
b.set_tile(6,1)
b.set_tile(7,1)
b.set_tile(8,2)
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tile Map Tester')
level ="""
6666666666666666666666666
6611161111111111111116666
6816111666611166666616666
6611116666611166666616666
6666616661111111666616666
6661116611111111166616666
6661666611177711166616666
6661111111707771116616666
6666666111177711111116666
6666666111111111116666666
6666666611111111166666666
6666666611111111166666666
6666666661111111666666666
6666666666611166666666666
6666666666661666666666666
6666666666661116666666666
6666666666666116666666666"""
Printer.init(level, screen, x, b, False)

# testing
player_x = 780
player_y = 580
clock = pygame.time.Clock()
rect = (player_x, player_y, 20, 20)
speed_x = 0
speed_y = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                speed_y = 1
            if event.key == pygame.K_UP:
                speed_y = -1
            if event.key == pygame.K_LEFT:
                speed_x = -1
            if event.key == pygame.K_RIGHT:
                speed_x = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                speed_y = 0
            if event.key == pygame.K_UP:
                speed_y = 0
            if event.key == pygame.K_LEFT:
                speed_x = 0
            if event.key == pygame.K_RIGHT:
                speed_x = 0

    player_x += speed_x
    player_y += speed_y
    screen.fill((0,0,0))
    rect = (player_x, player_y, 20,20)

    if b.solid_rec_collided(rect):
        player_x -= speed_x
        player_y -= speed_y
        speed_x = 0
        speed_y = 0

    if b.special_rec_collided(rect):
        player_x = 300
        player_y = 300

    Printer.print(level, screen, x, b)
    pygame.draw.rect(screen, (255, 0, 0), rect)

    pygame.display.update()

    clock.tick(100)


