from service.AbsClass import AbsClass


class A(AbsClass):
    def __init__(self):
        super().__init__()
        print("a")

    def test(self):
        print("a test")
