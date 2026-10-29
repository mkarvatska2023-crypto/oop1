# Звіт до роботи

## Тема: Тестування

## Мета роботи: Дізнатись про види тестування, а також як і коли ними користуватись.

---

### Виконання роботи

#### 1. Unit testing (`unittest`)
* **Папка:** `01_general_testing`
* **Файли:** `app.py` та `test_app.py`
* **Результат:** Passed
* **Висновок:** Навчились користуватись класичними unit-тестами.
![](/1%20lab/photo/lab1_photo1.png)

#### 2. Testing by library `pytest`
* **Папка:** `02_pytest`
* **Файли:** `app.py` та `test_app.py`
* **Результат:** Passed
* **Висновок:** Навчились користуватись бібліотекою `pytest`.

![](/1%20lab/photo/lab1_photo2.png)
#### 3. Code coverage
* **Папка:** `03_coverage`
* **Файли:** `app.py` та `test_app.py`
* **Результат:** Passed
* **Висновок:** Навчились користуватись бібліотекою `coverage`.
![](/1%20lab/photo/lab1_photo3.png)
![](/1%20lab/photo/lab1_phptp4.png)
#### 4. Integration testing
* **Папка:** `04_integration_tests`
* **Файли:** `app.py` та `test_app.py`
* **Результат:** Passed
* **Висновок:** Навчились користуватись інтеграційним методом тестування.
![](/1%20lab/photo/lab1_photo5.png)
---

### Реалізований код та тести

#### `app.py`
```python
class Figure:
    def __init__(self, figure_type: str, length: float):
        if length <= 0:
            raise ValueError("Довжина має бути більшою за нуль!")
        
        self.figure_type = figure_type
        self.length = length

    @property
    def get_figure_type(self) -> str:
        return self.figure_type

    @property
    def get_figure_length(self) -> float:
        return self.length

    @property
    def get_angles(self) -> int:
        """Метод, який повертає кількість кутів залежно від типу фігури."""
        fig_type = self.figure_type.lower()
        if fig_type in ["квадрат", "прямокутник"]:
            return 4
        elif fig_type in ["трикутник"]:
            return 3
        else:
            raise ValueError(f"Невідомий тип фігури: {self.figure_type}")
```

#### `test_app.py`
```python
import pytest
from app import Figure

def test_triangle_type():
    triangle = Figure("трикутник", 4)
    assert triangle.get_figure_type == "трикутник"

def test_invalid_length():
    with pytest.raises(ValueError):
        Figure("квадрат", 0)
```

### Висновок:


- Методи тестування;

- Так;

- Дізнався про методи тестування та як ними користуватись,а також про бібліотеки для полегшення роботи при тестуванні;

- Так;

- Так;

- Ні;

- Так;

- Все на вищому рівні.