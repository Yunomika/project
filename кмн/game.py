# Знаю что моя игра понравится Вам, поэтому сделала Вам "start_game.bat" что бы на коротком старте запускать) 
import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
BUTTON_COLOR = (100, 149, 237)
BUTTON_HOVER_COLOR = (70, 130, 180)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FONT = pygame.font.Font(None, 36)
BACKGROUND_FONT = pygame.font.Font(None, 100)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Камень, Ножницы, Бумага")

player_rock_image = pygame.image.load('photo/player_rock.png')
player_scissors_image = pygame.image.load('photo/player_scissors.png')
player_paper_image = pygame.image.load('photo/player_paper.png')
image_names = ['photo/win1.png', 'photo/win2.png', 'photo/win3.png', 'photo/win4.png', 'photo/win5.png']
img_names = ['photo/lose1.png', 'photo/lose2.png', 'photo/lose3.png', 'photo/lose4.png', 'photo/lose5.png']

computer_rock_image = pygame.image.load('photo/computer_rock.png')
computer_scissors_image = pygame.image.load('photo/computer_scissors.png')
computer_paper_image = pygame.image.load('photo/computer_paper.png')

def draw_text(text, x, y, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def get_computer_choice():
    return random.choice(['камень', 'ножницы', 'бумага'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"
    elif (
        (user_choice == 'камень' and computer_choice == 'ножницы') or
        (user_choice == 'ножницы' and computer_choice == 'бумага') or
        (user_choice == 'бумага' and computer_choice == 'камень')
    ):
        return ""
    else:
        return ""

def draw_button(text, x, y, width, height):
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    button_rect = pygame.Rect(x, y, width, height)

    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, button_rect)
        if mouse_click[0]:
            return True
    else:
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect)

    draw_text(text, x + (width - FONT.size(text)[0]) // 2, y + (height - FONT.size(text)[1]) // 2, FONT, WHITE)
    return False

SMALL_BACKGROUND_FONT = pygame.font.Font(None, 50)

def show_menu():
   #Функция для отображения главного меню игры
    
    clock = pygame.time.Clock()  # Создаем объект для контроля частоты кадров (FPS)
    
    while True:  # Начинаем бесконечный цикл для отображения меню
        screen.fill(WHITE)  # Заполняем экран белым цветом для очистки предыдущих отрисовок

        # Отображаем заголовок игры по центру экрана
        draw_text(
            "Камень, Ножницы, Бумага",  # Текст заголовка
            WIDTH // 2 - SMALL_BACKGROUND_FONT.size("Камень, Ножницы, Бумага")[0] // 2,  # Вычисляем x-координату для центрирования текста
            HEIGHT // 4,  # y-координата
            SMALL_BACKGROUND_FONT,  # Шрифт для текста
            BLACK  # Цвет текста
        )

        # Проверяем нажатие кнопки Играть
        if draw_button("Играть", WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 60):  
            play_game()  # Если кнопка нажата вызываем функцию для начала игры
        
        # Проверяем нажатие кнопки Правила
        if draw_button("Правила", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 60):  
            show_rules()  # Если кнопка нажата показываем правила игры

        # Проверяем нажатие кнопки Выход
        if draw_button("Выход", WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 60):  
            exit_game()  # Если кнопка нажата выходим из игры

        # Обрабатываем события Pygame
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  # Если событие - закрытие окна
                pygame.quit()  # Завершаем Pygame
                sys.exit()  # Выходим из программы

        pygame.display.flip()  # Обновляем экран чтобы отобразить все изменения
        clock.tick(FPS)  # Ограничиваем частоту кадров до заданного значения FPS


def exit_game():
    sys.exit()

def show_rules():
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)
        draw_text("Правила:", WIDTH // 2 - BACKGROUND_FONT.size("Правила:")[0] // 2, HEIGHT // 4, BACKGROUND_FONT, BLACK)
        draw_text("1. Камень бьет Ножницы", WIDTH // 2 - FONT.size("1. Камень бьет Ножницы")[0] // 2, HEIGHT // 4 + 100, FONT, BLACK)
        draw_text("2. Ножницы бьют Бумагу", WIDTH // 2 - FONT.size("2. Ножницы бьют Бумагу")[0] // 2, HEIGHT // 4 + 140, FONT, BLACK)
        draw_text("3. Бумага бьет Камень", WIDTH // 2 - FONT.size("3. Бумага бьет Камень")[0] // 2, HEIGHT // 4 + 180, FONT, BLACK)
        draw_text("Нажмите ESC для возврата в меню", WIDTH // 2 - FONT.size("Нажмите ESC для возврата в меню")[0] // 2, HEIGHT // 4 + 300, FONT, BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  
                    return

        pygame.display.flip()
        clock.tick(FPS)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!", 0
    elif ((user_choice == "камень" and computer_choice == "ножницы") or 
         (user_choice == "ножницы" and computer_choice == "бумага") or 
         (user_choice == "бумага" and computer_choice == "камень")):
        return "Вы выиграли!", 1
    else:
        return "Компьютер выиграл!", -1

def draw_text(text, x, y, font, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

current_image_index = 0

def play_game():
    clock = pygame.time.Clock()
    user_score = 0
    computer_score = 0
    user_choice = None
    computer_choice = None
    result_text = ""
    
    lose_images = [pygame.image.load(name) for name in img_names]
    random.shuffle(img_names)
    
    win_images = [pygame.image.load(name) for name in image_names]
    random.shuffle(image_names)

    replay_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 170, 210, 50)
    exit_button_rect = pygame.Rect(WIDTH // 2 - 90, HEIGHT // 2 + 220, 190, 50)

    game_over = False  

    while True: 
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_1:
                    user_choice = 'камень'
                elif event.key == pygame.K_2:
                    user_choice = 'ножницы'
                elif event.key == pygame.K_3:
                    user_choice = 'бумага'

                if user_choice:
                    computer_choice = get_computer_choice()
                    result_text, score_change = determine_winner(user_choice, computer_choice)

                    if score_change == 1:
                        user_score += 1
                    elif score_change == -1:
                        computer_score += 1

            if game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if replay_button_rect.collidepoint(mouse_pos):
                        play_game()
                    elif exit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()

        if not game_over:
            draw_text("Выберите: 1 - Камень, 2 - Ножницы, 3 - Бумага", 50, 50, FONT, BLACK)
            draw_text(f"Счет: Компьютер {computer_score} - {user_score} Вы", 200, 100, FONT, BLACK)

            if computer_choice:
                draw_text(f"Компьютер выбрал: {computer_choice}", 50, 150, FONT, BLACK)
                draw_text(f"Вы выбрали: {user_choice}", 50, 200, FONT, BLACK)

                draw_text(result_text, WIDTH // 2 - FONT.size(result_text)[0] // 2, HEIGHT // 2 - 50, FONT, BLACK)

                if computer_choice == 'камень':
                    screen.blit(computer_rock_image, (50, HEIGHT // 2 + 20))
                elif computer_choice == 'ножницы':
                    screen.blit(computer_scissors_image, (50, HEIGHT // 2 + 20))
                elif computer_choice == 'бумага':
                    screen.blit(computer_paper_image, (50, HEIGHT // 2 + 20))
                
                if user_choice == 'камень':
                    screen.blit(player_rock_image, (WIDTH - player_rock_image.get_width() - 50, HEIGHT // 2 + 20 + 40))
                elif user_choice == 'ножницы':
                    screen.blit(player_scissors_image, (WIDTH - player_scissors_image.get_width() - 50, HEIGHT // 2 + 20 + 40))
                elif user_choice == 'бумага':
                    screen.blit(player_paper_image, (WIDTH - player_paper_image.get_width() - 50, HEIGHT // 2 + 20 + 40))

            if user_score >= 3 or computer_score >= 3:
                game_over = True
                winner_text = "Вы выиграли!" if user_score >= 3 else "Компьютер выиграл!"
                draw_text(winner_text, WIDTH // 2 - FONT.size(winner_text)[0] // 2, HEIGHT // 4 - 50, FONT, BLACK)

                if computer_score >= 3:
                    lose_image = lose_images[current_image_index]
                    lose_image_rect = lose_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
                    screen.blit(lose_image, lose_image_rect)
                if user_score >= 3:
                      win_image = win_images[current_image_index]
                      win_image_rect = win_image.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
                      screen.blit(win_image, win_image_rect)

                pygame.draw.rect(screen, GREEN, replay_button_rect)
                draw_text("Сыграть ещё раз", replay_button_rect.x + 0, replay_button_rect.y + 10, FONT, WHITE)

                pygame.draw.rect(screen, RED, exit_button_rect)
                draw_text("Выход", exit_button_rect.x + 20, exit_button_rect.y + 10, FONT, WHITE)

            pygame.display.flip()
            clock.tick(FPS)



if __name__ == "__main__":
    show_menu()
