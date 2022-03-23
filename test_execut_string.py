"""
if string.stratswith(XX): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()
elif string.startwith(YY): do_something()

"""
def decision_process(conditions, outs):
    base_string = f"if string.startswith('{conditions[0]}'): print('{outs[0]}')"    

    for c, out in zip(conditions[1:], outs[1:]):
        base_string += f"\n\telif string.startswith('{c}'): print('{out}')"    


    return base_string


def create_func(conditions, outs):
    return f"""def complexit_if(string):
\t{decision_process(conditions, outs)} 
    """

programming = create_func(['0', '1', '2'], ['none', 'first', 'second'])

exec(programming)
exec("complexit_if('001231')")
exec("complexit_if('101231')")
exec("complexit_if('201231')")













