def sum_of_last(n):

    if n == 0:
        return 0

    return (n % 10) + sum_of_last(n // 10)


print(sum_of_last(505))