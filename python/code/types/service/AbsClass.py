class AbsClass(object):
    def __init__(self):
        print("AbsClass")

    def test(self):
        raise NotImplementedError
