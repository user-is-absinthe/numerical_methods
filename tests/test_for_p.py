def main():
    number = input('Введите число:\n')
    print('Сейчас мы будем Ваше число вращать!')
    number = list(number)
    exit_number = ''
    for i in range(len(number)):
        exit_number += str(number[len(number) - i - 1])
    print('Перевернутое число: {0}!'.format(exit_number))


if __name__ == '__main__':
    main()
