# python 3.7.1


def split(msg):
    line = []
    word = ''
    for ch in msg:
        if ch != ' ':
            word += ch
        elif ch == ' ':
            line.append(word)
            word = ''
    line.append(word)
    return line

