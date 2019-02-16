# -*- coding: utf-8 -*-
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

# =================================================
# tail -n [N] ./input/hightemp.txt

import linecache

INPUT_PATH = './input/hightemp.txt'

n = int(input())
lines = len(open(INPUT_PATH).readlines())
for i in range(n):
    print(linecache.getline(INPUT_PATH , lines - n + i + 1).rstrip())
