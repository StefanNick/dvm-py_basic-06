def is_very_long(password):
    result = len(password) > 12
    return result


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_symbols(password):
    return any(not symbol.isalpha() and not symbol.isdigit() for symbol in password)


def score_password(password):
    list_of_functions = [
        is_very_long,
        has_digit,
        has_lower_letters,
        has_upper_letters,
        has_symbols,
    ]
    score = 0
    for func in list_of_functions:
        if func(password):
            score = score + 2
    return score


def main():
    password = input("Введите пароль: ")
    print("Рейтинг пароля:", score_password(password))


if __name__ == "__main__":
    main()
