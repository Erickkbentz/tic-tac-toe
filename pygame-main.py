import pygame

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
running = True
# Define grid parameters
grid_color = (0, 0, 0)  # black
cell_size = 50  # size of each cell in the grid
grid_size = 3  # size of the grid (3x3)

# Calculate the starting position of the grid
start_x = screen.get_width() // 2 - (cell_size * grid_size) // 2
start_y = screen.get_height() // 2 - (cell_size * grid_size) // 2

cell_colors = [[(255, 255, 255) for _ in range(grid_size)] for _ in range(grid_size)]  # initialize with white color


def menu_button(string, x, y, width, height, color, hover_color):
    mouse = pygame.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        print("Button clicked")
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render(string, True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (x + width // 2, y + height // 2)
    screen.blit(text, text_rect)


def menu():
    menu_button("Single Player", 75, 40, 150, 45, (155, 155, 155), (125, 125, 125))
    menu_button("Multi Player", 75, 95, 150, 45, (155, 155, 155), (125, 125, 125))
    menu_button("Help", 75, 150, 150, 45, (155, 155, 155), (125, 125, 125))
    menu_button("Exit", 75, 205, 150, 45, (155, 155, 155), (125, 125, 125))


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
    

while running:
    pygame.display.set_caption("Tic Tac Toe")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP key pressed")
            if event.key == pygame.K_DOWN:
                print("DOWN key pressed")
            if event.key == pygame.K_LEFT:
                print("LEFT key pressed")
            if event.key == pygame.K_RIGHT:
                print("RIGHT key pressed")
        
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:  # A mouse click has occurred
            mouse_x, mouse_y = event.pos
            if start_x <= mouse_x <= start_x + cell_size * grid_size and start_y <= mouse_y <= start_y + cell_size * grid_size:
                cell_x = (mouse_x - start_x) // cell_size
                cell_y = (mouse_y - start_y) // cell_size
                print(f"Mouse clicked in cell ({cell_x}, {cell_y})")
                cell_colors[cell_x][cell_y] = (150, 150, 150)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    
    menu()

    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

