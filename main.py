"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

from Album import Album
from Interpreter import Interpreter

interpreter = Interpreter()

interpreter.addAlbumToRegistry(Album("Untouchables", "Korn"))
interpreter.addAlbumToRegistry(Album("Adrenaline", "Deftones"))
interpreter.interpret("album 2")
interpreter.interpret("album author 2")
interpreter.interpret("album author 1")
interpreter.interpret("author 1")
