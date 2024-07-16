import pygame
from sprites.active_entity import ActiveEntity
from pygame.locals import *
from assets import GAME_ASSETS
from sprites.healthbar import Healthbar
from sprites.weapon import Weapon
from attack import Attack
from typing import Any, Optional

class Character(ActiveEntity):
    """Class representing a character entity.

    Attributes:
        (Inherited)
        surf (pygame.Surface): Pygame surface for the entity, onto which to blit the entity image, weapon and healthbar.
            Size: 64 x 64, transparent.
        image (pygame.Surface): Surface representing entity's sprite image.
            Size: 32 x 48, transparent.
        name (str): Name of character
        attack (int): Attack stat
        defence (int): Defence stat
        max_health (int): Maximum health stat
        health (int): Current health stat
        health_regen (int): How much health regenerates each turn
        weapon (Weapon): Currently held weapon
        is_alive (bool): Whether entity's is alive: health above 0 or not
        xcoord (int): X coordinate of entity in world
        ycoord (int): Y coordinate of entity in world
        healthbar (Healthbar): Healthbar of entity

        level (int): Current level of character
        exp (int): Exp stat
    """
    
    # Attributes
    __level = None
    __exp = None

    # Constructor
    def __init__(self,  
                 image: pygame.Surface, 
                 name: str,
                 weapon_id: str, 
                 attack: int = 25, 
                 defence: int = 25, 
                 max_health: int = 100, 
                 health: int = 100, 
                 health_regen: int = 2,
                 is_alive: bool = True, 
                 xcoord: int = 0, 
                 ycoord: int = 0, 
                 level: int = 1, 
                 exp: int = 0):
        super().__init__(image, name, attack, defence, max_health, health, health_regen, 
                         Weapon(weapon_id, xcoord, ycoord),
                         is_alive, xcoord, ycoord, Healthbar(health, max_health)) 
        self.setLevel(level)
        self.setExp(exp)

    # Getters
    def getLevel(self):
        return self.__level
    def getExp(self):
        return self.__exp
    
    # Setters
    def setLevel(self, level):
        self.__level = level
    def setExp(self, exp):
        self.__exp = exp

    # Methods
    def handleAction(self, action: tuple[str, Any]) -> Optional[list[str]] | bool:
        """Runs the character method for a given action.

        Returns the list of events caused if the action was valid.
        Else returns False if the action was invalid.
        """
        action_type = action[0]
        action_arg = action[1]
        # Determines and runs the corresponding character method.
        match action_type:
            case 'move':
                character_caused_events = self.move(action_arg)
            case 'interact':
                character_caused_events = self.interact(action_arg)
            case 'attack':
                character_caused_events = self.attack(action_arg)
            case _:
                raise ValueError(f'Action ({action_type}) does not exist.')
        return character_caused_events
    
    def move():
        pass 

    def interact(self, direction: str, some_group: pygame.sprite.Group) -> bool:
        """
        Given a direction, has character interact with adjacent entity in that direction.
        Valid entities are: npc, portal
        """
        pass

    def attack(self, target):
        """
        Given a target, determines whether it is in range, then attacks it
        
        TODO will need to insert unpassable squares
        """
        pass

    def tilesInRange(self, attack, tile_group, all_entities):
        """
        Returns a list of all tiles in range of attack.
        Takes the attack used, and the groups of tiles and all entities as arguments. 
        """
        pass

    def gainExp(self, exp):
        """
        Increases character's exp, and increases levels accordingly. Subtracts used exp.
        Runs stat increase method based on levels gained.
        """
        original_level = self.getLevel()
        self.setExp(self.getExp() + exp)
        required_exp = self.calcRequiredExp() # Calculate exp required for next level

        # Level up character while character has enough exp to level up and is below the level cap (50).
        while self.getExp() >= required_exp and self.getLevel() < 50:
            self.setLevel(self.getLevel() + 1)
            self.setExp(self.getExp() - required_exp) # subtract used exps.
            required_exp = self.calcRequiredExp() # Re-calculate exp required for next level

        # Update attack/defence and if levelled up, prints levelup info.
        level_increase = self.updateStats(original_level)
        # TODO


    def updateStats(self, original_level):
        """Updates attack, defence based on change in level.

        Returns tuple (level_increase, attack_increase, defence_increase)
        """
        level_increase = self.getLeve() - original_level
        attack_increase = level_increase * 2
        defence_increase = level_increase * 2
        self.setAttack(self.getAttack() + attack_increase)
        self.setDefence(self.getDefence() + defence_increase)
        return (level_increase, attack_increase, defence_increase)

    def calcRequiredExp(self):
        """
        Calculates total required exp to get to next level
        """ 
        return int(100 * (1.5 ** (self.getLevel())))  # Current formula TODO change: 100 * 1.5^level.