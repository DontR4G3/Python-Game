__author__ = 'Jack Gerulskis'
# testing purposes
from TileControl import *
from Players import *
from Client import *

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
6666666122222111116666666
6666666611111111166666666
6666666611111111166666666
6666666661111111666666666
6666666666611166666666666
6666666666661666666666666
6666666666661116666666666
6666666666666116666666666"""
map1 = Printer.print(level, screen, b, False)
# testing

#player creation
p_1 = Player(1,0,0, "player_image.png")
p_2 = Player(100,0,1, "player_image.png")
p_3 = Player(0,100,2, "player_image.png")
p_4 = Player(100,100,3, "player_image.png")
all_p = Players([p_1, p_2, p_3, p_4])
player_coords = [p_1.get_player(), p_2.get_player(), p_3.get_player(), p_4.get_player()]

client = Client()

all_p = Players([p_1, p_2, p_3, p_4])

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
    #change player on diff computers
    p_1.update_player(speed_x, speed_y)
    #player_x += speed_x
    #player_y += speed_y
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

    screen.blit(map1, screen.get_rect())
    pygame.draw.rect(screen, (255, 0, 0), rect)
    Printer.print_players(all_p, screen)
    client.get_data(all_p, p_1.get_player())
    #change for diff player
    #client.get_data(all_p, p_2.get_player())
    pygame.display.update()
    clock.tick(100)

