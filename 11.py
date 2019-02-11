# -*- coding: utf-8 -*-
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

# =================================================
# sed s/$'\t'/' '/g ./input/hightemp.txt
# cat ./input/hightemp.txt | tr '\t' ' '
# expand -t 1 ./input/hightemp.txt

INPUT_PATH  = './input/hightemp.txt'
for line in open(INPUT_PATH, 'r'):
  print(line.replace('\t', ' '), end='')
