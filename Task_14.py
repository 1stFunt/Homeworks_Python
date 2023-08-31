# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
import sys


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))

        if year < 1 or year > 9999:
            return False

        if month < 1 or month > 12:
            return False

        if month == 2:
            if is_leap_year(year):
                if day < 1 or day > 29:
                    return False
            else:
                if day < 1 or day > 28:
                    return False
        elif month in [4, 6, 9, 11]:
            if day < 1 or day > 30:
                return False
        else:
            if day < 1 or day > 31:
                return False

        return True
    except ValueError:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            "Пожалуйста, укажите дату в формате DD.MM.YYYY как аргумент командной строки.\nПример: python Task_14.py 31.12.2023")
    else:
        date = sys.argv[1]
        if is_valid_date(date):
            print(f"{date} - это допустимая дата.")
        else:
            print(f"{date} - это недопустимая дата.")
