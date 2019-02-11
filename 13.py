# -*- coding: utf-8 -*-
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

# =================================================
# paste -d '\t' ./input/col1.txt ./input/col2.txt

INPUT_PATH1 = './input/col1.txt'
INPUT_PATH2 = './input/col2.txt'
OUTPUT_PATH = './output/13.txt'

f1 = open(INPUT_PATH1, 'r')
f2 = open(INPUT_PATH2, 'r')
output = open(OUTPUT_PATH, 'w')

for col1, col2 in zip(f1, f2):
    output.write(col1.rstrip() + '\t' + col2.rstrip() + '\n')
