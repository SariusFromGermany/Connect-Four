import pygame

#Fenster einrichten
screenheight = 600
screenwidth = 600

pygame.init()

win = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("4 Gewinnt")

win.fill((255, 255, 255))
pygame.draw.rect(win, (0, 175, 175), (0, 60, screenwidth, screenheight))

for x in range(0, 600, 80):
    for y in range(0, 600, 80):
        pygame.draw.circle(win, (255, 255, 255), (x - 25, y - 15), 25)
        
#Definitionen
def quit_button():
    run = True
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    return run

def get_xcursor():
    position = pygame.mouse.get_pos()[0]
    if position < 45:
        position  = 50
    elif position > 600:
        position = 550
       
    return position
def get_mousepress():
    pygame.event.get()
    pressed = pygame.mouse.get_pressed()[0]
    return True if pressed == 1 else False
def myround(x, base=80):
    return (base * round(x/base)) - 25


#Classes
class Stein():
    def __init__(self):
        self.game_round = 0
        self.xposition = None
        self.colour = None
        self.radius = 25

        self.places_free = {55:7, 135:7, 215:7, 295:7, 375:7, 455:7, 535:7}
        
        self.set_colour()
    def set_colour(self):   #sets the colour corresponding to the round
        if self.game_round % 2 == 0:
            self.colour = (0, 0, 255)
        else:
            self.colour = (255, 0, 0)

    def project(self):      #projecs where the stone will be 
        self.xposition = myround(get_xcursor())
        
        self.set_colour()

        pygame.draw.rect(win, (255, 255, 255), (0, 0, screenwidth, 100))
        pygame.draw.circle(win, self.colour, (self.xposition, 25), self.radius)
        
        if get_mousepress():        #checks for mousepress
            self.fall()
            
    def fall(self):

        if self.places_free[self.xposition] > 0:
            pygame.draw.circle(win, self.colour, (self.xposition, self.places_free[self.xposition] * 80 - 15), self.radius)
        
            self.places_free[self.xposition] -= 1
            self.game_round += 1

        pressed = get_mousepress()
        while pressed:                      #Safetyfeature, that the mousebutton can't be held down
            pressed = get_mousepress()
            pygame.time.delay(100)

#Variablen
game_round = 1
run = True
stein = Stein()
#Spielschleife
while run:
    run = quit_button()

    stein.project()
    
    pygame.time.delay(10)
    pygame.display.update()
pygame.quit()
