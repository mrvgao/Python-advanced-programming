def test_pattern_match(json):
    match json: 
        case {"name": name, "age": age}: 
            print(name, age)
        case {"user_info": {"name": name, "age": age}, "action": {"login": login_time}}: 
            print(name, age, login_time)
        case {"user_info": {"name": name, "age": age}, "action": {"login": login_time, "login_counts": login_counts}}: 
            print(name, age, login_time, login_counts)
        default: 
            print('invalid json')
