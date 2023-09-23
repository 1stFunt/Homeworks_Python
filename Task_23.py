# Поиск корней квадратного уравнения.
# Функция find_roots, принимает три параметра: коэффициенты уравнения и возвращает его 
# корни в виде кортежа из двух значений.
# Созданы два собственных исключения NoSolutionsError и InfiniteSolutionsError, которые будут 
# вызваны в случае отсутствия и бесконечного количества решений уравнения.
# Если переданные коэффициенты не являются рациональными числами, вызовается исключение TypeError.
class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    try:
        x1 = float(0.00)
        x2 = float(0.00)
        if a == 0 and b == 0 and c == 0:
            raise InfiniteSolutionsError
        elif a == 0 and b != 0 and c != 0:
            x1 = -(c / b)
            return x1
        elif a == 0 and b == 0 and c != 0:
            raise NoSolutionsError
        elif a == 0 and b != 0 and c == 0:
            x1 = 0
            return x1
        else:
            disc = (b ** 2) - (4 * a * c)
            if disc == 0:
                return (-b / (2 * a), -b / (2 * a))
            elif disc > 0:
                x1 = (-b - (disc ** 0.5)) / (2 * a)
                x2 = (-b + (disc ** 0.5)) / (2 * a)
                return min(x1, x2), max(x1, x2)
            elif disc < 0:
                raise NoSolutionsError
    except TypeError:
        return "Вызвано исключение TypeError"
    except NoSolutionsError:
        return "Вызвано исключение NoSolutionsError"
    except InfiniteSolutionsError:
        return "Вызвано исключение InfiniteSolutionsError"


print(find_roots(1, 2, 1))

# Вызываем NoSolutionsError, так как a=0, b=0, и c=1
print(find_roots(0, 0, 1))  
# Вызываем InfiniteSolutionsError, так как a=0, b=0, и c=0
print(find_roots(0, 0, 0))
# Вызываем TypeError, так как первый аргумент - строка, а не число
print(find_roots("a", 2, 1))