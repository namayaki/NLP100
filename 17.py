# -*- coding: utf-8 -*-
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

# =================================================
# cat ./input/hightemp.txt | cut -d $'\t' -f 1 | sort | uniq

INPUT_PATH = './input/hightemp.txt'

records = set()
for line in open(INPUT_PATH, 'r'):
    cols = line.split('\t')
    records.add(cols[0])

for str in sorted(list(records)):
    print(str)
