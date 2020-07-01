def main():
    arr_1 = ['aa', 'bb', 'ccee', 'dd', 'ee', 'ff']
    arr_2 = ['acc', 'b', 'c', 'dee', 'e', 'f']
    iter_a = ((x, y) for x in arr_1 if len(x) == 2 for y in arr_2 if len(y) == 1)
    print(type(iter_a))
    print(next(iter_a))
    print(next(iter_a))
    print(next(iter_a))


if __name__ == '__main__':
    main()
