def square(sq_side=int(input('Длина стороны квадрата: '))):
    """
    Func takes 1 arg that is len of square side.
    Than gives tuple of (perimeter, square, diagonal)
    :param sq_side:
    :return:
    """
    import math
    res = ((sq_side * 4), (sq_side ** 2), (math.sqrt(2 * (sq_side ** 2))))
    print(res)


if __name__ == '__main__':
    square()

