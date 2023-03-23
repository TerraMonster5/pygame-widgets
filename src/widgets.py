import pygame
import pygame.freetype
from typing import Union, Callable

font = pygame.freetype.SysFont("Arial", 18)

class Label:
    def __init__(self,
                 parent,
                 x: int=0,
                 y: int=0,
                 text: str="") -> None:
        
        """
        Displays a text box with top left co-ordinates at x, y containing text.
        """

        self.parent = parent
        self.x = x
        self.y = y
        self.text = text

    def draw(self) -> None:
        font.render_to(self.parent, (self.x, self.y), self.text)

class Button:
    def __init__(self,
                 parent,
                 x: int=0,
                 y: int=0,
                 width: Union[int, None]=None,
                 height: Union[int, None]=None,
                 bg: Union[pygame.Color, int, tuple, None]=None,
                 state: str="enabled",
                 text: str="",
                 command: Union[Callable, None]=None) -> None:
        
        """
        Displays and interactive button with top left co-ordinates at x, y containing text.
        """

        self.parent = parent
        self.x = x
        self.y = y

        if width: self.width = width
        else: self.width = 100

        if height: self.height = height
        else: self.height = 50

        if bg: self.bg = bg
        else: self.bg = pygame.Color(0, 0, 0)

        self.state = state
        self.text = text
        self.command = command
    
    def draw(self) -> None:
        pygame.draw.rect(self.parent, self.bg, pygame.Rect(self.x, self.y, self.width, self.height), 0)

        if self.text:
            text = font.render(self.text, 1, (0, 0, 0))

class CheckButton(Button):
    pass

class RadioButton(Button):
    __groups: dict = {}
    pass

class Entry:
    pass