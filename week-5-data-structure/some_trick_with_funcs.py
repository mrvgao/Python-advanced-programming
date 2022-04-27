def func0(a=0, b=1): pass


def func1(a=1, b=2, numbers=[1, 2, 3]):
    print(numbers + [a, b])


func1.__defaults__[-1].append(func0.__defaults__[0])
func1()