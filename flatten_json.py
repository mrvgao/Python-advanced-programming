def parse_json(json_string):
    match json_string:
        case {'text': str(name), 'color': str(c)}:
            print(f'Give {name} with color {c}')
        case {'sleep': str(state), 'time': str(t)}:
            print(f'{state} for {t}')
        case {'sleep': str(state), 'time': int(c), 'person': {'name': str(name), 'age': int(age)}}:
            print(f'{name} with age {age} has been {state} for {c}')
        case _:
            raise TypeError('invalid Json')


if __name__ == '__main__':
    color_json = {'text': 'Car', 'color': 'Red'}
    state_json = {'sleep': 'off', 'time': '10'}
    state_with_person = {'sleep': 'off', 'time': 10, 'person': {'name': 'John', 'age': 20}}

    parse_json(color_json)
    parse_json(state_json)
    parse_json(state_with_person)
