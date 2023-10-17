# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.
import logging
import argparse

logging.basicConfig(
    format='{asctime} {levelname} {funcName} -> {lineno}: {msg}', style='{', level=logging.INFO)
logger = logging.getLogger(__name__)


def find_roots(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        logger.error("Ошибка: Все аргументы (a, b, c) должны быть числами.")
        raise TypeError("Все аргументы (a, b, c) должны быть числами.")

    if a == 0 and b == 0:
        if c == 0:
            logger.info("Уравнение имеет бесконечно много корней.")
            raise ValueError("Уравнение имеет бесконечно много корней.")
        else:
            logger.info("Уравнение не имеет корней.")
            raise ValueError("Уравнение не имеет корней.")

    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c
    logger.info(f"Дискриминант: {discriminant}")
    # Если дискриминант положителен, есть два вещественных корня
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        logger.info(f"Два вещественных корня: {root1}, {root2}")
        return (root1, root2)
    # Если дискриминант равен нулю, есть один корень
    if discriminant == 0:
        root = -b / (2*a)
        logger.info(f"Один корень: {root}")
        return (root, root)
    # В противном случае (дискриминант отрицателен), корни комплексные
    real_part = -b / (2*a)
    imaginary_part = (-discriminant)**0.5 / (2*a)
    logger.info(
        f"Два комплексных корня: {complex(real_part, imaginary_part)}, {complex(real_part, -imaginary_part)}")
    return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

# Прописать в терминал: python Task_25.py 1 2 1
parser = argparse.ArgumentParser(description='Решение квадратного уравнения')
parser.add_argument('-a', type=float, help='Коэффициент a', default=0)
parser.add_argument('-b', type=float, help='Коэффициент b', default=0)
parser.add_argument('-c', type=float, help='Коэффициент c', default=0)
args = parser.parse_args()

try:
    roots = find_roots(args.a, args.b, args.c)
    print(f"Корни уравнения: {roots}")
except Exception as e:
    logger.error(f"Произошла ошибка: {str(e)}")