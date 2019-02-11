# -*- coding: utf-8 -*-
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

STR1 = 'paraparaparadise'
STR2 = 'paragraph'

def generate_ngram(str, n):
    list = []
    for i in range(0, len(str) - n + 1):
        list.append(str[i:i+n])
    return list

X = set(generate_ngram(STR1, 2))
Y = set(generate_ngram(STR2, 2))

print(set.union(X,Y))
print(set.intersection(X,Y))
print(set.difference(X,Y))
print('se' in X)
print('se' in Y)
