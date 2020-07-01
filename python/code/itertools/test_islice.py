from itertools import islice


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    a = iter(data)
    while True:
        d = list(islice(a, 2))
        if not d:
            break
        print(d)

if __name__ == '__main__':
    main()
