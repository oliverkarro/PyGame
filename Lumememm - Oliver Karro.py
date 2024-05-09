import pygame # Impordime pygame teegi, et kasutada graafikatöötluse funktsioone.
pygame.init() # Initsialiseerime pygame'i, et valmistada ette graafiliste elementide kasutamine.

screen = pygame.display.set_mode([300,300]) # Loome 300x300 pikslise ekraani.
pygame.display.set_caption("Lumemees - Oliver Karro") # Määrame akna pealkirjaks "Lumemees - Oliver Karro".

# Joonistame lumememme osi ükshaaval
pygame.draw.circle(screen, [255, 255, 255], [150,200], 50, 100) # Lumememme ülemine osa.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

pygame.draw.circle(screen, [255, 255, 255], [150,125], 40, 100) # Lumememme keskmine osa.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

pygame.draw.circle(screen, [255, 255, 255], [150,60], 30, 100) # Lumememme alumine osa.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

# Joonistame lumememme silmad ja nina
pygame.draw.circle(screen, [255, 0, 0], [150,75], 10, 10) # Punane nina.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

pygame.draw.circle(screen, [0, 0, 0], [135,60], 10, 5) # Vasak silm.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

pygame.draw.circle(screen, [0, 0, 0], [165,60], 10, 5) # Parem silm.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

running = True
try:
    while running: # Loome while-tsükli, mis kestab seni, kuni running on True.
        for event in pygame.event.get(): # Tsükkel, mis kontrollib kõiki pygame'i poolt tekitatud sündmusi.
            if event.type == pygame.QUIT: # Kui kasutaja üritab akent sulgeda...
                running = False # ...seadistame running muutuja False'iks, et tsükkel lõpetada.
    pygame.quit() # Lõpetame pygame'i kasutamise.
except SystemExit: # Kui süsteemist tuleb väljumissignaal...
    pygame.quit() # ...lõpetame pygame'i kasutamise.
