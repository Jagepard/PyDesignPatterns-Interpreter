"""
author  : Jagepard <jagepard@yandex.ru>
license https://mit-license.org/ MIT
"""

class Interpreter():
    registry = []

    def addAlbumToRegistry(self, album):
        self.registry.append(album)

    def interpret(self, input):
        exploded = input.split(' ')

        for element in exploded:
            if self.is_number(element):
                self.getDataFromRegistry(exploded, self.registry[int(element) - 1])

    def getDataFromRegistry(self, exploded, album):
        output = ""

        for element in exploded:
            if element == "album":
                output += album.name + ' '
            if element == "author":
                output += album.author

        print(output)

    def is_number(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False
