from sys import maxsize
from setting import *
from button import *
import random
import pygame

class Game:
    def __init__(self):
        self.drawing_color = color[3]
        self.buttons = []
    
    def initialize_buttons(self, win):
        button_y_coordinate = HEIGHT - MENUBAR_HEIGHT/2 - 10 # setting the buttons postion 
        self.buttons = [
            Button(10, button_y_coordinate, 25, 25, 3),  # creating button instance
            Button(50, button_y_coordinate, 25, 25, 2),
            Button(90, button_y_coordinate, 25, 25, 1),
            Button(130, button_y_coordinate, 25, 25, 5),
            Button(170, button_y_coordinate, 25, 25, 6),
            Button(210, button_y_coordinate, 25, 25, 7),
            Button(250, button_y_coordinate, 25, 25, 8),
            Button(290, button_y_coordinate, 40, 25, 3, 'arial', 15,"Erase", 4),
            Button(350, button_y_coordinate, 40, 25, 3, 'arial', 15, "Clear", 4),
            Button(410, button_y_coordinate, 40, 25, 3,'arial', 15, 'Save',4),
        ]

        for button in self.buttons:
            button.createbutton(win)

    def init_grid(self, color):
        return [[color]*COLS for _ in range(ROWS)]
        #[ [ [255,255,255], [255,255,255] ]
        #  [ [255,255,255], [255,255,255] ]
        #  [ [255,255,255], [255,255,255] ]]

    def draw_grid(self, win, grid): # drawing actual pixels on screen
        for i, row in enumerate(grid):
            for j, color in enumerate(row): # pixel's location in grid = 1 unit grid * Pixel Dimension(height/width)
                pygame.draw.rect(win, color, (j * PIXEL_DIMENSIONS, i * PIXEL_DIMENSIONS, PIXEL_DIMENSIONS, PIXEL_DIMENSIONS))
    
    def draw_toolbar_line(self, win):
         # just drawing line between the painting part and the menu bar
            pygame.draw.line(win, color[3],  (0,ROWS * PIXEL_DIMENSIONS + 20),(COLS * PIXEL_DIMENSIONS  ,ROWS * PIXEL_DIMENSIONS + 20), PIXEL_DIMENSIONS//2)

    def draw(self, win, grid):
        self.draw_grid(win, grid) # gives call to draw grid function
        pygame.display.update() # needs to update the screen to display the change

    def get_row_col_from_pos(self, pos): # gets cursor position
        x, y = pos
        row = y // PIXEL_DIMENSIONS 
        col = x // PIXEL_DIMENSIONS 
        #           |r|
        # ----------|o|---(cols)--(x)
        #           |w|
        #         (y)

        if row >= ROWS: # checks if the mouse click was out of the grid
            raise IndexError

        return row, col

    def save(self, win):
        size = (600, 600) # lower right
        pos = (0, 0) # upper left
        image = pygame.Surface(size)  # Create image surface
        image.blit(win,(pos,size))  # send portion of display to image
        name = str(random.randint(1, maxsize)) + ".png" # create a random name
        pygame.image.save(image,name)  # Save the image 

    def rungame(self):
        pygame.init() # inits the game
        win = pygame.display.set_mode((WIDTH, HEIGHT)) # set the window
        pygame.display.set_caption("PAINT") # title for window
        grid = self.init_grid(BG_COLOR) # init_grid creates a grid and adds hex color values to each section of grid 
        win.fill(color[4]) # sets the background color
        self.initialize_buttons(win) 
        self.draw_toolbar_line(win)
        run = True

        while run: # main game loop
            for event in pygame.event.get(): # checks for any click event
                if event.type == pygame.QUIT: # checks if close button is cliked
                    run = False # game stops

                if pygame.mouse.get_pressed()[0]: # checks if left mouse button is clicked
                    pos = pygame.mouse.get_pos() # get cursor postion
                    
                    try:
                        # tries to get row and coloumn of grid correspondig to the cursor position
                        row, col = self.get_row_col_from_pos(pos) 
                        grid[row][col] = self.drawing_color # sets the section of grid to current drawing color
                    except IndexError: 
                        # if click is outside the painting area it means click is outside the grid and exception will be raised
                        for button in self.buttons: # checks if button located outside the grid are clicked
                            if not button.chechkifclicked(win): # if no button is clicked then the game will continue
                                continue
                            elif button.btext == "Clear": # if cleat button is clicked then the grid will be reset
                                grid = self.init_grid(BG_COLOR)
                                self.drawing_color = color[3] # drawing color will be set to deafult [currently black]
                            elif button.btext == "Erase": # if erase button is clicked drawing color will be set to white
                                self.drawing_color = color[4]
                            elif button.btext == "Save": # if save button is clicked the painting will be saved
                                self.save(win)
                            else: # if none of above buttons are clicked it means a color button was selected
                                self.drawing_color = color[button.bcolorcode] # color associated with the button becomes the drawing color
            self.draw(win, grid) # draws the grid with changes that are made
        pygame.quit() # quites the game

if __name__ == '__main__': # checks if it is the main file
    game = Game() # creates instance of game class
    game.rungame() # calling the run game function