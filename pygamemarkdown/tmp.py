import pygame
pygame.init()
screen = pygame.display.set_mode((600, 900))
pygame.display.get_surface().fill((200, 200, 200))
# Fonts
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
text_surface = my_font.render('Some Text', False, (0, 0, 0))
text_surface2 = my_font.render(u'\u2022 BulletPoint', False, (0, 0, 0))
# Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(text_surface, (10, 0))
    screen.blit(text_surface2, (10, 50))
    pygame.display.flip()