# -*- coding: utf-8 -*-
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

import json
import re

INPUT_PATH = './input/jawiki-country.json'
TARGET = 'イギリス'

records = []
for line in open(INPUT_PATH, 'r'):
    records.append(json.loads(line))

pattern = re.compile(r'(={2,})\s*(.+?)\s*\1')
for record in records:
    results = pattern.findall(record['text'])
    for r in results:
        print(f'{r[1]}({len(r[0])})')
