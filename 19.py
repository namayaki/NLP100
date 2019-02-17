# -*- coding: utf-8 -*-
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

# =================================================
# cat ./input/hightemp.txt | cut -d $'\t' -f 1 | sort | uniq -c | sort -r

INPUT_PATH = './input/hightemp.txt'

counts = {}
for line in open(INPUT_PATH, 'r'):
    cols = line.split('\t')
    if cols[0] not in counts:
         counts[cols[0]] = 0
    counts[cols[0]] += 1

for data in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(f'{data[0]}({data[1]})')
