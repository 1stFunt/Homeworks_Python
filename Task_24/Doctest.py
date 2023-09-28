def find_roots(a, b, c):
    """
    Находит корни квадратного уравнения ax^2 + bx + c = 0.
    :param a: коэффициент при x^2
    :param b: коэффициент при x
    :param c: свободный член
    :return: кортеж из двух значений - корни уравнения (может быть (None, None) для комплексных корней)

    >>> find_roots(1, -3, 2)
    (2.0, 1.0)
    >>> find_roots(1, 2, 1)
    (-1.0, -1.0)
    >>> find_roots(1, 1, 2)
    ((-0.5+1.3228756555322954j), (-0.5-1.3228756555322954j))
    >>> find_roots("a", 2, 1)
    Traceback (most recent call last):
    ...
    TypeError: Все аргументы (a, b, c) должны быть числами.
    >>> find_roots(0, 0, 0)
    Traceback (most recent call last):
    ...
    ValueError: Уравнение имеет бесконечно много корней.
    >>> find_roots(0, 0, 1)
    Traceback (most recent call last):
    ...
    ValueError: Уравнение не имеет корней.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Все аргументы (a, b, c) должны быть числами.")
    
    if a == 0 and b == 0:
        if c == 0:
            raise ValueError("Уравнение имеет бесконечно много корней.")
        else:
            raise ValueError("Уравнение не имеет корней.")

    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c
    # Если дискриминант положителен, есть два вещественных корня
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)
    # Если дискриминант равен нулю, есть один корень
    if discriminant == 0:
        root = -b / (2*a)
        return (root, root)
    # В противном случае (дискриминант отрицателен), корни комплексные
    real_part = -b / (2*a)
    imaginary_part = (-discriminant)**0.5 / (2*a)
    return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)