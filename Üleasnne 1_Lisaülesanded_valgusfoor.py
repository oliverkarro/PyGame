import pygame # Impordime pygame teegi, et kasutada graafikatöötluse funktsioone.
pygame.init() # Initsialiseerime pygame'i, et valmistada ette graafiliste elementide kasutamine.

screen = pygame.display.set_mode([300,600]) # Loome 300x600 pikslise ekraani.
pygame.display.set_caption("Valgusfoor - Oliver Karro") # Määrame akna pealkirjaks "Valgusfoor - Oliver Karro".

# Joonistame valgusfoori kasti
pygame.draw.rect(screen, [150, 150, 150], [100, 25, 100, 250], 2) # Valgusfoori kasti joonistamine.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

# Joonistame alumise valgusfoori ringi (roheline)
pygame.draw.circle(screen, [80, 200, 120], [150,230], 35, 90) # Alumise ringi joonistamine.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

# Joonistame keskmise valgusfoori ringi (kollane)
pygame.draw.circle(screen, [255, 255, 0], [150,145], 35, 90) # Keskmise ringi joonistamine.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

# Joonistame valgusfoori posti aluse
pygame.draw.polygon(screen, [255, 255, 255], [(110, 590), (150, 500), (190, 590)]) # Posti aluse joonistamine.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

# Joonistame ülemise valgusfoori ringi (punane)
pygame.draw.circle(screen, [255, 0, 0], [150,60], 35, 90) # Ülemise ringi joonistamine.
pygame.display.flip() # Värskendame ekraani, et näidata joonistust.

# Joonistame valgusfoori posti
pygame.draw.rect(screen, [255, 255, 255], [130, 275, 40, 280]) # Posti joonistamine.
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
