
class ShowCalled:
    def __init__(self):
        self.level = 0

    def add_one(self):
        self.level += 1


sc1 = ShowCalled()

sc2 = ShowCalled()

print(dir(ShowCalled))

sc = ShowCalled()

sc.add_one()

sc.add_one()
print(sc.level)

