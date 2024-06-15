import pygame

# Example file showing a basic pygame "game loop"
import pygame
import time

# pygame setup
pygame.init()

current_player = 1

screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
# Define grid parameters
grid_color = (0, 0, 0)  # black
cell_size = 50  # size of each cell in the grid
grid_size = 3  # size of the grid (3x3)

# Calculate the starting position of the grid
start_x = screen.get_width() // 2 - (cell_size * grid_size) // 2
start_y = screen.get_height() // 2 - (cell_size * grid_size) // 2

cell_states = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # initialize with 0 (no circle)

cell_colors = [[(255, 255, 255) for _ in range(grid_size)] for _ in range(grid_size)]  # initialisze with white color
pygame.display.set_caption("Tic Tac Toe")


def menu_button(string,font,  x, y, width, height, color, hover_color, action=None, clicked=False):
    mouse = pygame.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if clicked:
            if action is not None:
                action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font('freesansbold.ttf', font)
    text = font.render(string, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    screen.blit(text, text_rect)


def draw_board():

    # Draw the cells
    for x in range(grid_size):
        for y in range(grid_size):
            pygame.draw.rect(screen, cell_colors[x][y], pygame.Rect(start_x + x * cell_size, start_y + y * cell_size, cell_size, cell_size))

    # Draw the grid
    for x in range(grid_size + 1):
        pygame.draw.line(screen, grid_color, (start_x + x * cell_size, start_y), (start_x + x * cell_size, start_y + cell_size * grid_size))
    for y in range(grid_size + 1):
        pygame.draw.line(screen, grid_color, (start_x, start_y + y * cell_size), (start_x + cell_size * grid_size, start_y + y * cell_size))
    
    for x in range(grid_size):
        for y in range(grid_size):
            if cell_states[x][y] == 1:
                pygame.draw.circle(screen, (0, 0, 255), (start_x + x * cell_size + cell_size // 2, start_y + y * cell_size + cell_size // 2), (cell_size // 2) - 5)
            elif cell_states[x][y] == 2:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(start_x + x * cell_size + 5, start_y + y * cell_size + 5, cell_size - 10, cell_size - 10))


def reset_game():
    global cell_states
    cell_states = [[0 for _ in range(grid_size)] for _ in range(grid_size)]  # initialize with 0 (no circle)
    global cell_colors
    cell_colors = [[(255, 255, 255) for _ in range(grid_size)] for _ in range(grid_size)]  # initialize with white color


def single_player_game():
    reset_game()
    global current_player
    
    while True:
        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # A mouse click has occurred
                mouse_x, mouse_y = event.pos
                clicked = pygame.mouse.get_pressed()
                if start_x <= mouse_x <= start_x + cell_size * grid_size and start_y <= mouse_y <= start_y + cell_size * grid_size:
                    update_board(mouse_x, mouse_y)


        screen.fill("white")

        menu_button("Back", 10, 7.5, 7.5, 50, 25, (155, 155, 155), (125, 125, 125), main_menu, clicked)
        draw_board()
                
        pygame.display.flip()
        clock.tick(60)
   

def update_board(mouse_x, mouse_y):
    global current_player
    cell_x = (mouse_x - start_x) // cell_size
    cell_y = (mouse_y - start_y) // cell_size
    if cell_states[cell_x][cell_y] == 0:
            cell_states[cell_x][cell_y] = current_player

    current_player = 2 if current_player == 1 else 1
    

def check_winner(player):
    # Check rows
    for i in range(3):
        if cell_states[i][0] == cell_states[i][1] == cell_states[i][2] == player:
            return True
    
    # Check columns
    for i in range(3):
        if cell_states[0][i] == cell_states[1][i] == cell_states[2][i] == player:
            return True

    # Check diagonals
    if cell_states[0][0] == cell_states[1][1] == cell_states[2][2] == player:
        return True
    if cell_states[0][2] == cell_states[1][1] == cell_states[2][0] == player:
        return True

    return False


def multi_player_game():
    reset_game()
    global current_player

    while True:
        clicked = False
        if check_winner(1):
            print("Player 1 wins!")
            time.sleep(2)
            reset_game()
        elif check_winner(2):
            print("Player 2 wins!")
            time.sleep(2)
            reset_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                clicked = pygame.mouse.get_pressed()
                if start_x <= mouse_x <= start_x + cell_size * grid_size and start_y <= mouse_y <= start_y + cell_size * grid_size:
                    update_board(mouse_x, mouse_y)

        screen.fill("white")

        menu_button("Back", 10, 7.5, 7.5, 50, 25, (155, 155, 155), (125, 125, 125), main_menu, clicked)
        draw_board()

        pygame.display.flip()
        clock.tick(60)


def exit_game():
    pygame.quit()
    quit()


def main_menu():
    while True:
        clicked = False
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = pygame.mouse.get_pressed()
            
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        menu_button("Single Player", 15, 75, 40, 150, 45, (155, 155, 155), (125, 125, 125), single_player_game, clicked)
        menu_button("Multi Player", 15, 75, 95, 150, 45, (155, 155, 155), (125, 125, 125), multi_player_game, clicked)
        menu_button("Exit", 15, 75, 150, 150, 45, (155, 155, 155), (125, 125, 125), exit_game, clicked)
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60


main_menu()

