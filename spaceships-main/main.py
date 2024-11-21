import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 700))
ship1 = pygame.image.load("ship1.png")
ship1 = pygame.transform.scale(ship1,(100,70))
ship1 = pygame.transform.rotate(ship1,270)
ship2 = pygame.image.load("ship2.png")
ship2 = pygame.transform.scale(ship2,(100,70))
ship2 = pygame.transform.rotate(ship2,90)
background = pygame.image.load("background.png")
border = pygame.Rect(500,0, 10,700)
class Spaceship(pygame.sprite.Sprite):
       def __init__(self, x, y, colour):
        super().__init__()
        if colour == "yellow":
            self.image = ship2
        elif colour == "red":
            self.image = ship1
        self.colour = colour
        self.rect = self.image.get_rect()
        self.rect.topleft = x,y
        self.health = 100
       def update(self,key_pressed):
           if self.colour == "yellow":
               if key_pressed[pygame.K_w]and self.rect.y>10:
                   self.rect.y -= 5
               if key_pressed[pygame.K_a]and self.rect.x>75:
                   self.rect.x -= 5
               if key_pressed[pygame.K_s]and self.rect.y<625:
                   self.rect.y += 5
               if key_pressed[pygame.K_d]and self.rect.x<450:
                   self.rect.x += 5
           if self.colour == "red":
               if key_pressed[pygame.K_UP]and self.rect.y>10:
                   self.rect.y -= 5
               if key_pressed[pygame.K_LEFT]and self.rect.x>550:
                   self.rect.x -= 5
               if key_pressed[pygame.K_DOWN]and self.rect.y<625:
                   self.rect.y += 5
               if key_pressed[pygame.K_RIGHT]and self.rect.x<950:
                   self.rect.x += 5
                    
    
red_ship = Spaceship(725,350, "red")
yellow_ship = Spaceship(225,350, "yellow")
spaceships = pygame.sprite.Group()                     
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill("light pink")
    screen.blit(background, (0,0))
    screen.blit(red_ship.image, red_ship.rect.topleft)
    screen.blit(yellow_ship.image, yellow_ship.rect.topleft)
    key_pressed = pygame.key.get_pressed()
    red_ship.update(key_pressed)
    yellow_ship.update(key_pressed)
    pygame.draw.rect(screen, "yellow", border)
    pygame.display.update()
