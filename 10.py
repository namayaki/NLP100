# -*- coding: utf-8 -*-
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# =================================================
# wc -l ./input/hightemp.txt

INPUT_PATH = './input/hightemp.txt'
count = len(open(INPUT_PATH).readlines())
print(count)
