import numpy as np


class Point(np.ndarray):
    def __new__(cls, x, y):
        return np.ndarray(shape=(2,), dtype=np.int64, buffer=np.array([x, y], dtype=np.int64)).view(cls)

    def __array_finalize__(self, obj) -> None:
        if obj is None:
            return
        default_attributes = {"attr": 1}
        self.__dict__.update(default_attributes)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        return Point(self[0] - other[0], self[1] - other[1])

    def __add__(self, other):
        return Point(self[0] + other[0], self[1] + other[1])

    def __repr__(self):
        return f'(x: {self.x}, y: {self.y})'

    def transform_to_tuple(self):
        return self.x, self.y

    @classmethod
    def is_equal(cls, point_1, point_2):
        cond = point_1 == point_2
        return cond[0] and cond[1]
