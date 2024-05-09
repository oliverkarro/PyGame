import pygame # Impordime pygame teegi, et kasutada graafikatöötluse funktsioone.
pygame.init() # Initsialiseerime pygame'i, et valmistada ette graafiliste elementide kasutamine.

# Ekraani seaded
screen = pygame.display.set_mode([640,480]) # Loome 640x480 pikslise ekraani.
pygame.display.set_caption("Harjutamine") # Määrame akna pealkirjaks "Harjutamine".
screen.fill([204, 255, 204]) # Täidame ekraani värviga [204, 255, 204] (hele roheline).

# Lisame pildid
bg = pygame.image.load("youwin.jpg") # Laeme taustapildi "youwin.jpg".
screen.blit(bg,[0,0]) # Kuvame taustapildi (0,0) koordinaatidega.

trophy = pygame.image.load("trophy.png") # Laeme trofee pildi "trophy.png".
trophy = pygame.transform.scale(trophy, [300, 200]) # Muudame trofee pildi suurust 300x200 pikslisteks.
screen.blit(trophy,[180,50]) # Kuvame trofee pildi (180,50) koordinaatidega.

pygame.display.flip() # Värskendame ekraani, et näidata kõiki joonistusi.

running = True
try:
    while running: # Loome while-tsükli, mis kestab seni, kuni running on True.
        for event in pygame.event.get(): # Tsükkel, mis kontrollib kõiki pygame'i poolt tekitatud sündmusi.
            if event.type == pygame.QUIT: # Kui kasutaja üritab akent sulgeda...
                running = False # ...seadistame running muutuja False'iks, et tsükkel lõpetada.
    pygame.quit() # Lõpetame pygame'i kasutamise.
except SystemExit: # Kui süsteemist tuleb väljumissignaal...
    pygame.quit() # ...lõpetame pygame'i kasutamise.
