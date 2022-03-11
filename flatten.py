def flatten(elements):
    match elements:
        case []: return []
        case list() | tuple() | set() as first, *remains:
            return flatten(first) + flatten(remains)
        case _: return [elements[0]] + flatten(elements[1:])


if __name__ == '__main__':
    simple = [0, 1, (2, 3)]
    L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
    nest = [(0, 1), (2, 3), 4, 5, ((6, 7, 8), ((9, 10), ((11, 12, ((13, 14), 15), 16), 17)))]

    print(flatten(simple))
    print(flatten(L))
    print(flatten(nest))
