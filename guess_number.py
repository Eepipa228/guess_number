from random import randint

def play_game():
    """Одна игра — угадывание числа от 1 до 100."""
    number = randint(1, 100)
    print('\nУгадайте число от 1 до 100')

    while True:
        guess = int(input('Введите число: '))

        if guess < number:
            print('Ваше число меньше того, что загадано.')
        elif guess > number:
            print('Ваше число больше того, что загадано.')
        else:
            print('Отличная интуиция! Вы угадали число :)')
            break


while True:
    play_game()

    answer = input('Хотите сыграть ещё раз? (да/нет): ').strip().lower()
    if answer not in ('да', 'д', 'yes', 'y'):
        print('Спасибо за игру! До встречи 👋')
        break