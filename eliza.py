import re
from flatten import flatten
import random
from eliza_rules import rule_responses


PAT = re.compile(r'(\?[\*|\+](\w))')


def split_by_rule(text, rule):
    not_placeholders = [s.strip() for s in PAT.sub(' ', rule).split()]

    return split_by(text, not_placeholders)


def split_by(string, keywords):
    pat = re.compile('|'.join(keywords))
    spans = [s.span() for s in pat.finditer(string)]

    all_split_indices = flatten(spans)

    if all_split_indices and all_split_indices[0] != 0: all_split_indices = [0] + all_split_indices
    if all_split_indices and all_split_indices[-1] != len(string): all_split_indices.append(len(string))

    split_sentence = [string[index: all_split_indices[i + 1]] for i, index in enumerate(all_split_indices[:-1])]

    return split_sentence


def generate_match_case_by_rule(rule):
    split_rule = split_by_rule(rule, rule)
    rule_clean = PAT.sub(r'\g<2>', str(split_rule))
    rule_clean = re.sub("'([a-z])'", r'\g<1>', str(rule_clean))

    return rule_clean


def give_response(response):
    var_with_arg = [re.sub(r'\?([a-z])', "{\g<1>}", s) for s in response]
    return var_with_arg


def text_match(split_text, rule, response):
    pattern = generate_match_case_by_rule(rule)

    res = random.choice(give_response(response))

    script = f"""def _match(split_text):
    match split_text:
        case {pattern}:
            # print(split_text)
            # print('匹配到了')
            print(f"Q: {''.join(split_text)}")
            print(f"回答：{res}")
            return True
        case _:
            # print('匹配不到')
            return False
    """

    print(f"生成的程序是: {script}")
    exec(script)
    match = eval("_match(split_text)")

    return match


if __name__ == '__main__':
    test_cases = [
        "Minquan我想开飞机",
        "我觉得这个世界可能是虚拟的",
        "医生我昨天梦见一只山羊",
        "医生你为什么不去读个博士",
        "简直就是开玩笑",
        "大壮和小强和小明还有秃头都是很坏的人"
    ]

    for text in test_cases:
        for rule, response in rule_responses.items():
            text_match(split_by_rule(text, rule), rule, response)