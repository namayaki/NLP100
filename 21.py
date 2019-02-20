# -*- coding: utf-8 -*-
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import json
import re

INPUT_PATH = './input/jawiki-country.json'
TARGET = 'イギリス'

records = []
for line in open(INPUT_PATH, 'r'):
    records.append(json.loads(line))

pattern = re.compile(r'\[\[Category:.+\]\]')
for record in records:
    for line in record['text'].split('\n'):
        if pattern.match(line):
            print(line)
