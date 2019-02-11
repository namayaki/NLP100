# -*- coding: utf-8 -*-
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ

STR = 'I am an NLPer'

def generate_ngram(str, n):
    list = []
    for i in range(0, len(str) - n + 1):
        list.append(str[i:i+n])
    return list

print(generate_ngram(STR.split(' '), 2))
print(generate_ngram(STR, 2))
