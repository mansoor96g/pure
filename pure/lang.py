



def toid(text, delim = '-'):
    #  TODO Documentation
    if text is None:
        return None

    text = text.strip().lower()

    result = []
    for c in text:
        if c in 'abcdefghijklmnopqrstuvwxyz1234567890':
            result.append(c)
        else:
            result.append(delim)

    result = ''.join(result)
    while (delim + delim) in result:
        result = result.replace((delim + delim), delim)

    return result
