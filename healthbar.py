import pygame
from assets import GAME_ASSETS

class HealthBar:
    # Attributes
    __surf = None
    __rect = None
    __entity_health = None
    __entity_max_health = None
    __entity_position = None

    # Constructor
    def __init__(self, surf, rect, entity_health, entity_max_health, entity_position):
        self.setSurf(surf)
        self.setRect(rect)
        self.setEntityHealth(entity_health)
        self.setEntityMaxHealth(entity_max_health)
        self.setEntityPosition(entity_position)

    # Getters
    def getSurf(self):
        return self.__surf
    def getRect(self):
        return self.__rect
    def getEntityHealth(self):
        return self.__entity_health
    def getEntityMaxHealth(self):
        return self.__entity_max_health
    def getEntityPosition(self):
        return self.__entity_position

    # Setters
    def setSurf(self, surf):
        self.__surf = surf
    def setRect(self, rect):
        self.__rect = rect
    def setEntityHealth(self, entity_health):
        self.__entity_health = entity_health
    def setEntityMaxHealth(self, entity_max_health):
        self.__entity_max_health = entity_max_health
    def setEntityPosition(self, entity_position):
        self.__entity_position = entity_position
