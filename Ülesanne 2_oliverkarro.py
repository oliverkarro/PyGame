import pygame # Impordime pygame teegi, et kasutada graafikatöötluse funktsioone.
pygame.init() # Initsialiseerime pygame'i, et valmistada ette graafiliste elementide kasutamine.

# Ekraani seaded
screen = pygame.display.set_mode([640,480]) # Loome 640x480 pikslise ekraani.
pygame.display.set_caption("Ülesanne 2") # Määrame akna pealkirjaks "Ülesanne 2".

# Lisame taustapildi
bg = pygame.image.load("bg_shop.jpg") # Laeme taustapildi "bg_shop.jpg".
screen.blit(bg,[0,0]) # Kuvame taustapildi (0,0) koordinaatidega.

# Lisame müüja pildi
seller = pygame.image.load("seller.png") # Laeme müüja pildi "seller.png".
seller = pygame.transform.scale(seller, [224, 264]) # Muudame müüja pildi suurust 224x264 pikslisteks.
screen.blit(seller,[140,180]) # Kuvame müüja pildi (140,180) koordinaatidega.

# Lisame vestluse pildi
chat = pygame.image.load("chat.png") # Laeme vestluse pildi "chat.png".
chat = pygame.transform.scale(chat, [250, 190]) # Muudame vestluse pildi suurust 250x190 pikslisteks.
screen.blit(chat,[260,75]) # Kuvame vestluse pildi (260,75) koordinaatidega.

# Lisame teksti
font = pygame.font.Font(None, 25) # Määrame fondi suuruseks 25.
text = font.render("Tere, olen Oliver Karro", True, [255,255,255]) # Loome teksti "Tere, olen Oliver Karro".
screen.blit(text, [280,150]) # Kuvame teksti (280,150) koordinaatidega.

# Lisame Vikk logo
vikk = pygame.image.load("vikk.png") # Laeme Vikk logo "vikk.png".
vikk = pygame.transform.scale(vikk, [267, 35]) # Muudame Vikk logo suurust 267x35 pikslisteks.
screen.blit(vikk,[0,0]) # Kuvame Vikk logo (0,0) koordinaatidega.

# Lisame mõõga pildi
mõõk = pygame.image.load("Mõõk.png") # Laeme mõõga pildi "Mõõk.png".
mõõk = pygame.transform.scale(mõõk, [100, 82]) # Muudame mõõga pildi suurust 100x82 pikslisteks.
screen.blit(mõõk,[530,180]) # Kuvame mõõga pildi (530,180) koordinaatidega.

# Lisame tordi pildi
tort = pygame.image.load("tort.png") # Laeme tordi pildi "tort.png".
tort = pygame.transform.scale(tort, [100, 82]) # Muudame tordi pildi suurust 100x82 pikslisteks.
screen.blit(tort,[400,215]) # Kuvame tordi pildi (400,215) koordinaatidega.

# Lisame kaarega teksti "TULEVIK 2050"
font = pygame.font.Font(None, 30) # Määrame fondi suuruseks 30.
text = font.render("TULEVIK 2050", True, [255, 255, 255]) # Loome teksti "TULEVIK 2050".
text = pygame.transform.rotate(text, 45) # Pöörame teksti 45 kraadi võrra.
screen.blit(text, [50, 50]) # Kuvame teksti (50, 50) koordinaatidega.

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
