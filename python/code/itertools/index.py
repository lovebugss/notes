'''
测试写入方式
'''
import gzip
import time
from itertools import islice


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        resp = func(*args, **kwargs)
        print('fucntion name: [%s] used time: [%f], args: [%s], kwargs: [%s]' % (
        func.__name__, time.time() - start, args, kwargs))
        return resp

    return wrapper


@timeit
def test1(file):
    with gzip.open("test1.gz", "wb") as f:
        with gzip.open(file, "rb") as d:
            while True:
                lines = d.readlines(5000)
                if not lines:
                    break
                # f.writelines(lines)


@timeit
def test(file):
    with gzip.open("test.gz", "wb") as f:
        with gzip.open(file, "rb") as d:
            while True:
                line = d.readline()
                if not line:
                    break
                # f.write(line)


@timeit
def test2(file):
    with gzip.open("test2.gz", "wb") as f:
        with gzip.open(file, "rb") as d:

            while True:
                line = list(islice(d, 5000))
                if not line:
                    break
                # f.writelines(line)


@timeit
def test3(file):
    with gzip.open("test3.gz", "wb") as f:
        with gzip.open(file, "rb") as d:
            # f.write(d.read())
            d.read()


@timeit
def test4(file):
    with gzip.open("test4.gz", "wb") as f:
        with gzip.open(file, "rb") as d:
            for line in d:
                # f.write(line)
                pass


@timeit
def main():
    test("/Users/goclouds/Downloads/E30QWJQGSJ8WGU.2020-06-11-15.9de6fb88.gz")
    test1("/Users/goclouds/Downloads/E30QWJQGSJ8WGU.2020-06-11-15.9de6fb88.gz")
    test2("/Users/goclouds/Downloads/E30QWJQGSJ8WGU.2020-06-11-15.9de6fb88.gz")
    test3("/Users/goclouds/Downloads/E30QWJQGSJ8WGU.2020-06-11-15.9de6fb88.gz")
    test4("/Users/goclouds/Downloads/E30QWJQGSJ8WGU.2020-06-11-15.9de6fb88.gz")


if __name__ == '__main__':
    main()
