# -*- coding: utf-8 -*-
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）

# =================================================
# cat ./input/hightemp.txt | sort -k 3 -n -r -t $'\t'

INPUT_PATH = './input/hightemp.txt'

records = []
f = open(INPUT_PATH, 'r')
for line in sorted(f.readlines(), key=lambda x: x.split('\t')[2], reverse=True):
    print(line.rstrip())
