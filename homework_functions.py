def your_function(*args, **kwargs) -> float:
    suma = 0
    if args:
        for arg in args:
            if type(arg) in [int, float]:
                suma += arg
    return suma


def add_numbers_up_to(number: int) -> int:
    if number == 0:
        return 0
    return number + add_numbers_up_to(number - 1)


def add_even_numbers_up_to(number: int) -> int:
    if number == 0:
        return 0
    if number % 2 == 1:
        return add_even_numbers_up_to(number - 1)
    return number + add_even_numbers_up_to(number - 2)


def add_odd_numbers_up_to(number: int) -> int:
    if number == 1:
        return 1
    if number % 2 == 0:
        return add_odd_numbers_up_to(number - 1)
    return number + add_odd_numbers_up_to(number - 2)


def number_has_decimals():
    number = input("Give a number")
    if int(number) == float(number):
        return number
    return 0


if __name__ == '__main__':
    print(your_function(1, 5, -3, 'ABC', [12, 56, 'cad']))
    print(your_function())
    print(your_function(2, 4, 'abc', param_1=2))
    print(add_numbers_up_to(10))
    print(add_odd_numbers_up_to(8))
    print(add_odd_numbers_up_to(7))
    print(add_even_numbers_up_to(8))
    print(add_even_numbers_up_to(7))
    print(number_has_decimals())
