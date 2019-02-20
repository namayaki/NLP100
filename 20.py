# -*- coding: utf-8 -*-
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．

import json

INPUT_PATH = './input/jawiki-country.json'

records = []
for line in open(INPUT_PATH, 'r'):
    records.append(json.loads(line))

for record in records:
    if 'イギリス' in record['title']:
        print(record['text'])
