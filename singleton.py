class RGB:
    _instances: list["RGB"] = []

    def __new__(cls, r: int, g: int, b: int):
        inst = [x for x in cls._instances if x == (r, g, b)]

        if len(inst):
            return inst[0]
        
        new_inst = super().__new__(cls)
        cls._instances.append(new_inst)
        return new_inst


    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self) -> str:
        return f"rgb({self.r}, {self.g}, {self.b})"
    
    def __eq__(self, value: tuple[int, int, int]) -> bool:
        return (self.r, self.g, self.b) == value
    
rouge = RGB(255, 0, 0)
meme_rouge = RGB(255, 0, 0)

print(meme_rouge is rouge)

blue = RGB(0, 0, 255)
meme_blue = RGB(0, 0, 255)

print(blue is meme_blue)
print(rouge is blue)

blue.r = 1
print(meme_blue)
