# -*- coding: utf-8 -*-
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

# =================================================
# N=[分割数]
# mkdir ./output/16
# rm -rf ./output/16/*
# LINES=$(($(cat ./input/hightemp.txt | wc -l)/$N))
# if [ $(( $LINES % N )) -gt 0]; then
#  LINES=$(($LINES+1))
# fi
# split -l $LINES ./input/hightemp.txt ./output/16/

import numpy as np
import shutil
import os

INPUT_PATH = './input/hightemp.txt'
OUTPUT_DIR = './output/16'

n = int(input())
lines = open(INPUT_PATH).readlines()
if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.makedirs(OUTPUT_DIR)
for i, block in enumerate(np.array_split(lines, n), start=1):
    with open(f'{OUTPUT_DIR}/{i}.txt', 'w') as f:
        for line in block:
            f.write(line)
