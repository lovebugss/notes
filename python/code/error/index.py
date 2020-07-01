import logging

logger = logging.getLogger()


def test(a):
    try:
        raise KeyError('aaa')
    except Exception as e:
        logger.error('a: %s, e: %s', a, e, exc_info=True)


def main():
    test("aa")


if __name__ == '__main__':
    main()
