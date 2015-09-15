

def connect(path):
    import sqlite3
    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    connection.text_factory = str
    return connection


def toid(text, delim = '-'):
    if text is None:
        return ''

    text = delim + text + delim
    result = []
    text = text.lower()

    for c in text:
        if c in '0123456789abcdefghijklmnopqrstuvwxyz':
            result.append(c)
        else:
            result.append(delim)

    result = ''.join(result)
    while (delim + delim in result):
        result = result.replace(delim + delim, delim)
    return result[1:-1]


def log(*args, **kws):
    import collections

    strargs = [str(a) for a in args]
    pairs = []

    for k, v in kws.items():
        k = str(k)
        v = str(v)
        pairs.append(k + ': ' + v)

    print '\t'.join(strargs) + '\t' + '\t'.join(pairs)

def csv_dict(path, key = None):
    import csv
    import collections

    result = collections.OrderedDict()
    with open(path) as f:
        reader = csv.DictReader(f, delimiter = '\t')
        if key is None:
            key = reader.fieldnames[0]


        for row in reader:
            k = row[key]
            result[k] = row
    return result