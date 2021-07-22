def is_even(x):
    return x % 2 == 0

if __name__ == '__main__':
    # ten = []
    # for i in range(10):
    #     ten.append(i)
    # print(ten)
    ten = [i for i in range(10)]
    print(ten)
    even = list(filter(is_even, ten))
    print(even)
    even = list(filter(lambda x: x % 2 == 0, ten))
    print(even)
    incremented = list(map(lambda x: x + 1, even))
    print(incremented)