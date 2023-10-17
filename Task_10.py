# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
def add_funds(balance, transactions):
    while True:
        try:
            amount = int(input("Введите сумму для пополнения (кратную 50): "))
            if amount % 50 == 0:
                balance += amount
                transactions.append(f"Пополнение: +{amount}")
                return balance
            else:
                print("Введена некорректная сумма (не кратна 50)")
        except ValueError:
            print("Введите корректное число.")


def withdraw_funds(balance, transactions):
    while True:
        try:
            amount = int(input("Введите сумму для снятия (кратную 50): "))
            if amount % 50 == 0:
                if amount + 0.015 * amount < balance:
                    balance -= (amount + 0.015 * amount)
                    transactions.append(f"Снятие: -{amount + 0.015 * amount}")
                    return balance
                else:
                    print("Недостаточно средств на счете.")
            else:
                print("Введена некорректная сумма (не кратна 50)")
        except ValueError:
            print("Введите корректное число.")


def atm_simulation():
    balance = 0
    transactions = []
    count = 0

    while True:
        if balance > 5_000_000:
            print("С вас сняли налог на богатство:", balance * 0.1)
            balance -= balance * 0.1

        print(f"Текущий баланс: {balance} у.е.")
        print("1. Пополнить счет")
        print("2. Снять средства")
        print("3. Выйти")

        action = input("Выберите действие: ")

        if action == "1":
            balance = add_funds(balance, transactions)
            count += 1
        elif action == "2":
            balance = withdraw_funds(balance, transactions)
            count += 1
        elif action == "3":
            print("Завершаем работу банкомата.")
            break

        if count % 3 == 0:
            balance *= 1.03


if __name__ == "__main__":
    atm_simulation()
