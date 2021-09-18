
class Cat:

    def __init__(self, legs, colour):
        self.colour = colour
        self.legs = legs

figo = Cat(4, "GREEN")
print(figo.__dict__)