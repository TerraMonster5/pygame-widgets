import pygame as pyg
from typing import Union, Callable

class Widget:
    def __init__(self, parent, x: int, y: int, text: str=""):
        self._parent = parent
        self._text = text

    def draw(self):
        pass

class Button(Widget):
    def __init__(self, parent, x: int, y: int, width: Union[int, None]=None, height: Union[int, None]=None, bg: Union[pyg.Color, str, None]=None, state: str="enabled", default: str="enabled", text: str="", command: Union[Callable, None]=None) -> None:
        super().__init__(parent, x, y, text)

class Entry(Widget):
    pass

class CheckButton(Widget):
    pass

class RadioButton(Widget):
    __groups: dict = {}
    pass

class Label(Widget):
    pass