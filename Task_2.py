# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


num = int(input("Введите число (от 2 до 100000): "))
if 2 <= num <= 100000:
    if is_prime(num):
        print(f"{num} - простое число.")
    else:
        print(f"{num} - составное число.")
else:
    print("Число должно быть от 2 до 100000.")
