for number in range(99, 1001):
    if number % 2 == 0:
        my_n = number
        number = number * number + 1
        if my_n == 1000:
            print(number)
            break
