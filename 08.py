# -*- coding: utf-8 -*-
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# ・英小文字ならば(219 - 文字コード)の文字に置換
# ・その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

import re

def cipher(txt):
    result = ''
    for c in txt:
        if c.islower():
            result = result + chr(219-ord(c))
        else:
            result = result + c
    return result

print(cipher('ABCDEabcde'))
