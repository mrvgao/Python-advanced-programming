def search_1(p, t):
    """
    >>> search_1('.', 'a')
    True
    >>> search_1('a', 'a')
    True
    >>> search_1('a', 'b')
    False
    >>> search_1('a', '')
    False
    """
    if not t: return False

    return p == '.' or p == t


def match_1(p, text):
    if text == '': return False

    return search_1(p, text[0])


def match_plus(p, _pat, text): # a*bcd => p: a, _pat: bad
    # a+bcd                           abcde ; aaaabcd
    return match_1(p, text) and (
       match(_pat, text[1:]) or match_plus(p, _pat, text[1:])
    )


def match(pat, text):
    if pat == '':
        return True
    elif pat == '$':
        return text == ''
    elif len(pat) > 1 and pat[1] in '*?+':
        p, op, _pat = pat[0], pat[1], pat[2:]
        if op == '*':
            return match(_pat, text) or match_plus(p, _pat, text)
        elif op == '?':
            return match(p + _pat, text) or match(_pat, text)
        elif op == '+':
            return match_plus(p, _pat, text)
    else:
        return match_1(pat[0], text) and match(pat[1:], text[1:])


def search(pat, text):
    """
    return if pat exists in this text
    >>> search('p?hone', 'phone')
    True
    >>> search('p?hone', 'hone')
    True
    >>> search('p?hone', 'this is my honey')
    True
    >>> search('^ph?one*', 'poneeeee')
    True
    >>> search('^ph?one*', 'phon')
    True
    >>> search('^ph?one*', 'iphone')
    False
    >>> search('^ph?one*.*!$', 'phone number!')
    True
    >>> search('^ph?one*.*!$', 'phone number?')
    False
    """
    if pat.startswith('^'):
        # e.g ^phone, ^1.*
        return match(pat[1:], text)
    else:
        return match('.*' + pat, text)
