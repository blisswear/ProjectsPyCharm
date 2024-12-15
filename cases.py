import random


balance = 600
inventory = []
cases = {
    "Бомж": 50,
    "Мажор": 150,
    "Олигарх": 200,
    "Мультимиллионер": 3000,
}

items = {
    "Бомж": [("Ножовка", 50), ("Водка", 150), ("Мальборо", 250)],
    "Мажор": [("Наушники", 250), ("Топор", 350), ("Золотая ручка", 450)],
    "Олигарх": [("Духи", 1500), ("Телефон", 3500), ("Аккумулятор", 4500)],
    "Мультимиллионер": [("Пистолет", 15000), ("Флешка", 5000), ("Камера", 60000)],
}


def show_cases():
    print("Доступные кейсы:")
    for case, price in cases.items():
        print(f"{case}: {price}")


def open_case(case_name):
    global balance
    if case_name not in cases:
        print("Такого кейса не существует.")
        return

    case_price = cases[case_name]
    if balance < case_price:
        print("Недостаточно средств для открытия этого кейса.")
        return

    balance -= case_price
    item = random.choice(items[case_name])
    inventory.append(item)
    print(f"Вам выпало: {item[0]} - Цена: {item[1]}")


def show_inventory():
    if not inventory:
        print("Ваш инвентарь пуст.")
    else:
        print("Ваш инвентарь:")
        for idx, item in enumerate(inventory):
            print(f"{idx + 1}. {item[0]} - Цена: {item[1]}")


def sell_item(item_index):
    global balance
    if item_index < 1 or item_index > len(inventory):
        print("Некорректный индекс предмета.")
        return

    item = inventory.pop(item_index - 1)
    balance += item[1]  # Добавляем цену предмета к балансу
    print(f"Вы продали: {item[0]} - Получено: {item[1]}")


while True:
    show_cases()
    user_input = input("Введите название кейса для открытия (или 'выход' для выхода): ")

    if user_input.lower() == 'выход':
        break

    open_case(user_input)
    show_inventory()

    if inventory:
        sell_choice = input("Хотите продать предмет? (да/нет): ")
        if sell_choice.lower() == 'да':
            try:
                item_index = int(input("Введите номер предмета для продажи: "))
                sell_item(item_index)
            except ValueError:
                print("Пожалуйста, введите корректное число.")

    print(f"Ваш баланс: {balance}")