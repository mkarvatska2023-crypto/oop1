class Figure:
    def __init__(self, name: str, side: int):
        self.name = name
        self.side = side

    def get_angles(self):
        if self.name.lower() == "трикутник":
            return 3
        elif self.name.lower() == "квадрат":
            return 4
        elif self.name.lower() == "прямокутник":
            return 4
        else:
            # якщо фігура невідома
            return None
