# -*- coding: utf-8 -*-
#「"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
# という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import re

str = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
str = re.sub(r'[,|.]', '', str)
list = []
for word in str.split(' '):
    list.append(len(word))

print(list)
