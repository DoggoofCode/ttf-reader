class Vec2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: 'Vec2' and '{}'".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -: 'Vec2' and '{}'".format(type(other)))

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vec2(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Unsupported operand type for *: 'Vec2' and '{}'".format(type(scalar)))

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vec2(self.x / scalar, self.y / scalar)
        else:
            raise TypeError("Unsupported operand type for /: 'Vec2' and '{}'".format(type(scalar)))

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Index out of range for 'Vec2'")

    def __repr__(self):
        return "Vec2({}, {})".format(self.x, self.y)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normalize(self):
        length = self.length()
        if length != 0:
            return Vec2(self.x / length, self.y / length)
        else:
            return Vec2()


def LinearInterpolation(start: Vec2, end: Vec2, t: float):
    return start + (end - start) * t


def BezierInterpolation(a: Vec2, control_point: Vec2, c: Vec2, t: float):
    return LinearInterpolation(LinearInterpolation(a, control_point, t), LinearInterpolation(control_point, c, t), t)


def IntX(value: list[str], little_endian=False):
    bin_val = "0b"
    for i in value:
        binaried = bin(int(i, 16))[2:]
        bin_val += binaried
    return int(bin_val, 2) if not little_endian else int("0b"+((bin_val[2:])[::-1]), 2)


def ReadText(data: list[str]):
    return "".join([chr(int(i, 16)) for i in data])
