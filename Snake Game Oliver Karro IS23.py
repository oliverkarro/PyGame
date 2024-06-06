import pygame  # Impordi pygame'i mängumootor
import time  # Impordi aja moodul ajaarvamiseks
import random  # Impordi random moodul juhuslike arvude genereerimiseks
import sys  # Impordi sys moodul süsteemi funktsioonidele

pygame.init()  # Initsialiseeri pygame'i mängumootor

# Defineeri mõned värvide konstandid RGB formaadis
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
colors = [black, red, green, blue, yellow]  # List värvidega mao jaoks

dis_width = 1080  # Mänguala laius pikslites
dis_height = 1080  # Mänguala kõrgus pikslites

snake_block = 20  # Iga mao bloki suurus pikslites

initial_snake_speed = 15  # Algkiirus mao liikumiseks
speed_increment = 5  # Kiiruse suurendamise samm

dis = pygame.display.set_mode((dis_width, dis_height))  # Looge mänguaken
pygame.display.set_caption('Snake Game by Oliver')  # Seadke mängu akna pealkiri

# Määra pildi suurendamise tegur
scaling_factor = 2  # Suurendage seda väärtust, et skelette suurendada

# Laadi ja suurenda pildid
skeleton_images = {
    "skeleton1": pygame.image.load("skeleton1.png"),
    "skeleton2": pygame.image.load("skeleton2.png"),
    "skeleton3": pygame.image.load("skeleton3.png"),
}

# Suurenda pilte
for skeleton_name in skeleton_images:
    skeleton_images[skeleton_name] = pygame.transform.scale(
        skeleton_images[skeleton_name],
        (int(snake_block * scaling_factor), int(snake_block * scaling_factor))
    )

# Laadi taustapilt mängu lõpus
background_image = pygame.image.load("background.png")
background_image = pygame.transform.scale(background_image, (dis_width, dis_height))

clock = pygame.time.Clock()  # Looge kell objekt mängu kiiruse kontrollimiseks

# Defineeri fondid
font_style = pygame.font.SysFont("timesnewroman", 25, bold=True)
score_font = pygame.font.SysFont("timesnewroman", 75, bold=True)

# Laadige taustamuusika
pygame.mixer.music.load("Snake.mp3")

# Laadige heliefektid
eat_sound = pygame.mixer.Sound("eatsound.mp3")
game_over_sound = pygame.mixer.Sound("gameover.mp3")

# Mängu taustamuusika mängimine
def play_music():
    pygame.mixer.music.play(-1)  # Lõpmatu muusika esitus

# Lõpeta muusika esitus
def stop_music():
    pygame.mixer.music.stop()

# Kuvage mängu lõpus skoor
def Your_score(score, color):
    value = score_font.render("Your Score: " + str(score), True, color)
    value_with_outline = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value_with_outline, [0, 0])
    dis.blit(value, [1, 1])

# Kuvage möödunud aeg mängu lõpus
def Timer(time_passed, color):
    minutes = time_passed // 60000
    seconds = (time_passed // 1000) % 60
    value = score_font.render(f"Time: {minutes:02d}:{seconds:02d}", True, color)
    value_with_outline = score_font.render(f"Time: {minutes:02d}:{seconds:02d}", True, black)
    dis.blit(value_with_outline, [0, 60])
    dis.blit(value, [1, 61])

# Kuvage madu mängu ajal
def our_snake(snake_block, snake_list, color):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

# Kuvage sõnum mängu keskel
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Looge toidu esinemine
def spawn_food(skeletons, snake_block, scaling_factor, dis_width, dis_height, double_chance=0.3):
    food = random.choice(skeletons)
    foodx = round(random.randrange(0, dis_width - snake_block * scaling_factor) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block * scaling_factor) / 10.0) * 10.0
    
    # Kontrollige, kas toidu ilmumissagedust tuleks kahekordistada
    if random.random() < double_chance:
        food_spawn_interval = 10000  # Vaikimisi ilmumissagedus
    else:
        food_spawn_interval = random.randint(10000, 15000)  # Juhuslik ilmumissagedus vahemikus 10-15 sekundit
        
    return {"type": food, "x": foodx, "y": foody, "spawn_interval": food_spawn_interval}

# Joonista mängu grid
def draw_grid():
    for x in range(0, dis_width, snake_block):
        for y in range(0, dis_height, snake_block):
            rect = pygame.Rect(x, y, snake_block, snake_block)
            pygame.draw.rect(dis, (200, 200, 200), rect, 1)  

# Mäng on läbi
def game_over():
    dis.blit(background_image, (0, 0))  # Kuvage taustapilt mängu lõpus
    message("Sa kaotasid! Vajuta C-Mängi uuesti või Q-Välju", red)  # Kuvage sõnum mängu lõpus
    pygame.display.update()  # Uuendage ekraani
    stop_music()  # Lõpeta muusika esitus  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_c:
                    gameLoop()  # Mängi uuesti


# Mängutsükkel
def gameLoop():
    global initial_snake_speed
    snake_speed = initial_snake_speed  # Määra algkiirus

    x1 = dis_width / 2  # Mao alguskoordinaadid
    y1 = dis_height / 2

    x1_change = 0  # Mao liikumise suuna muutus
    y1_change = 0

    snake_List = []  # Madu osade list
    Length_of_snake = 1  # Madu algpikkus

    current_color = random.choice(colors)  # Algne värv
    last_color_change = pygame.time.get_ticks()  # Viimane värvi muutumise aeg
    last_speed_increase = pygame.time.get_ticks()  # Viimane kiiruse suurendamise aeg
    last_food_spawn = pygame.time.get_ticks()  # Viimane toidu ilmumise aeg
    start_time = pygame.time.get_ticks()  # Mängu alguse aeg

    skeletons = list(skeleton_images.keys())  # Skelettide nimede loetelu
    foods = [spawn_food(skeletons, snake_block, scaling_factor, dis_width, dis_height) for _ in range(6)]  # Toidu loomine
    food_spawn_interval = 5000  # Toidu ilmumise vahelejätmine

    play_music()  # Mängi taustamuusikat  

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Kui madu jõuab mängu piiridesse, mäng läbi
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over()
            return
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)  # Täida mänguala valge värviga
        
        draw_grid()  # Joonista mängu ruudustik

        current_time = pygame.time.get_ticks()
        # Kui toit on aegunud ja toite on vähem kui 6, siis loo uus toit
        if current_time - last_food_spawn > food_spawn_interval and len(foods) < 6:  
            foods.append(spawn_food(skeletons, snake_block, scaling_factor, dis_width, dis_height, double_chance=0.5))  
            last_food_spawn = current_time

        food_rects = []
        for food in foods:
            dis.blit(skeleton_images[food["type"]], (food["x"], food["y"]))
            food_rects.append(pygame.Rect(food["x"], food["y"], int(snake_block * scaling_factor), int(snake_block * scaling_factor)))
        
        snake_head_rect = pygame.Rect(x1, y1, snake_block, snake_block)
        
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Kui madu põrkab endaga kokku, mäng läbi
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over()
                return

        # Iga 5 sekundi järel muutke madu värvi
        if current_time - last_color_change > 5000:
            current_color = random.choice(colors)
            last_color_change = current_time

        # Iga 15 sekundi järel suurendage madu kiirust
        if current_time - last_speed_increase > 15000:
            snake_speed += speed_increment
            last_speed_increase = current_time

        # Kuvage madu
        our_snake(snake_block, snake_List, current_color)
        Your_score(Length_of_snake - 1, current_color)  # Kuvage skoor
        Timer(current_time - start_time, current_color)  # Kuvage möödunud aeg

        pygame.display.update()  # Uuendage ekraani

        # Kontrollige, kas madu on söönud toitu
        for food in foods:
            food_rect = pygame.Rect(food["x"], food["y"], int(snake_block * scaling_factor), int(snake_block * scaling_factor))
            if snake_head_rect.colliderect(food_rect):
                foods.remove(food)
                Length_of_snake += 1
                food_spawn_interval = max(500, food_spawn_interval / 2)  # Vähendage toidu ilmumise vahelejätmist
                eat_sound.play()  # Mängige söömise heliefekti

        clock.tick(snake_speed)  # Kontrolli mängu kiirust

gameLoop()  # Käivita mängutsükkel
