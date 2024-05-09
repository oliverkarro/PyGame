import pygame

pygame.init()

screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Lumemees - Oliver Karro")

# Taustavärv
screen.fill((173, 216, 230))

# Joonistame lumememme
pygame.draw.circle(screen, [255, 255, 255], [150, 200], 50, 0)  # Keha
pygame.draw.circle(screen, [255, 255, 255], [150, 125], 40, 0)  # Ülakeha
pygame.draw.circle(screen, [255, 255, 255], [150, 60], 30, 0)  # Pea
pygame.draw.circle(screen, [255, 0, 0], [150, 75], 10, 0)  # Nupp
pygame.draw.circle(screen, [0, 0, 0], [135, 60], 10, 0)  # Vasak silm
pygame.draw.circle(screen, [0, 0, 0], [165, 60], 10, 0)  # Paremsilm

# Käed
pygame.draw.line(screen, (0, 0, 0), [120, 120], [90, 150], 5)  # Vasak käsi
pygame.draw.line(screen, (0, 0, 0), [180, 120], [210, 150], 5)  # Parem käsi

# Harja käes
pygame.draw.line(screen, (0, 0, 0), [210, 150], [200, 270], 3)  # Parema käe harja vars
pygame.draw.line(screen, (0, 0, 0), [200, 270], [220, 275], 3)  # Harja ots
pygame.draw.line(screen, (0, 0, 0), [200, 270], [180, 275], 3)
pygame.draw.line(screen, (0, 0, 0), [200, 270], [200, 290], 3)
pygame.draw.line(screen, (0, 0, 0), [200, 270], [210, 290], 3)
pygame.draw.line(screen, (0, 0, 0), [200, 270], [190, 290], 3)


# Nööbid
pygame.draw.circle(screen, (0, 0, 0), [150, 170], 5)  # Ülemine nööp
pygame.draw.circle(screen, (0, 0, 0), [150, 190], 5)  # Keskmise nööp
pygame.draw.circle(screen, (0, 0, 0), [150, 210], 5)  # Alam nööp

# Kübar/müts
pygame.draw.rect(screen, (0, 0, 0), (120, 30, 60, 20))  # Kübar

# Päike koos päikese kiirtega
pygame.draw.circle(screen, (255, 255, 0), [250, 50], 30)  # Päike
pygame.draw.line(screen, (255, 255, 0), [250, 20], [250, 80], 2)  # Päikesekiir 1
pygame.draw.line(screen, (255, 255, 0), [220, 50], [280, 50], 2)  # Päikesekiir 2
pygame.draw.line(screen, (255, 255, 0), [220, 20], [280, 80], 2)  # Päikesekiir 3
pygame.draw.line(screen, (255, 255, 0), [280, 20], [220, 80], 2)  # Päikesekiir 4

# Pilved
pygame.draw.circle(screen, (255, 255, 255), [50, 50], 20)  # Pilv 1
pygame.draw.circle(screen, (255, 255, 255), [80, 60], 30)  # Pilv 2
pygame.draw.circle(screen, (255, 255, 255), [30, 80], 25)  # Pilv 3

pygame.display.flip()

running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
except SystemExit:
    pygame.quit()
