def count_digits(number):
    return len(str(number))

def is_armstrong_number(number):
    p = count_digits(number)
    num = number
    result = 0

    while num:
        digit = num % 10
        num = num // 10
        result += digit ** p

    return result == number
