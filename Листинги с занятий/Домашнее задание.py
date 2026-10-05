import os

HISTORY_FILE = 'calculations.txt'


def calculate(a, b, op):
    if op == 1:
        return a + b, '+'
    if op == 2:
        return a - b, '-'
    if op == 3:
        return a * b, '*'
    if op == 4:
        return a / b, '/'


def save_to_history(a, b, op, result):
    symbol = ['+', '-', '*', '/'][op - 1]
    if op == 4:
        line = f'Результат: {a}{symbol}{b}={result:.2f}\n'
    else:
        line = f'Результат: {a}{symbol}{b}={result}\n'
    with open(HISTORY_FILE, 'a', encoding='utf-8') as f:
        f.write(line)


def show_history():
    if not os.path.exists(HISTORY_FILE):
        print('История пуста.')
        return
    with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.strip():
        print('История пуста.')
    else:
        print(content, end='')


def main():
    while True:
        print('\nВыберите операцию:')
        print('1. Сложение')
        print('2. Вычитание')
        print('3. Умножение')
        print('4. Деление')
        print('5. Просмотр истории вычислений')

        choice = input('\nВведите номер операции: ')

        if choice == '5':
            show_history()
            continue

        if choice not in ('1', '2', '3', '4'):
            print('Некорректный ввод. Введите число от 1 до 5.')
            continue

        op = int(choice)
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))

        if op == 4 and b == 0:
            print('Деление на ноль невозможно.')
            continue

        result, _ = calculate(a, b, op)
        symbol = ['+', '-', '*', '/'][op - 1]

        if op == 4:
            print(f'Результат: {a}{symbol}{b}={result:.2f}')
        else:
            print(f'Результат: {a}{symbol}{b}={result}')

        save_to_history(a, b, op, result)


if __name__ == '__main__':
    main()