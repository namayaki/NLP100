# -*- coding: utf-8 -*-
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

# =================================================
# cat ./input/hightemp.txt | cut -d $'\t' -f 1 > ./output/col1.txt
# cat ./input/hightemp.txt | cut -d $'\t' -f 2 > ./output/col1.txt

INPUT_PATH = './input/hightemp.txt'
OUT_PATH1 = './output/col1.txt'
OUT_PATH2 = './output/col2.txt'

f1 = open(OUT_PATH1, 'w')
f2 = open(OUT_PATH2, 'w')

for line in open(INPUT_PATH, 'r'):
    cols = line.split('\t')
    f1.write(cols[0]+'\n')
    f2.write(cols[1]+'\n')
