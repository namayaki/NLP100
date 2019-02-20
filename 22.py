# -*- coding: utf-8 -*-
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import json
import re

INPUT_PATH = './input/jawiki-country.json'
TARGET = 'イギリス'

records = []
for line in open(INPUT_PATH, 'r'):
    records.append(json.loads(line))

pattern = re.compile(r'\[\[Category:(.+)\]\]')
for record in records:
    for line in record['text'].split('\n'):
        m = pattern.match(line)
        if m:
            print(m.group(1))
