import time
from functools import reduce


def time_decorator(func_to_timing):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        sum_result = func_to_timing(*args, **kwargs)
        time_result = time.time() - start_time
        print(f"Time: {time_result * 1000}")
        return sum_result

    return wrapper


class Utils:
    @staticmethod
    @time_decorator
    def sum_n_numbers(n=100):
        return sum([i for i in range(1, 101)])

    @staticmethod
    @time_decorator
    def prod_n_numbers(n=100):
        return reduce(lambda prod, x: prod * x, range(1, n + 1), 1)


sum_result = Utils.sum_n_numbers()
print(sum_result)

prod = Utils.prod_n_numbers(50)
print(prod)


class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1
        self.__get_w_h()

    @property
    def x0(self):
        return self._x0

    @property
    def y0(self):
        return self._y0

    @property
    def x1(self):
        return self._x1

    @property
    def y1(self):
        return self._y1

    def __str__(self):  # Представляет класс в виде строки
        return f"x0={self._x0}, y0={self._y0}, x1={self._x1}, y1={self._y1}"

    def __repr__(self):  # Представляет класс в виде строки в объектах
        return f"(({self._x0}; {self._y0}), ({self._x1}; {self._y1}))"

    def __add__(self, other):
        return Bbox(min(self._x0, other._x0),
                    min(self._y0, other._y0),
                    max(self._x1, other._x1),
                    max(self._y1, other._y1))

    def __get_w_h(self):  # внутренний метод. Не для пользователя
        self.w = self._x1 - self._x0
        self.h = self._y1 - self._y0

    def get_area(self):
        self.__get_w_h()
        return self.w * self.h


bbox = Bbox(1, 2, 5, 6)
print(bbox.x0)
print(dir(bbox))
print(bbox.get_area())


class Chessman:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def __repr__(self):
        return f"Я {self.color} фигура на {self.position}"


class Pawn(Chessman):
    def __init__(self, position, color):
        super().__init__(position, color)
        self.im_queen = False

    def __repr__(self):
        return f"Я {self.color} пешка на {self.position}"

piece = Chessman("A2", "White")
pawn = Pawn("G2", "White")

print(piece)
print(pawn, pawn.im_queen)
