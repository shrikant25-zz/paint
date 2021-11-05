import pygame
from setting import *

class Button:  # class use to create buttons
    def __init__(self, bxcoord, bycoord, bwidth, bheight, bcolorcode, bfontname=None, bfontsize=None, btext=None, btextcolor=None):
        self.bxcoord = bxcoord  # x-coordinate
        self.bycoord = bycoord  # y-coordinate
        self.bwidth = bwidth  # width
        self.bheight = bheight  # height
        self.bfontname = bfontname  # fontname
        self.bfontsize = bfontsize  # fontsize
        self.btext = btext  # text on button
        self.bcolorcode = bcolorcode  # backgroundcolor
        self.btextcolor = btextcolor  # text color

    def createbutton(self, win):  # function to create button
        pygame.draw.rect(win, color[self.bcolorcode], (self.bxcoord, self.bycoord, self.bwidth, self.bheight))
        # create an instance for font object
        if self.btext:
            smalltext = pygame.font.SysFont(self.bfontname, self.bfontsize)
            # get the surface and and rectangle to store the text
            textsurf, textrect = self.text_objects(self.btext, smalltext)
            # align the rectangle
            textrect.center = (int(self.bxcoord + (self.bwidth / 2)), int(self.bycoord + (self.bheight / 2)))
            # blit draws one thing on another
            # here it draws the textsurface on textrect
            win.blit(textsurf, textrect)
        pygame.display.flip()

    # this function returns the surface fo text and a rectangle to hold text on surface
    def text_objects(self, text, font):
        # renders text on surface and returns the surface
        # the returned surface will be the dimensions required to hold the surface
        textsurface = font.render(text, True, color[self.btextcolor])
        # textsurface provides the dimensions
        # while textsurface.get_rect() provides the rectangle to store
        # finally returns the surface (variable = textsurface)
        # textsurface.get_rect() creates returns a new rectangle covering the surface
        return textsurface, textsurface.get_rect()

    def chechkifclicked(self, win):  # checks if the button is clicked
        mousex, mousey = pygame.mouse.get_pos()  # gets the x and y coordinates of mouse's current position
        # if the position of mouse is within the button does the stuff and returns 1 else returns 0
        if self.bxcoord <= mousex <= self.bxcoord + self.bwidth and self.bycoord <= mousey <= self.bycoord + self.bheight:
            return 1
        return 0