# -*- coding: utf-8 -*-
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

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
