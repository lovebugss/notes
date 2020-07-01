import gzip
from itertools import islice


def main():
    path = "/Users/goclouds/Downloads/E30QWJQGSJ8WGU.2020-06-01-13.ca8d0fa3.gz"
    with gzip.open(path, 'r') as f:
        while True:
            lines = list(islice(f, 1000))
            if not lines:
                break
            print(lines)


if __name__ == '__main__':
    main()
