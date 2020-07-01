from service import AbsClass


class B(AbsClass):
    def __init__(self):
        super().__init__()
        print("b")

    def test(self):
        print("b test")
