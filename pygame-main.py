import pygame

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
# Define grid parameters
grid_color = (0, 0, 0)  # black
cell_size = 50  # size of each cell in the grid
grid_size = 3  # size of the grid (3x3)

# Calculate the starting position of the grid
start_x = screen.get_width() // 2 - (cell_size * grid_size) // 2
start_y = screen.get_height() // 2 - (cell_size * grid_size) // 2

cell_colors = [[(255, 255, 255) for _ in range(grid_size)] for _ in range(grid_size)]  # initialize with white color
pygame.display.set_caption("Tic Tac Toe")

def menu_button(string,font,  x, y, width, height, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1:
            if action is not None:
                action()
            print("Button clicked")
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font('freesansbold.ttf', font)
    text = font.render(string, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    screen.blit(text, text_rect)


def draw_board():
    menu_button("Back", 10, 7.5, 7.5, 50, 25, (155, 155, 155), (125, 125, 125), main_menu)

    # Draw the cells
    for x in range(grid_size):
        for y in range(grid_size):
            pygame.draw.rect(screen, cell_colors[x][y], pygame.Rect(start_x + x * cell_size, start_y + y * cell_size, cell_size, cell_size))

    # Draw the grid
    for x in range(grid_size + 1):
        pygame.draw.line(screen, grid_color, (start_x + x * cell_size, start_y), (start_x + x * cell_size, start_y + cell_size * grid_size))
    for y in range(grid_size + 1):
        pygame.draw.line(screen, grid_color, (start_x, start_y + y * cell_size), (start_x + cell_size * grid_size, start_y + y * cell_size))
    

def single_player_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # A mouse click has occurred
                mouse_x, mouse_y = event.pos
                if start_x <= mouse_x <= start_x + cell_size * grid_size and start_y <= mouse_y <= start_y + cell_size * grid_size:
                    cell_x = (mouse_x - start_x) // cell_size
                    cell_y = (mouse_y - start_y) // cell_size
                    print(f"Mouse clicked in cell ({cell_x}, {cell_y})")
                    cell_colors[cell_x][cell_y] = (150, 150, 150)

        screen.fill("white")

        draw_board()
                
        pygame.display.flip()
        clock.tick(60)


def exit_game():
    pygame.quit()
    quit()


def main_menu():
    while True:
        
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")

        # RENDER YOUR GAME HERE
        
        menu_button("Single Player", 15, 75, 40, 150, 45, (155, 155, 155), (125, 125, 125), single_player_game)
        menu_button("Multi Player", 15, 75, 95, 150, 45, (155, 155, 155), (125, 125, 125))
        menu_button("Help", 15, 75, 150, 150, 45, (155, 155, 155), (125, 125, 125))
        menu_button("Exit", 15, 75, 205, 150, 45, (155, 155, 155), (125, 125, 125), exit_game)
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60


main_menu()

