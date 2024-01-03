#!/usr/bin/python3
"""
The ``5-text_indentation`` module
This ``text_indentation`` supplies one function, text_indentation(text)
"""


def text_indentation(text):
    """Print the formated text based on these characters: ., ? and :
    Args:
        text (str): text to be formated
    Returns:
        None
    """
    cnt = 0
    tmp = 0
    tmp_str = None
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            cnt += 1
            tmp_str = text[tmp:cnt]
            print(tmp_str.strip())
            print()
            tmp = cnt + 1
        else:
            cnt += 1
    if tmp_str is None:
        print(text, end="")
    else:
        print(text[tmp - 1:].strip(), end="")
