# -*- coding: utf-8 -*-
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

import re

STR = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
TARGET = [1, 5, 6, 7, 8, 9, 15, 16, 19]

ans = {}
for i, word in enumerate(re.sub(r'[,|.]', '', STR).split(' '), 1):
    if i in TARGET:
        ans[word[0]] = i
    else:
        ans[word[:2]] = i

print(ans)
