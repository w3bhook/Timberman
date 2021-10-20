import pygame, os, time

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1020
#SCREEN_WIDTH = 640
#SCREEN_HEIGHT = 480

def rot_center(image, angle):
    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

class Lumberjack(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Lumberjack, self).__init__()
        self.image = pygame.image.load(os.path.join('res', 'lumberjack-001.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (526, 526))
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        pass

    def kill(self):
        pygame.sprite.Sprite.kill(self)

class Axe(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Axe, self).__init__()
        self.image = pygame.image.load(os.path.join('res', 'axe-001.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (256, 256))
        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def update(self, direction):
        pass

    def kill(self):
        pygame.sprite.Sprite.kill(self)

class Button(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Button, self).__init__()
        global button_rect
        self.image = pygame.image.load(os.path.join('res', 'button-start.png'))
        self.image = pygame.transform.scale(self.image, (700, 350))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        button_rect = self.rect

    def update(self):
        pass

    def kill(self):
        pygame.sprite.Sprite.kill(self)

pygame.init()

bg = pygame.image.load(os.path.join('res', 'bg.png'))
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Timberman [DEMASTERED]")

left = True
right = False

lumberjack_left = Lumberjack((300, 750))
lumberjack_right = Lumberjack((1600, 750))
axe_left = Axe((500, 700))
axe_right = Axe((1450, 700))
start_button = Button((960, 510))
group = pygame.sprite.Group()
group.add(start_button)
menu = True

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if button_rect.collidepoint(x, y):
                start_button.kill()
                menu = False

        if menu == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_LEFT:
                    axe_right.kill()
                    lumberjack_right.kill()
                    axe_left.kill()
                    lumberjack_left.kill()
                    group.add(lumberjack_left, axe_left)

                if event.key == pygame.K_r or event.key == pygame.K_RIGHT:
                    axe_left.kill()
                    lumberjack_left.kill()
                    axe_right.kill()
                    lumberjack_right.kill()
                    group.add(lumberjack_right, axe_right)

    screen.blit(bg, (0, 0))
    group.draw(screen)
    pygame.display.flip()

pygame.quit()