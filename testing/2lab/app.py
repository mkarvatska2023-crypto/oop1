class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, figure_type: str, length: float):
        # Перевірка типу
        assert figure_type in self.FIGURES, "Невідомий тип фігури!"
        # Перевірка довжини
        assert length > 0, "Довжина має бути більшою за нуль!"
        self.type = figure_type
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.type

    @property
    def get_figure_length(self) -> float:
        return self.length

    def get_angles(self) -> int:
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        elif self.type == "трикутник":
            return 3
