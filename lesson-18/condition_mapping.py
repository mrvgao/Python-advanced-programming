 condition_mapping = {
        lambda x: 'test' in x: do_something_1,
        lambda len(x) > 10: do_something_1,
        lambda len(x) > 15: do_something_2,
        lambda len(x) > 20: do_something_3,
        lambda len(x) > 25: do_something_4,
        lambda len(x) > 35: do_something_5,
        lambda len(x) > 40: do_something_6,
        lambda len(x) > 50: do_something_7,
        lambda len(x) > 10: do_something_8,
}


def condition_mapping(arg, condition_mapping, default_action):
    for cond, action in condition_mapping.items():
        if cond(string): 
            action(string)
            break
    else:
        default_action(string)
