# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def add_fractions(num1, den1, num2, den2):
    common_denominator = den1 * den2
    sum_numerator = num1 * den2 + num2 * den1
    common_divisor = gcd(sum_numerator, common_denominator)
    return sum_numerator // common_divisor, common_denominator // common_divisor


def multiply_fractions(num1, den1, num2, den2):
    product_numerator = num1 * num2
    product_denominator = den1 * den2
    common_divisor = gcd(product_numerator, product_denominator)
    return product_numerator // common_divisor, product_denominator // common_divisor


fraction_str1 = input("Введите первую дробь в формате a/b: ")
fraction_str2 = input("Введите вторую дробь в формате a/b: ")
num1, den1 = map(int, fraction_str1.split('/'))
num2, den2 = map(int, fraction_str2.split('/'))
sum_num, sum_den = add_fractions(num1, den1, num2, den2)
product_num, product_den = multiply_fractions(num1, den1, num2, den2)
print("Своя программа:")
print("Сумма дробей:", str(sum_num) + "/" + str(sum_den))
print("Произведение дробей:", str(product_num) + "/" + str(product_den))

# Проверка с использованием модуля fractions
fraction1 = Fraction(num1, den1)
fraction2 = Fraction(num2, den2)
expected_sum = fraction1 + fraction2
expected_product = fraction1 * fraction2
print("\nПроверка с использованием fractions:")
print("Ожидаемая сумма:", expected_sum)
print("Ожидаемое произведение:", expected_product)