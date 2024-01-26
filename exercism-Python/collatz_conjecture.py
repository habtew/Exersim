def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    def steps_recursive(number, count):
        if number == 1:
            return count

        if number % 2 == 0:
            return steps_recursive(number // 2, count + 1)
        else:
            return steps_recursive(number * 3 + 1, count + 1)

    return steps_recursive(number, 0)
        

