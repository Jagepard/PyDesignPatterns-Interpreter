"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

class Album():
    _name = ""
    _author = ""

    def __init__(self, name, author): 
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author
