def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isdigit() and not symbol.isalpha() for symbol in password)


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)


def main():
    password = input('Введите пароль: ')
    score = 0
    conditions = [
        is_very_long(password),
        has_digit(password),
        has_upper_letters(password),
        has_lower_letters(password),
        has_symbols(password),
        has_letters(password)
    ]
    for condition in conditions:
        if condition:
            score += 2
    print('Рейтинг вашего пароля', score)


if __name__ == '__main__':
    main()
