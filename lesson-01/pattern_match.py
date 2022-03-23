# Pattern Match

def parse_json(parsed_json):
    """
    possible input: {
        "Age": 19,
        "USER-ID: uuid1231241,
        "goods-info": {
            "price": 100,
            "createtime": 2022
        }
    }

    possible input: {
        "name": Tome,
        "USER-ID": uuid1231241,
        "action-info": {
            "last-login": March-22
        }
    }
    """
    match parsed_json:
        case {'name': str(name), 'user-id': str(userd_id), "goods-info": {"price": float(p), 'createtime': str(time_)}}:
            print(f"{name} with id {userd_id} bought {p} goods")
        case {'Age': str(age), 'user-id': str(userd_id), "action-info": {"last-login": str(p)}}:
            print(f"{userd_id} with age {age} last login is {p}")
        case _:
            raise TypeError('invalid json format')



