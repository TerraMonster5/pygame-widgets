import pygame as pyg
from typing import Union, Callable

class Widget:
    def __init__(self):
        pass

    def draw(self):
        pass

class Button(Widget):
    def __init__(self, parent, x: int, y: int, width: Union[int, None]=None, height: Union[int, None]=None, text: str="", command: Union[Callable, None]=None) -> None:
        pass

class Entry(Widget):
    pass

class CheckButton(Widget):
    pass

class RadioButton(Widget):
    __groups: dict = {}
    pass

class Label(Widget):
    pass