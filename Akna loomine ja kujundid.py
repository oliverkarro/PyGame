import pygame
pygame.init()
# Importeerib pygame'i ja käivitab selle.

#ekraani seaded
screen=pygame.display.set_mode([640,480])
# Loob ekraani mõõtudega 640x480 pikslit.
pygame.display.set_caption("My Screen")
# Määrab akna pealkirja "My Screen".
screen.fill([204, 255, 255])
# Täidab ekraani värvi [204, 255, 255] (helesinine).

#joonistamine
pygame.draw.line(screen, [255,0,0], [100,100], [200,200], 2)
# Joonistab punase joone punktist (100, 100) punkti (200, 200) paksusega 2 pikslit.

pygame.draw.rect(screen, [0, 225, 0], [50, 80, 200, 300], 2)
# Joonistab rohelise nelinurga (rööpküliku) asukohaga (50, 80), laiusega 200 ja kõrgusega 300 ning paksusega 2 pikslit.

pygame.draw.circle(screen, [0, 0, 255], [150,200], 100, 1)
# Joonistab sinise ringi keskpunktiga (150, 200), raadiusega 100 ja paksusega 1 piksel.

pygame.draw.polygon(screen, [255, 0, 255], [[50,50],[100,50],[100,150],[250,50],[350,250],[50,250]], 2)
# Joonistab roosa polügooni, määrates selle tipud loendina antud koordinaatidena ja paksuseks 2 pikslit.

pygame.draw.ellipse(screen, [0, 225, 0], [50, 80, 200, 300], 2)
# Joonistab rohelise ellipsi asukohaga (50, 80), laiusega 200 ja kõrgusega 300 ning paksusega 2 pikslit.

pygame.display.flip()
# Värskendab ekraani, et näidata kõiki joonistusi.

running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()
except SystemExit:
    pygame.quit()
