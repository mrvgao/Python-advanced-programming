import requests


def get_webpage(url):
    r = requests.get(url)
    r.encoding = 'gbk'

    return r.text


def get_subway_page():
    url = 'https://www.bjsubway.com/station/xltcx/'
    text = get_webpage(url)
    return text


def is_line_start_line(line):
    mark = '<div class="subway_num'
    if mark in line:
        return True
    else:
        return False


def get_line_number(line):
    right = line.rfind('<')  # find start from right
    left = line.find('>')

    return line[left+1:right]


def is_target_line(line, line_num):
    if is_line_start_line(line) and get_line_number(line) == line_num:
        return True
    else:
        return False


def is_end_of_line_block(line):
    mark = '<div class="line_name">'
    if mark in line:
        return True
    else:
        return False


def get_target_line_info_block(page, line_num):
    target_lines = []
    start_record = False

    for line in page.split('\n'):
        if is_target_line(line, line_num):
            start_record = True
            continue

        if start_record and is_end_of_line_block(line):
            break

        if start_record:
            target_lines.append(line)

    return target_lines


def contain_station_info(line):
    mark = '/station/xltcx/'
    """
    'return mark in line' equals to
    if mark in line:
        return True
    else:
        return False
    """
    return mark in line


def get_station_info(line):
    left_mark = 'html">'
    left_index = line.find(left_mark) + len(left_mark)
    right_mark = '</a>'
    right_index = line.rfind(right_mark)

    return line[left_index:right_index]


def get_stations(line_info_lines):
    stations = []

    for line in line_info_lines:
        if contain_station_info(line):
            stations.append(get_station_info(line))

    return stations


def composing_get_line_stations(line_name, text=None):
    if text is None: text = get_subway_page()

    lines = get_target_line_info_block(text, line_name)

    stations = get_stations(lines)

    return stations

""" 
Advanced part: 学有余力部分

    In the previous part, we noticed that: 
        - is_line_start_line()
        - is_end_of_line_block()
        - contain_station_info() 
        
        are very similar 
        
    we could do some further. 
"""


def test_contain(mark):
    """
    You can analyse the mechanises of this function, and the following assignment statements.
    """

    def _inner(line):
        return mark in line

    return _inner


new_is_line_start_line = test_contain('<div class="subway_num')
new_is_end_of_line_block = test_contain('<div class="line_name">')
new_contain_station_info = test_contain('/station/xltcx/')


"""
Similarly, the: 
    - get_line_number()
    - get_station_info()
    
    two function also are similar
    
    we can use the following function to simplify the functino define. 
"""


def get_span(left_mark, right_mark):
    def _inner(line):
        return line[line.find(left_mark)+len(left_mark):line.rfind(right_mark)]

    return _inner


new_get_line_number = get_span(left_mark='>', right_mark='<')
new_get_station_info = get_span(left_mark='html">', right_mark='</a>')


"""
Try to use the new__XXX function to substitute the XXX function.   

Analyse the difference and the advantage of above simplify. 
Try to compare the length of original version and simplified version.
Try to deeply understand the python function.
"""

if __name__ == '__main__':
    # -- step-01: get page from web
    # url = 'https://www.bjsubway.com/station/xltcx/'
    # text = get_webpage(url)

    # text = get_subway_page()

    # -- step-02: save to text file, avoid repetitive getting.
    # with open('subway.txt', 'w') as f:
    #     f.write(text)

    # -- step-03: test is_line_start_line function

    with open('subway.txt', 'r') as f:
        for line in f.read().split('\n'):
            if is_line_start_line(line):
                print(line)
                print(get_line_number(line))

    # --step-04: test is_target_line function

    with open('subway.txt', 'r') as f:
        for line in f.read().split('\n'):
            if is_target_line(line, '1号线/八通线'):
                print(f'find line 1: {line}')
            if is_target_line(line, '2号线'):
                print(f'找到了二号线: {line}')

    lines = get_target_line_info_block(open('subway.txt').read(), '2号线')

    for line in lines:
        print(line)

    # finally: compose it together
    print(composing_get_line_stations('5号线', open('subway.txt').read()))
    print(composing_get_line_stations('13号线', open('subway.txt').read()))
