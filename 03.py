# -*- coding: utf-8 -*-
#「"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import re

STR = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

list = []
for word in re.sub(r'[,|.]', '', STR).split(' '):
    list.append(len(word))

print(list)
