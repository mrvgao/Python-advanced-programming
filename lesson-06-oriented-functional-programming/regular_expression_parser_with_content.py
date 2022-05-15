def match_1(p, text):
    if text == '': return None

    return text[0] if (p == text[0] or p == '.') else None


assert match_1('a', 'anew')  == 'a'
assert match_1('a', '') is None
assert match_1('.', 'a') == 'a'
assert match_1('a', 'b') is None
print('test done!')


def match_plus(p, _pat, text):
    # a*bcd => p: a, _pat: bcd,  text: abcdefg
    prefix = match_1(p, text)
    tail_match_remain = match(_pat, text[1:])
    tail_match_with_plus = match_plus(p, _pat, text[1:])

    tail = tail_match_remain or tail_match_with_plus

    if prefix and tail:
        return prefix + tail
    else:
        return None


def match(pat, text):
    """
    return:
        None: if pat not be found in the text begining
        string: the matched sub-string in the text begining
    """
    if text == '':
        return '' if pat == '' else None
    elif pat == '':
        return ''
    elif pat == '$':
        return text if text == '' else None
    elif len(pat) > 1 and pat[1] in '*?+':
        p, op, _pat = pat[0], pat[1], pat[2:]
        if op == '*':
            return match(_pat, text) or match_plus(p, _pat, text)
        elif op == '?':
            match_with_one = match(p + _pat, text)
            match_without_one = match(_pat, text)
            return match_with_one or match_without_one
            # return match(p + _pat, text) or match(_pat, text)
        elif op == '+':
            return match_plus(p, _pat, text)
    else:
        head = match_1(pat[0], text)
        tail = match(pat[1:], text[1:])
        # match('test', 'test') -> 'test'
        # match('a', 'a') = 'a'

        if head and tail is not None:
            return head + tail
        else:
            return None


#        return match_1(pat[0], text) and match(pat[1:], text[1:])


def search(pat, text):
    """
    return if pat exists in this text
    >>> search('a', 'a')
    'a'
    # >>> search("a", 'b')
    # None
    # >>> search('p?hone', 'phone')
    # phone
    # >>> search('p?hone', 'hone')
    # hone
    >>> search('p?hone', 'this is my honey')
    honey
    >>> search('^ph?one*', 'poneeeee something else')
    poneeeee
    >>> search('^ph?one*', 'phon')
    phon
    >>> search('^ph?one*', 'iphone')
    None
    >>> search('^ph?one*.*!$', 'phone number!')
    phone number!
    >>> search('^ph?one*.*!$', 'phone number')
    None
    """
    if pat.startswith('^'):
        # e.g ^phone, ^1.*
        return match(pat[1:], text)
    else:
        for i in range(len(text)):
            r = match(pat, text[i:])
            if r: return r
        return None

