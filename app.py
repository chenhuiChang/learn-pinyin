import re

from flask import Flask, request, render_template
from pypinyin import pinyin, Style

app = Flask(__name__)


def is_chinese_char(char):
    return '\u4e00' <= char <= '\u9fff'


def is_english_letter(char):
    return char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_pinyin(text):
    pinyin_list = pinyin(text, errors='ignore', style=Style.NORMAL)
    if len(pinyin_list) == 0:
        return text
    return pinyin_list[0][0]


def split_input(text):
    # Regular expressions to match Chinese characters and to identify punctuation
    chinese_char_re = re.compile(r'[\u4e00-\u9fff]')
    punctuation_re = re.compile(r'[^\w\s]')

    result = []
    buffer = ""

    for char in text:
        if punctuation_re.match(char):
            continue  # Skip punctuation
        elif chinese_char_re.match(char):
            if buffer:
                result.extend(buffer.split())  # Split buffer on spaces
                buffer = ""
            result.append(char)
        else:
            buffer += char

    if buffer:
        result.extend(buffer.split())  # Split buffer on spaces if anything is left

    return result


def convert_to_pinyin(text):
    pinyin_text = ""
    for char in text:
        if char in [' ', '～', '，', '、', ',', '。', ',', '.', '~', '`']:
            return ' '
        pinyin_text += get_pinyin(char)
    return pinyin_text


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/show', methods=['POST'])
def show():
    if request.method == 'POST':
        text = request.form['text']
        text_list = split_input(text)
        original_text_list = []
        pinyin_text_list = []
        for text in text_list:
            original_text_list.append(text)
            pinyin_text_list.append(convert_to_pinyin(text))
        original_text = ' '.join(original_text_list)
        pinyin_text = ' '.join(pinyin_text_list)
        return render_template('show.html', originalText=original_text, pinyinText=pinyin_text)


if __name__ == '__main__':
    app.run(debug=True)
