# -*- coding: utf-8 -*-
# 記事から参照されているメディアファイルをすべて抜き出せ．

import json
import re

INPUT_PATH = './input/jawiki-country.json'
TARGET = 'イギリス'

records = []
for line in open(INPUT_PATH, 'r'):
    records.append(json.loads(line))

pattern = re.compile(r'\[\[(File|ファイル):(.+?)\|.*?\]\]')
for record in records:
    results = pattern.findall(record['text'])
    for r in results:
        print(r[1])
