import pygame
import random
import time
import sys
import area
import math
pygame.init()

dirs = ["up", "down", "right", "left"]
screen = pygame.display.set_mode((1200, 1200))
clock = pygame.time.Clock()
running = True
col = "black"
puth = "images"
speed = 50
dino_speed = 50
status = "menu"
var = 1
score = 0
count = 1
pos = [550, 500]
pos_mat = [10, 11]
last_direction = ""
k = 0
board = area.board1
area_color = "blue"
dino = {
    "pos": [[50, 50], [50, 950], [950, 950], [950, 50]],
    "pos_mat": [[1, 1], [1, 19], [19, 19], [19, 1]],
    "color": ["Blue", "Orange", "Pink", "Red"],
    "dir_dino": ["up", "down", "left", "right"],
}

def regul(dino: dict):
    for i in range(4):
        dino["pos_mat"][i][0] = dino["pos"][i][0] // 50
        dino["pos_mat"][i][1] = dino["pos"][i][1] // 50


def rand_dir():
    global dino
    dir = []
    for i in range(4):
        if board[dino["pos_mat"][i][0]][dino["pos_mat"][i][1] - 1] != 0:
            dir.append("up")
        if board[dino["pos_mat"][i][0]][dino["pos_mat"][i][1] + 1] != 0:
            dir.append("down")
        if board[dino["pos_mat"][i][0] + 1][dino["pos_mat"][i][1]] != 0:
            dir.append("right")
        if board[dino["pos_mat"][i][0] - 1][dino["pos_mat"][i][1]] != 0:
            dir.append("left")
    for i in range(4):
        dino["dir_dino"][i] = (dir[random.randint(0, len(dir) - 1)])


def drow_menu(scereen):
    global icon, copyright, new_game, about, maps, slaq
    screen.fill("black")
    icon = pygame.image.load(puth + f"/pacman.png")
    copyright = pygame.image.load(puth + f"/copyright.png")
    new_game = pygame.image.load(puth + f"/New Game/newgame.png")
    about = pygame.image.load(puth + f"/About/about.png")
    maps = pygame.image.load(puth + f"/Maps/maps.png")


def draw_area(screen):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] != 0):
                rec = pygame.Rect(i * 50, j * 50, 50, 50)
                pygame.draw.rect(screen, area_color, rec)


def draw_pacman(puth: str):
    global count, last_direction, var
    count = (count + 1) % 8
    if count % 8 <= 3:
        if last_direction == "left":
            obj = pygame.image.load(puth + f"/pacs/pacman_left1.png")        
        else:
            obj = pygame.image.load(puth + f"/pacs/pacman_right1.png")
    else:
        if last_direction == "left":
            obj = pygame.image.load(puth + f"/pacs/pacman_left-1.png")
        
        else:
            obj = pygame.image.load(puth + f"/pacs/pacman_right-1.png")
    if last_direction == "down":
        obj = pygame.transform.rotate(obj, -90)
        
    elif last_direction == "up":
        obj = pygame.transform.rotate(obj, 90)
    elif last_direction == "left":
        obj = pygame.transform.rotate(obj, 0)

    screen.blit(obj, (pos[0], pos[1]))


def draw_apple(puth: str):
    global score
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 1):
                obj = pygame.image.load(puth + f"/Apple/apple.png")
                screen.blit(obj, (i * 50, j * 50))


def draw_dino(dino: dict):
    global k
    k += 1
    if k % 10 == 0:
        k = 0
        rand_dir()
    for i in range(4):
        color = dino["color"][i]
        name = dino["dir_dino"][i]
        obj = pygame.image.load(f"images/Eggs/{color}_{name}.png")
        screen.blit(obj, (dino["pos"][i][0], dino["pos"][i][1]))


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        pygame.mixer.stop()
        score = 0
        count = 1
        pos = [550, 500]
        pos_mat = [10, 11]
        last_direction = ""
        k = 0
        board = area.board1

        dino = {
        "pos": [[50, 50], [50, 950], [950, 950], [950, 50]],
        "pos_mat": [[1, 1], [1, 19], [19, 19], [19, 1]],
        "color": ["Blue", "Orange", "Pink", "Red"],
        "dir_dino": ["up","left", "down",  "right"]
        }
        for i in range(len(area.board1)):
            for j in range(len(area.board1[i])):
                if area.board1[i][j] != 0:
                    area.board1[i][j] = 1
                if area.board2[i][j] != 0:
                    area.board2[i][j] = 1
                if area.board3[i][j] != 0:
                    area.board3[i][j] = 1

        k = 0
        status = "menu"

    if status == "menu":
        pygame.mixer.stop()
        score = 0
        count = 1
        pos = [550, 500]
        pos_mat = [10, 11]
        last_direction = ""
        k = 0
        board = area.board1

        dino = {
        "pos": [[50, 50], [50, 950], [950, 950], [950, 50]],
        "pos_mat": [[1, 1], [1, 19], [19, 19], [19, 1]],
        "color": ["Blue", "Orange", "Pink", "Red"],
        "dir_dino": ["up","left", "down",  "right"]
        }
        for i in range(len(area.board1)):
            for j in range(len(area.board1[i])):
                if area.board1[i][j] != 0:
                    area.board1[i][j] = 1
                if area.board2[i][j] != 0:
                    area.board2[i][j] = 1
                if area.board3[i][j] != 0:
                    area.board3[i][j] = 1
#___menu___________________________________________________________________________
        drow_menu(screen)
        if pygame.mouse.get_pos()[1] < 440 and pygame.mouse.get_pos()[1] > 335:

            new_game = pygame.image.load(puth + f"/New Game/newgame_shadow.png")
            if pygame.mouse.get_pressed()[0]:
                score = 0
                status = "new game"
               
        elif pygame.mouse.get_pos()[1] > 515 and pygame.mouse.get_pos()[1] <  620:
            maps = pygame.image.load(puth + f"/Maps/maps_shadow.png")
            if pygame.mouse.get_pressed()[0]:
                status = "maps"
        elif pygame.mouse.get_pos()[1] > 680 and pygame.mouse.get_pos()[1] <  780:
            about = pygame.image.load(puth+ f"/About/about_shadow.png")
            if pygame.mouse.get_pressed()[0]:
                status = "about"
 
        screen.blit(icon, (275, 50))
        screen.blit(copyright, (375, 950))
        screen.blit(new_game, (190, 330))
        screen.blit(maps, (415, 510))
        screen.blit(about, (350, 675))
    #________________________________________________________________________________

    if status == "new game":
        
        pygame.mixer.music.load("music/dino.mp3")
        pygame.mixer.music.play(1)
        screen.fill("black")
        draw_area(screen)
        draw_apple(puth)
        draw_pacman(puth)
        draw_dino(dino)
        font = pygame.font.Font('freesansbold.ttf', 75)
        text = font.render(f"{score - 1}", True, "white", "black")
        textRect = text.get_rect()
        textRect.center = (750, 180)
        screen.blit(text, textRect)
        sco = pygame.image.load(puth + f"/Score/score.png")
        screen.blit(sco, (420, 150))
        for i in range(4):
            if math.sqrt((pos[0] - dino["pos"][i][0]) ** 2 + (pos[1] - dino["pos"][i][1]) ** 2)  < 50:
                pygame.mixer.music.load("music/game_over.mp3")
                pygame.mixer.music.play(0)
                status = "game_over"
        if pos_mat in dino["pos_mat"] or pos in dino["pos"]:
            pygame.mixer.music.load("music/game_over.mp3")
            pygame.mixer.music.play(0)
            status = "game_over"
        if True:
            if True:
                if pygame.key.get_pressed()[pygame.K_UP]:
                    if board[pos_mat[0]][pos_mat[1] - 1] != 0:
                        last_direction = "up"
                elif pygame.key.get_pressed()[pygame.K_DOWN]:
                    if board[pos_mat[0]][pos_mat[1] + 1]:
                        last_direction = "down"
                elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                    if board[pos_mat[0] + 1][pos_mat[1]] != 0:
                        last_direction = "right"
                elif pygame.key.get_pressed()[pygame.K_LEFT]:
                    if board[pos_mat[0] - 1][pos_mat[1]] != 0:
                        last_direction = "left"
# ______pacMan_________________________________________________________________
            if True:
                if last_direction == "up":
                    if board[pos_mat[0]][pos_mat[1] - 1] != 0 or pos[1] % 50 != 0:
                        pos[1] -= speed

                elif last_direction == "right":
                    if board[pos_mat[0] + 1][pos_mat[1]] != 0 or pos[0] % 50 != 0:
                        pos[0] += speed

                elif last_direction == "down":
                    if board[pos_mat[0]][pos_mat[1] + 1] != 0 or pos[1] % 50 != 0:
                        pos[1] += speed

                elif last_direction == "left":
                    if board[pos_mat[0] - 1][pos_mat[1]] != 0 or pos[0] % 50 != 0:
                        pos[0] -= speed
# ______dino___________________________________________________________________
            if True:
                for i in range(4):
                    if dino["dir_dino"][i] == "up":
                        if board[dino["pos_mat"][i][0]][dino["pos_mat"][i][1] - 1] != 0 or dino["pos"][i][1] % 50 != 0:
                            dino["pos"][i][1] -= dino_speed

                    elif dino["dir_dino"][i] == "right":
                        if board[dino["pos_mat"][i][0] + 1][dino["pos_mat"][i][1]] != 0 or dino["pos"][i][0] % 50 != 0:
                            dino["pos"][i][0] +=  dino_speed

                    elif dino["dir_dino"][i] == "down":
                        if board[dino["pos_mat"][i][0]][dino["pos_mat"][i][1] + 1] != 0 or dino["pos"][i][1] % 50 != 0:
                            dino["pos"][i][1] +=  dino_speed

                    elif dino["dir_dino"][i] == "left":
                        if board[dino["pos_mat"][i][0] - 1][dino["pos_mat"][i][1]] != 0 or dino["pos"][i][0] % 50 != 0:
                            dino["pos"][i][0] -=  dino_speed
# _____________________________________________________________________________

        pos_mat[0] = pos[0] // 50
        pos_mat[1] = pos[1] // 50

         

        regul(dino)
       
        if board[pos_mat[0]][pos_mat[1]] == 1:
            score += 1
            board[pos_mat[0]][pos_mat[1]] = 2   

        if score == 144:
            status = "win"
        
    if status == "maps":
        screen.fill("Black")
        copyright = pygame.image.load(puth + f"/copyright.png")
        back = pygame.image.load(puth + f"/back.png")
        screen.blit(copyright, (375, 950))
        icon = pygame.image.load(puth + f"/pacman.png")
        screen.blit(icon, (275, 100))
        area1 = pygame.image.load(puth + f"/Area/area1.png")
        area2 = pygame.image.load(puth + f"/Area/area2.png")
        area3 = pygame.image.load(puth + f"/Area/area3.png")
       
        if pygame.mouse.get_pos()[1] > 400 and  pygame.mouse.get_pos()[1] < 600 and pygame.mouse.get_pos()[0] > 200  and pygame.mouse.get_pos()[0] < 400:
            if pygame.mouse.get_pressed():
                area_color = "blue"
            area1 = pygame.image.load(puth + f"/Area/area1_shadow.png")
        if pygame.mouse.get_pos()[1] > 400 and  pygame.mouse.get_pos()[1] < 600 and pygame.mouse.get_pos()[0] > 450  and pygame.mouse.get_pos()[0] < 650:
            if pygame.mouse.get_pressed():
                area_color = "green"
            area2 = pygame.image.load(puth + f"/Area/area2_shadow.png")
        if pygame.mouse.get_pos()[1] > 400 and  pygame.mouse.get_pos()[1] < 600 and pygame.mouse.get_pos()[0] > 700  and pygame.mouse.get_pos()[0] < 900:
            if pygame.mouse.get_pressed():
                area_color = "gray"
            area3 = pygame.image.load(puth + f"/Area/area3_shadow.png")
        
        screen.blit(area1, (200, 400))
        screen.blit(area2, (450, 400))
        screen.blit(area3, (700, 400))
        if pygame.mouse.get_pos()[1] > 800 and pygame.mouse.get_pos()[0] < 200:
            back = pygame.image.load(puth + f"/back_shadow.png")

            if pygame.mouse.get_pressed()[0]:
                status = "menu"
        screen.blit(back, (20, 900))

        
        
    if status == "about":

        screen.fill("black")
        copyright = pygame.image.load(puth + f"/copyright.png")
        about_text = pygame.image.load(puth + f"/About/about_text.png")
        screen.blit(about_text, (180,150))
        screen.blit(copyright, (375, 975))
        icon = pygame.image.load(puth + f"/pacman.png")
        screen.blit(icon, (275, 30))
        back = pygame.image.load(puth + f"/back.png")
        if pygame.mouse.get_pos()[1] > 800 and pygame.mouse.get_pos()[0] < 200:
            back = pygame.image.load(puth + f"/back_shadow.png")

            if pygame.mouse.get_pressed()[0]:
                status = "menu"
        screen.blit(back, (20, 900))
    
    if status == "win":
        win = pygame.image.load(puth + f"/youwin.png")
        back = pygame.image.load(puth + f"/back.png")
        time.sleep(1)
        screen.fill("black")
        screen.blit(win, (280, 400))
        if pygame.mouse.get_pos()[1] > 800 and pygame.mouse.get_pos()[0] < 200:
            back = pygame.image.load(puth + f"/back_shadow.png")

            if pygame.mouse.get_pressed()[0]:
                status = "menu"
        screen.blit(back, (20, 900))

    if status == "game_over":
        screen.fill("black")
        back = pygame.image.load(puth + f"/back.png")
        game_over = pygame.image.load(puth + f"/gameover.png")
        screen.blit(game_over, (200, 400))
        if pygame.mouse.get_pos()[1] > 800 and pygame.mouse.get_pos()[0] < 200:
            back = pygame.image.load(puth + f"/back_shadow.png")

        if pygame.mouse.get_pressed()[0]:
            status = "menu"
        screen.blit(back, (20,900))
        
    pygame.display.update()
    pygame.display.flip()
    clock.tick(10) 

pygame.quit()
