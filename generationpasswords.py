import random
import string


def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation


    password = ''.join(random.choice(characters) for i in range(length))

    return password


if __name__ == "__main__":
    length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
    password = generate_password(length)
    print(f"Сгенерированный пароль: {password}")