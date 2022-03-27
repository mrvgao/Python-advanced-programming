def combine(elements):
    return sum(elements)


def configure(arguments):
    for k, v in arguments:
        print(k, v)


def configure_s(*arg):
    print(arg)


def configure_ks(**kwargs):
    print(kwargs)


def function_with_three_arguments(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def get_config_info():
    return ('length', 3), ('level', 4), ('security', 10)


def control_by_configure(length, level, security):
    print(length, level, security)


def function_with_arbitary_arguments(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':
    arguments = get_config_info()

    #function_with_three_arguments(get_config_info()[0], get_config_info()[1],)
    function_with_three_arguments(*get_config_info())

    configure(arguments)

    configure_s(('length', 3), ('level', 4), ('security', 10))

    configure_ks(length=3, level=3, security=10)

    configure_map = {
        "level": 3,
        "length": 3,
        "security": 10,
    }

    control_by_configure(**configure_map)

    function_with_arbitary_arguments(10, 20, 30, key=10, age=20, same=False)
