import pygame

#Fenster einrichten
screenheight = 600
screenwidth = 600

pygame.init()

win = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("4 Gewinnt")

background = pygame.transform.scale(pygame.image.load("leeres Spiel.gif"), (600, 550))

win.fill((255, 255, 255))
win.blit(background, (0,50))


#Definitionen
def quit_button():
    run = True
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    return run

def get_cursor():
    position = pygame.mouse.get_pos()[0]
    return position

def myround(x, base=75):
    return base * round(x/base)


#Classes
class Stein():
    def __init__(self):
        self.game_round = 0
        self.position = None
        self.colour = None
        self.radius = 25
        
        self.set_colour()
    def set_colour(self):
        if self.game_round % 2 == 1:
            self.colour = (0, 0, 255)
        else:
            self.colour = (255, 0, 0)

    def project(self):
        self.position = myround(get_cursor())
        pygame.draw.rect(win, (255, 255, 255), (0, 0, screenwidth, 50))
        pygame.draw.circle(win, self.colour, (self.position, 25), self.radius)

    def update_round(self, game_round):
        self.game_round = game_round

#Variablen
game_round = 1
run = True
stein = Stein()
stein.update_round(game_round)
#Spielschleife
while run:

    run = quit_button()

    stein.project()
    pygame.display.update()
pygame.quit()
