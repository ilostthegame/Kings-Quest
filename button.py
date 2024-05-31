import pygame

class Button(pygame.sprite.Sprite):
    """
    Class for a generalised button.
    Attributes:
    surf: pygame.image
    rect: pygame.Rect
    output: str
    x_coord: int
    y_coord: int

    Constructor: (button_image, output, x_coord, y_coord)

    # TODO Check since this class has no methods
    """
    # Attributes
    __surf = None
    __rect = None
    __output = None
    __x_coord = None
    __y_coord = None

    # Constructor
    def __init__(self, button_image, output, x_coord, y_coord):
        super().__init__()
        self.setSurf(button_image) # sets surface to be the inputted image
        self.setRect(self.getSurf().get_rect())
        self.setOutput(output)
        self.setXCoord(x_coord)
        self.setYCoord(y_coord)
        self.getRect().center = (self.getXCoord(), self.getYCoord())

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getOutput(self):
        return self.__output
    def getXCoord(self):
        return self.__x_coord
    def getYCoord(self):
        return self.__y_coord

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setOutput(self, output):
        self.__output = output
    def setXCoord(self, x_coord):
        self.__x_coord = x_coord
    def setYCoord(self, y_coord):
        self.__y_coord = y_coord