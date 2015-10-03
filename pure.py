

def connect(path):
    import sqlite3
    connection = sqlite3.connect(path, timeout=15)
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

    content = '\t'.join(strargs) + '\t' + '\t'.join(pairs)
    if 'logfile' in globals():
        logfile.write(content)
        logfile.write('\n')
    else:
        print content

def csv_dict(path, key = None, delimiter = '\t'):
    import csv
    import collections

    result = collections.OrderedDict()
    with open(path) as f:
        reader = csv.DictReader(f, delimiter = delimiter)
        if key is None:
            key = reader.fieldnames[0]

        for row in reader:
            k = row[key]
            result[k] = row
    return result


def csv_array(path, delimiter = '\t'):
    import csv
    import collections

    result = []
    with open(path) as f:
        reader = csv.DictReader(f, delimiter = delimiter)

        for row in reader:
            result.append(row)
    return result



def get_md5(data):
    import hashlib
    md5 = hashlib.md5()
    md5.update(text)
    return md5.hexdigest()


def datestr(fmt='%s'):
    import datetime
    return datetime.datetime.now().strftime(fmt)

def current_folder_name():
    path = os.path.abspath(os.curdir)
    folder = os.path.basename(path)
    return folder


def ensure_dir(path):
    abspath = os.path.abspath(path)
    try:
        parent = os.path.dirname(abspath)
        if not os.path.exists(parent):
            os.makedirs(parent)
    except:
        pass

connect('test.db')