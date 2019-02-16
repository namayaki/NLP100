# -*- coding: utf-8 -*-
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

# =================================================
# head ./input/hightemp.txt -n [N]

import linecache

INPUT_PATH = './input/hightemp.txt'

n = int(input())
for i in range(1, n+1):
    print(linecache.getline(INPUT_PATH , i).rstrip())
