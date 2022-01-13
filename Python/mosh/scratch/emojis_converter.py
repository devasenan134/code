# python 3.7.1
def emojis_converter(msg):
    words = msg.split(" ")
    output = ''
    emojis = {':)': '😀', ':(': '☹️', ':|': '😐', '_/\_': '🙏🏻'}
    for word in words:
        output += emojis.get(word, word)+' '
    return output
