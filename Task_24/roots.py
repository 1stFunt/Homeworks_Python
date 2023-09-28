def find_roots(a, b, c):
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